from fastapi import FastAPI
from routes.student_route import student
from routes.materias_route import materia
from docs import tags_metadata

app=FastAPI(
    title="REST API con FastAPI y MongoDB en la UTB",
    description="Este es una PAI de estudiantes en el programa de MISIONTIC 2022",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(student)
app.include_router(materia)


