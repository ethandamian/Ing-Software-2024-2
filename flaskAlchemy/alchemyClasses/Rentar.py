from sqlalchemy import Column, Integer, DateTime, ForeignKey
from alchemyClasses import db

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer,default=5)
    estatus = Column(Integer,default=1)

    def __init__(self, idUsuario, idPelicula, fechaRenta, dias_de_renta,estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fechaRenta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus 

    def __str__(self) -> str:
        return f'Renta: \nId: {self.idRentar} \nIdUsuario: {self.idUsuario} \nIdPelicula: {self.idPelicula}\nDias De renta: {self.dias_de_renta}\n'