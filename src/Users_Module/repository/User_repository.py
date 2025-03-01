from fastapi import Depends
from database.db import get_db
from src.Users_Module.dtos.create_user_dto import Create_User_DTO
from src.Users_Module.dtos.update_user_dto import Update_User_DTO
from src.Users_Module.models.User_entity import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.errors.Not_Found_Exception import NotFoundException
from sqlalchemy import exc
from fastapi import HTTPException

from src.helpers.io_helper import update_entity_data


class UserRepository:
    async def create_user(
        self, user: Create_User_DTO, db: AsyncSession = Depends(get_db)
    ) -> User:
        """
        Creates a new user or restores a deleted user.

        Args:
            user (Create_User_DTO): Data transfer object containing user details.
            db (AsyncSession, optional): Database session. Defaults to Depends(get_db).

        Raises:
            HTTPException: If the email already exists.
            SQLAlchemyError: If there is a database error.

        Returns:
            User: The created or restored user.
        """
        user_found = await self.get_user_by_email_with_deleted(email=user.email, db=db)
        if user_found != None and user_found.deleted_at != None:
            user_found.restore()
            setattr(user_found, "password", user.password)
            user_found.hash_password()
            try:
                await db.commit()
                await db.refresh(user_found)
                return user_found
            except exc.SQLAlchemyError as e:
                print(e.code)
                raise e
        else:
            user_to_create = user.model_dump()
            user = User(**user_to_create)
            user.hash_password()
            try:
                db.add(user)
                await db.commit()
                await db.refresh(user)
                return user
            except exc.SQLAlchemyError as e:
                print(e.code)
                if e.code == "gkpj":

                    raise HTTPException(
                        detail=[{"loc": ["email"], "msg": "The email already exists"}],
                        status_code=422,
                    )
                raise e

    async def list_users(self, db: AsyncSession = Depends(get_db)):
        result = await db.execute(select(User).filter(User.deleted_at.is_(None)))
        return result.scalars().all()

    async def get_user_by_id(self, user_id: str, db: AsyncSession = Depends(get_db)):
        result = await db.execute(
            select(User).filter(User.deleted_at.is_(None)).where(User.id == user_id)
        )
        user = result.scalars().first()
        if user is None:
            raise NotFoundException(f"User with id: {user_id} not found")
        return user

    async def get_user_by_id_with_deleted(
        self, user_id: str, db: AsyncSession = Depends(get_db)
    ):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if user is None:
            raise NotFoundException(detail=f"User with id: {user_id} not found")
        return user

    async def get_user_by_email_with_deleted(
        self, email: str, db: AsyncSession = Depends(get_db)
    ):
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalars().first()
        return user

    async def update_user(
        self,
        user_id: str,
        user_data: Update_User_DTO,
        db: AsyncSession = Depends(get_db),
    ):
        payload = user_data.model_dump(exclude_none=True, exclude_unset=True)
        user = await self.get_user_by_id(user_id, db=db)
        updated_entity = update_entity_data(payload_obj=payload, entity_to_update=user)
        await db.commit()
        await db.refresh(updated_entity)
        return updated_entity

    async def delete_user(self, user_id: str, db: AsyncSession = Depends(get_db)):
        user = await self.get_user_by_id(user_id, db)
        user.soft_delete()
        await db.commit()
        await db.refresh(user)

    async def hard_delete_user(self, user_id: str, db: AsyncSession = Depends(get_db)):
        user = await self.get_user_by_id_with_deleted(user_id, db)
        await db.delete(user)
        await db.commit()


async def get_user_repository():
    return UserRepository()
