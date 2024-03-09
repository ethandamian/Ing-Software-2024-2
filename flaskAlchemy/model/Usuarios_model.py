from alchemyClasses.Usuarios import Usuarios
from alchemyClasses import db 

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
    print("Nombre del Usuario actualizado con éxito!")
    print("-"*100)


def eliminar_usuario_por_id(id: int):
    usuario = obtener_usuario_por_id(id)
    db.session.delete(usuario)
    db.session.commit()
    print("Usuario eliminado con éxito!")
    print("-"*100)


def borrar_tabla_usuarios():
    db.session.query(Usuarios).delete()
    db.session.commit()
    print("Tabla usuarios borrada con éxito!")
    print("-"*100)


