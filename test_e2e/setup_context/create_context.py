# from typing import Annotated, List
# from sqlalchemy.ext.asyncio import AsyncSession

# from src.Business_Module.dtos.business_dtos.create_business_dto import (
#     Create_Business_DTO,
# )
# from src.Business_Module.dtos.space_dtos.create_space_dto import Create_Space_DTO
# from src.Business_Module.models.business_entity import Business
# from src.Business_Module.models.space_entity import Space
# from src.Business_Module.repository.business_repository import get_business_repository
# from src.Users_Module.dtos.create_user_dto import Create_User_DTO
# from src.Users_Module.dtos.role_dto import Role_DTO
# from src.Users_Module.models.Role_entity import Role
# from src.Users_Module.models.User_entity import User
# from src.Users_Module.repository.User_repository import get_user_repository
# from src.Users_Module.value_objects.Role_Type import Staff_Role_literal_Enum
# from test_e2e.setup_context.constants import ContextPayload


# class StaffForTest:
#     user: Create_User_DTO
#     role: Staff_Role_literal_Enum


# class CreateContext:
#     def __init__(self, db: AsyncSession):
#         self.db = db

#     async def create_client(self, clients: List[Create_User_DTO]):
#         pass

#     async def create_business(self, businesses: List[Create_Business_DTO]):
#         pass

#     async def create_spaces(self, spaces: List[Create_Space_DTO]):
#         pass

#     async def create_roles(self, roles: List[Role_DTO]):
#         pass

#     async def create(self, *args, **kwargs) -> dict:
#         clients_created: List[User] = None
#         business_created: Business = None
#         staffs_created: List[User] = None
#         spaces_created: List[Space] = None
#         roles_created: List[Role] = None

#         clients: List[Create_User_DTO] = kwargs["clients"]
#         if len(clients) > 0:
#             user_repo = get_user_repository()
#             clients_created = await user_repo.bulk_create_users(
#                 users=clients, db=self.db
#             )
#             # Use clients_created in some way, for example, return it
#             # return {"clients_created": clients_created}

#         business: Create_Business_DTO = kwargs["business"]
#         if business != None:
#             business_repo = get_business_repository()
#             business_created = await business_repo.create_business(
#                 business_payload=business, db=self.db
#             )

#         staffs: List[StaffForTest] = kwargs["staffs"]
#         if len(staffs) > 0:
#             user_repo = get_user_repository()
#             staffs_created = await user_repo.bulk_create_users(users=staffs, db=self.db)
#         spaces: List[Create_Space_DTO] = kwargs["spaces"]
#         # step 1: Create Default Business
#         # step 2: Create Default Spaces for business
#         # step 3: Create Default staff users for business
#         # step 4: Create Roles for those staffs related with Default Business
#         # step 5: Log Default users in
#         # step 5: Return a dict with:
#         """
#         {
#             default_bar_id: str
#             staffs: List[
#                 {
#                     staff_type: str
#                     user_id: str
#                     business_id: str
#                 }
#             ]
#         }
#         """
#         return {
#             "default_bar_id": business_created.id,
#             "clientes": clients_created,
#             "staffs": staffs,
#             "spaces": spaces,
#         }
