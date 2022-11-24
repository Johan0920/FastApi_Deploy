from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.studen_entity import studentEntity, studentsEntity
from models.student import Student
#from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from models.materias import Materia, MateriaAsignada
from schemas.materia_entity import materiaEntity

student = APIRouter()


@student.get('/students')#, response_model=list[Student], tags=["Estudiantes"])
def get_all_student():
    return studentsEntity(conn.TEST.Student.find())


@student.post('/students', response_model=Student, tags=["Estudiantes"])
def create_student(student: Student):
    new_student = dict(student)
    #new_student["clave"] = sha256_crypt.encrypt(new_student["clave"])
    id = conn.TEST.Student.insert_one(new_student).inserted_id
    return f"Estudiante creado {id}"


@student.get('/students/{id}', response_model=Student, tags=["Estudiantes"])
def get_student(id: str):
    return studentEntity(conn.TEST.Student.find_one({"_id": ObjectId(id)}))


@student.put('/students/{id}', response_model=Student, tags=["Estudiantes"])
def update_student(id: str, student: Student):
    conn.TEST.Student.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(student)})
    return studentEntity(conn.TEST.Student.find_one({"_id": ObjectId(id)}))


@student.delete('/students/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Estudiantes"])
def delete_student(id: str):
    studentEntity(conn.TEST.Student.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)


#----------------------
@student.post('/students/materias')#, response_model=Student, tags=["Estudiantes"])
def create_materia(mat: MateriaAsignada, idStudent:str):
    existe =studentEntity(conn.TEST.Student.find_one({"_id": ObjectId(idStudent)}))
    if bool(existe):
        new_materia = dict(mat)
        new_materia["idStudent"]=idStudent
        id = conn.TEST.materiaAsignada.insert_one(new_materia).inserted_id
        return f"Materia asignada {id}"
