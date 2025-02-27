
from fastapi import Depends
from database.db import get_db
from users_api.dtos.create_user_dto import Create_User_DTO
from users_api.models.User_entity import User
from users_api.repository.User_repository import  get_user_repository, UserRepository
from sqlalchemy.ext.asyncio import AsyncSession


class List_Users_Usecase:
    def __init__(self, user_repository: UserRepository, db: AsyncSession):
        self.user_repository = user_repository
        self.db = db

    async def execute(self) -> list[User]:
        return await self.user_repository.list_users(self.db)


async def get_list_users_use_case(
    user_repo: UserRepository = Depends(get_user_repository),
    db: AsyncSession = Depends(get_db),
) -> List_Users_Usecase:
    return List_Users_Usecase(user_repository=user_repo, db=db)





# from typing import Callable
# from fastapi import Depends
# from database.db import get_db
# from users_api.models.User_entity import User
# from sqlalchemy.ext.asyncio import AsyncSession

# from users_api.repository.users_queries import list_users_query


# class List_Users_Usecase:
#     def __init__(self, listUsersQuery:Callable[[AsyncSession], list[User]], db: AsyncSession):
#         self.listUsersQuery = listUsersQuery
#         self.db = db

#     async def execute(self) -> list[User]:
#         return await self.listUsersQuery(self.db)


# async def get_list_users_use_case(
#     user_repo: Callable[[AsyncSession], list[User]] = list_users_query,
#     db: AsyncSession = Depends(get_db),
# ) -> List_Users_Usecase:
#     return List_Users_Usecase(listUsersQuery=user_repo, db=db)

