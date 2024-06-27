from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, status, Request, Depends
from jose import jwt, JWTError
from passlib.context import CryptContext

from config import settings
from .crud import UserCRUDModel
from .schemas import UserCreateSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user_by_email(email):
    user = await UserCRUDModel.get_user_by_email(email=email)
    return user


async def register_user(user: UserCreateSchema):
    user_in_db = await UserCRUDModel.get_user_by_email(email=user.email)
    if user_in_db:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    user = await UserCRUDModel.create_user(
        email=user.email,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        is_admin=user.is_admin
    )
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def login_user(email, password):
    user_in_db = await UserCRUDModel.get_user_by_email(email=email)

    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not registered")
    if not verify_password(password, user_in_db.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

    return create_access_token(data={"sub": str(user_in_db.pk)})


def get_token(request: Request):
    token = request.cookies.get(settings.ACCESS_TOKEN_COOKIE_NAME)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found")
    return token


async def get_user_by_token(token=Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    exp = payload.get("exp")
    if exp is None or exp < datetime.now(timezone.utc).timestamp():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    pk = payload.get("sub")
    if pk is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Primary key not found")

    user = await UserCRUDModel.find_by(pk=int(pk))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user
