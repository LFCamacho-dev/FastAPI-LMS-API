from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

from api import users, courses, sections

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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)





