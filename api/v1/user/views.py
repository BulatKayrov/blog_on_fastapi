from fastapi import APIRouter, Depends, Response, status, HTTPException

from config import settings
from .crud import UserCRUDModel
from .schemas import UserCreateSchema, UserResponseSchema, UserLoginSchema
from .utils import register_user, login_user, get_user_by_token

router = APIRouter(prefix="/api/v1/user", tags=['User'])


@router.get("/all")
async def get_all_users(user=Depends(get_user_by_token)):
    if user.is_admin:
        return await UserCRUDModel.find_all()
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post('/sing-up', response_model=UserResponseSchema)
async def sing_up_user(user: UserCreateSchema):
    res = await register_user(user=user)
    return res


@router.post('/sing-in')
async def login(response: Response, user: UserLoginSchema):
    token = await login_user(password=user.password, email=user.email)
    response.set_cookie(key=settings.ACCESS_TOKEN_COOKIE_NAME, value=token, httponly=True)
    return {'status': 200}


@router.get('/logout')
async def logout(response: Response):
    response.delete_cookie(key=settings.ACCESS_TOKEN_COOKIE_NAME)
    return {'status': 200}

# from fastapi.security import HTTPBasic, HTTPBasicCredentials
#
# security = HTTPBasic()
#
#
# @router.get('/register_v2')
# async def register_user(user: HTTPBasicCredentials = Depends(security)):
#     return {'username': user.username, 'password': user.password}
