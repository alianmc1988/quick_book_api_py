from dataclasses import dataclass
from uuid import UUID

from fastapi import HTTPException, Request
from src.Auth_Module.constants.access_levels import AccessLevel
from src.Users_Module.models.User_entity import User
from src.errors.Unauthorized_Exception import ForbiddenException


@dataclass
class Base_Controller:
    def __init__(self, access_level: AccessLevel = None):
        self.access_level = access_level
        self.logged_user: User | None = None
        self.ctx: str | None = None

    def get_access_level(self):
        return self.access_level

    def _user_belong_to_ctx(self, ctx: UUID, user: User):
        if not ctx:
            raise HTTPException(detail="Missing Context Header", status_code=400)

        is_part_of_context = False
        role_name = None
        for role in user.roles:
            if ctx == str(role.business_id):
                is_part_of_context = True
                role_name = role.role
                break
        return (is_part_of_context, role_name)

    def access_control(self, request: Request):
        self.logged_user = request.state.logged_user
        self.ctx = request.headers.get("X-Context")

        if not self.logged_user:
            raise ForbiddenException("User cannot access this resource")

        if self.get_access_level() is None or self.logged_user.is_master_user():
            return

        is_part_of_context, role_name = self._user_belong_to_ctx(
            ctx=self.ctx, user=self.logged_user
        )

        if is_part_of_context and role_name <= self.get_access_level():
            return

        raise ForbiddenException("User cannot access this resource")

    @classmethod
    async def define(self):
        raise NotImplementedError()

    async def handle(self):
        return await self.define()
