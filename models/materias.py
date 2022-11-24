from pydantic import BaseModel

class Materia(BaseModel):
    nombreMateria:str
    descripcion:str
    
class MateriaAsignada(BaseModel):
    nombreMateria:str
    idMateria:str
    #idStudent:str