from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    def username_validator(cls, v):
        if len(v) < 4:
            raise ValueError("Username musr be at least 4 characters")
        return v


user = User(username="maleesha")

print(user)


class SignupData(BaseModel):
    password: str
    password_confirmation: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.password_confirmation:
            raise ValueError("Passwords do not match")
        return values
