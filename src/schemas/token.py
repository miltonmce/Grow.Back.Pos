from typing import Optional

from pydantic import BaseModel


class TokenData(BaseModel):
    """_summary_
    Args:
        BaseModel (_type_): _description_
    """
    username: Optional[str] = None


class Status(BaseModel):
    """_summary_
    Args:
        BaseModel (_type_): _description_
    """
    message: str
