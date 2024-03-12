from alchemyClasses.Usuarios import Usuarios
from alchemyClasses import db 


def crear_usuario(nombre, apPat, password, apMat=None, email=None, profilePicture=None, superUser=None):
    nuevo_usuario = Usuarios(nombre, apPat, bool(superUser), password, email, profilePicture, apMat)
    print(nuevo_usuario)
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al crear el usuario:", e)
        return -1



def obtener_usuarios():
    return Usuarios.query.all()


def obtener_usuario_por_id(id:int):
    return Usuarios.query.filter_by(idUsuario=id).first()

def obtener_usuario_por_nombre(nombre:str):
    return Usuarios.query.filter_by(nombre=nombre)

def actualizar_nombre_usuario(nombre: str, id: int):
    usuario = obtener_usuario_por_id(id)
    usuario.nombre = nombre
    db.session.commit()

def actualizar_usuario(id,nombre, apPat, password, email,apMat=None, superUser=None,profilePicture=None):
    usuario = obtener_usuario_por_id(id)
    usuario.nombre = nombre
    usuario.apPat = apPat
    usuario.password = password
    usuario.apMat = apMat
    usuario.email = email
    usuario.profilePicture = profilePicture
    usuario.superUser = superUser
    db.session.commit()


def eliminar_usuario_por_id(id: int):
    usuario = obtener_usuario_por_id(id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al eliminar el usuario:", e)
        return -1


def borrar_tabla_usuarios():
    db.session.query(Usuarios).delete()
    db.session.commit()



