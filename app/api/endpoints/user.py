from fastapi import APIRouter

from app.api.schemas.user import UserCreate, UserRead

router = APIRouter()

USER_ID = 3

FAKE_DB = [
    {
        "id": 1,
        "email": "st@ring",
        "password": "**********",
        "confirm_password": "**********"
    },
    {
        "id": 2,
        "email": "st@ring",
        "password": "**********",
        "confirm_password": "**********"
    }
]

@router.post('/', response_model=UserRead)
async def create_user(new_user: UserCreate):
    global USER_ID
    user_data = new_user.model_dump()
    user_data['id'] = USER_ID
    USER_ID += 1
    FAKE_DB.append(user_data)
    return user_data

@router.get('/', response_model=list[UserRead])
async def get_users():
    return FAKE_DB
