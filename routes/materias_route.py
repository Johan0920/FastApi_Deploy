from fastapi import APIRouter
from schemas.materia_entity import materiaEntity, materiasEntity
from models.materias import Materia
from config.db import conn

materia = APIRouter()

@materia.get('/materias')#, response_model=list[Materia], tags=["Materias"])
def get_all_materias():
    return materiasEntity(conn.TEST.materias.find())