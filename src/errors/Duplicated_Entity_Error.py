from fastapi import HTTPException
from starlette import status


class Duplicated_Entity_Error(HTTPException):
    def __init__(self, detail: str = "The Entity already exists in this context"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
