from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=3)
    # id: int = Field(le=2) # le - Less equal
    title: str
    # name: str = Field(alias="_name")  # Для примера

    # @validator("id")  # Используем валидатор или Field(le=3)
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 3:
    #         raise ValueError('Id is not less than two.')
    #     else:
    #         return v
