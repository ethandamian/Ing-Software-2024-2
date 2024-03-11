from sqlalchemy import Column, Integer, String, Boolean
from alchemyClasses import db


class Peliculas(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    genero = Column(String(200),default=None)
    duracion = Column(Integer,default=None)
    inventario = Column(Integer,default=1)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self) -> str:
        return f'Pelicula: \nId: {self.idPelicula} \n{self.nombre}\n'