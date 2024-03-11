from alchemyClasses.Peliculas import Peliculas
from alchemyClasses import db 


def crear_pelicula(nombre, genero=None, duracion=None, inventario=1):
    nueva_pelicula = Peliculas(nombre, genero, duracion, inventario)
    db.session.add(nueva_pelicula) 
    db.session.commit()

def obtener_peliculas():
    return Peliculas.query.all()

def obtener_pelicula_por_id(id:int):
    return Peliculas.query.filter_by(idPelicula=id).first()

def obtener_pelicula_por_nombre(nombre:str):
    return Peliculas.query.filter_by(nombre=nombre)

def actualizar_nombre_pelicula(nombre: str, id: int):
    pelicula = obtener_pelicula_por_id(id)
    pelicula.nombre = nombre
    db.session.commit()

def eliminar_pelicula_por_id(id: int):
    pelicula = obtener_pelicula_por_id(id)
    try:
        db.session.delete(pelicula)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al eliminar la pelicula:", e)
        return -1


def borrar_tabla_peliculas():
    db.session.query(Peliculas).delete()
    db.session.commit()
