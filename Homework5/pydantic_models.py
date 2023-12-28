from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str
    author: str
    price: float
    description: str | None = None
