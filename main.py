from optparse import Option
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List



app = FastAPI(
    title="FastAPI LMS App",
    description="Project created to practice this framework.",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Luis Fernando Camacho",
        "url": "https://creatos.dev",
        "email": "luisf@creatos.dev",
    },
    license_info={
        "name": "MIT"
    },
    )


users = []

class User(BaseModel):
    email: str
    is_active: str
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User Created Successfuly"}


@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve.", gt=1),
    q: str = Query(None, max_length=5)
    ):
    return { "user": users[id], "query": q}



