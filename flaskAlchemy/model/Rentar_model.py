from alchemyClasses.Rentar import Rentar
from alchemyClasses import db


def crear_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
    try:
        nueva_renta = Rentar(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
        db.session.add(nueva_renta)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al crear la renta:", e)
        return -1

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
 

def eliminar_renta_por_id(id: int):
    renta = obtener_renta_por_id(id)
    try:
        db.session.delete(renta)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al eliminar la renta:", e)
        return -1

def borrar_tabla_rentas():
    db.session.query(Rentar).delete()
    db.session.commit()
