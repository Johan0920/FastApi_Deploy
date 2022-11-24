from fastapi import FastAPI
from routes.student_route import student
from routes.materias_route import materia
from docs import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    title="REST API con FastAPI y MongoDB en la UTB",
    description="Este es una PAI de estudiantes en el programa de MISIONTIC 2022",
    version="0.0.1",
    openapi_tags=tags_metadata
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student)
app.include_router(materia)


