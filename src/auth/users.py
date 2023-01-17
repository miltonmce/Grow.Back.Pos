from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist

from src.database.models import Users
from src.schemas.users import UserDatabaseSchema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    """_summary_
    Args:
        plain_password (_type_): _description_
        hashed_password (bool): _description_
    Returns:
        _type_: _description_
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """_summary_
    Args:
        password (_type_): _description_
    Returns:
        _type_: _description_
    """
    return pwd_context.hash(password)


async def get_user(username: str):
    """_summary_
    Args:
        username (str): _description_
    Returns:
        _type_: _description_
    """
    return await UserDatabaseSchema.from_queryset_single(Users.get(username=username))


async def validate_user(user: OAuth2PasswordRequestForm = Depends()):
    """_summary_
    Args:
        user (OAuth2PasswordRequestForm, optional): _description_. Defaults to Depends().
    Raises:
        HTTPException: _description_
        HTTPException: _description_
    Returns:
        _type_: _description_
    """
    try:
        db_user = await get_user(user.username)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    return db_user
