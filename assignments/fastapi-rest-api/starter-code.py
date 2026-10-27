from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="School Library API")


class BookInput(BaseModel):
    title: str
    author: str
    publication_year: int = Field(ge=1450, le=2100)


books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "publication_year": 1937,
    },
    {
        "id": 2,
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "publication_year": 1962,
    },
]