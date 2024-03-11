from sqlalchemy import Column, Integer, String, Boolean
from alchemyClasses import db

class Usuarios(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200), nullable=True)
    password = Column(String(64))
    email = Column(String(200), default=None, unique=True)
    profilePicture = Column(String(200),nullable=True)
    superUser = Column(Boolean, default=None)

    def __init__(self, nombre, apPat,superUser, password, email, profilePicture = None, apMat=None ):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser
    
    def __str__(self) -> str:
        return f'Usuario: \nId: {self.idUsuario} \n{self.nombre} {self.apPat} {self.apMat} {self.password} {self.email} {self.superUser}\n'