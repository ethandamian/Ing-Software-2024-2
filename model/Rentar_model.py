from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

def obtener_rentas():
    return Rentar.query.all()

def obtener_renta_por_id(id:int):
    return Rentar.query.filter_by(idRentar=id).first()

def obtener_fecha_renta(fecha:str):
    return Rentar.query.filter_by(fecha_renta=fecha)

def actualizar_fecha_renta(fecha: str, id: int):
    renta = obtener_renta_por_id(id)
    renta.fecha_renta = fecha
    db.session.commit()
    print("Fecha de la renta actualizada con éxito!")
    print("-"*100)

def eliminar_renta_por_id(id: int):
    renta = obtener_renta_por_id(id)
    db.session.delete(renta)
    db.session.commit()
    print("Renta eliminada con éxito!")
    print("-"*100)

def borrar_tabla_rentas():
    db.session.query(Rentar).delete()
    db.session.commit()
    print("Tabla rentas borrada con éxito!")
    print("-"*100)