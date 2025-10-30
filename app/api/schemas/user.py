from pydantic import BaseModel, EmailStr, SecretStr, field_validator, model_validator


class UserCreate(BaseModel):
    email: str
    password: SecretStr
    confirm_password: SecretStr

    @field_validator('email')
    def email_validator(value):
        if '@' not in value:
            raise ValueError('Ошибка в оформлении Email')
        return value
    
    @model_validator(mode='after')
    def validate_password(self):
        if self.password != self.confirm_password:
            raise ValueError('Пароли не совпадают!')
        return self
    

class UserRead(BaseModel):
    id: int
    email: str