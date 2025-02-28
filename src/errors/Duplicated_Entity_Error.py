from fastapi import HTTPException


class Duplicated_Entity_Error(HTTPException):
    def __init__(self, detail: str = "The Entity already exists in this context"):
        super().__init__(status_code=422, detail=detail)
