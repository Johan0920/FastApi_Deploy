def materiaEntity(entity) -> dict:
    return {
        "id":str(entity["_id"]),
        "nombreMateria":entity["nombreMateria"],
        "descripcion":entity["descripcion"],
    }
    
def materiasEntity(entity) -> list: 
    return [materiaEntity(item) for item in entity]