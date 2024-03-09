from alchemyClasses.Peliculas import Peliculas
from alchemyClasses import db 

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
    print("Nombre de la Película actualizado con éxito!")
    print("-"*100)

def eliminar_pelicula_por_id(id: int):
    pelicula = obtener_pelicula_por_id(id)
    db.session.delete(pelicula)
    db.session.commit()
    print("Película eliminada con éxito!")
    print("-"*100)

def borrar_tabla_peliculas():
    db.session.query(Peliculas).delete()
    db.session.commit()
    print("Tabla películas borrada con éxito!")
    print("-"*100)
