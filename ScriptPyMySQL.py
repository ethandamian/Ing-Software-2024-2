import Conection as connection
from datetime import date


def verificar_si_existe_email(email: str):
    con = connection.establecer_conexion()
    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(sql, email)
            return cursor.fetchone() is not None

        
def verificar_si_existe_pelicula(nombre: str):
    con = connection.establecer_conexion()
    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql, nombre)
            return cursor.fetchone() is not None
 

def verificar_si_usuario_rento_pelicula(idUsuario: int, idPelicula: int):
    con = connection.establecer_conexion()
    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM rentar WHERE idUsuario = %s AND idPelicula = %s"
            cursor.execute(sql, (idUsuario,idPelicula))
            return cursor.fetchone() is not None
    

def obtener_id_usuario_por_email(email_usuario: str):
    con = connection.establecer_conexion()
    
    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(sql,email_usuario)
            result = cursor.fetchone()

            if result:
                return result['idUsuario']
            else:
                return None
           

def obtener_id_pelicula_por_nombre(nombre_pelicula: str):
    con = connection.establecer_conexion()
    
    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql,nombre_pelicula)
            result = cursor.fetchone()

            if result:
                return result['idPelicula']
            else:
                return None
    

def insertar_en_usuarios(nombre: str, apPat:str,apMat:str, password: str, email: str):
    con = connection.establecer_conexion()
    
    with con:
        with con.cursor() as cursor:
            # Verificar si el email ya existe
            if verificar_si_existe_email(email):
                return "El email ya existe"
            else: 
                sql = "INSERT INTO usuarios (nombre, apPat,apMat,password,email) VALUES (%s,%s,%s, %s,%s)"
                cursor.execute(sql, (nombre,apPat,apMat, password, email))
                con.commit()
                return "Usuario registrado con éxito"
                

def insertar_en_peliculas(nombre: str,genero: str, duracion: int,inventario: int):
    con = connection.establecer_conexion()

    with con:
        with con.cursor() as cursor:
            if verificar_si_existe_pelicula(nombre):
                return "La pelicula con este nombre ya esta registrada, intente de nuevo"
            else:
                sql = "INSERT INTO peliculas (nombre,genero,duracion,inventario) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql,(nombre,genero,duracion,inventario))
                con.commit()
                return "Pelicula registrada con éxito"
                


def insertar_en_rentar(idUsuario: int,idPelicula: int, fecha_renta: date, dias_de_renta: int=5,estatus:int = 0):
    con = connection.establecer_conexion()
    
    with con:
        with con.cursor() as cursor:
            if verificar_si_usuario_rento_pelicula(idUsuario,idPelicula):
                return f"El usuario con id {idUsuario} ya tiene en renta la pelicula con id {idPelicula}"
            else:
                sql = "INSERT INTO rentar (idUsuario,idPelicula,fecha_renta,dias_de_renta,estatus) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql,(idUsuario,idPelicula,fecha_renta,dias_de_renta,estatus))
                con.commit()
                return "Pelicula rentada con éxito"
               
def insertar_en_todas_las_tablas(usuario: dict, pelicula: dict, rentar: dict):
    print("\033[33mINSERTAR UN USUARIO EN LA TABLA USUARIOS\033[0m")
    print("Insertando usuario ",usuario)
    print(insertar_en_usuarios(usuario['nombre'],usuario['apPat'],usuario['apMat'],usuario['password'],usuario['email']))
    print("-"*100)

    print("\033[33mINSERTAR UNA PELICULA EN LA TABLA PELICULAS\033[0m")
    print("Insertando pelicula ",pelicula)
    print(insertar_en_peliculas(pelicula['nombre'],pelicula['genero'],pelicula['duracion'],pelicula['inventario']))
    print("-"*100)

    print("\033[33mINSERTAR RENTA EN LA TABLA RENTAR\033[0m")
    idUsuario = obtener_id_usuario_por_email(usuario['email'])
    idPelicula = obtener_id_pelicula_por_nombre(pelicula['nombre'])
    print(f"Insertando renta {renta} con id de usuario {idUsuario} y id de pelicula {idPelicula}")
    print(insertar_en_rentar(idUsuario,idPelicula,renta['fecha_renta'],renta['dias_de_renta'],renta['estatus']))
    print("-"*100)


def filtar_usuario_por_apellido(terminacion_apellido:str):
    con = connection.establecer_conexion()
    with con:
        with con.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s AND apMat LIKE %s"
            cursor.execute(sql, (f'%{terminacion_apellido}',f'%{terminacion_apellido}'))
            return cursor.fetchall()

def cambiar_genero_pelicula(nombre_pelicula: str, genero: str):
    con = connection.establecer_conexion()
    with con:
        with con.cursor() as cursor:
            # verificar si existe la pelicula
            if not verificar_si_existe_pelicula(nombre_pelicula):
                return f"No existe la pelicula {nombre_pelicula}"
            else:
                sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql,(genero,nombre_pelicula))
                con.commit()
                return f"Genero de la pelicula {nombre_pelicula} cambiado a {genero}"

def eliminar_rentas_anteriores_a_tres_dias():
    con = connection.establecer_conexion()
    with con:
        with con.cursor() as cursor:
            sql = "DELETE FROM rentar WHERE fecha_renta < DATE_SUB(NOW(), INTERVAL 3 DAY)"
            cursor.execute(sql)
            con.commit()
            return "Rentas eliminadas con éxito"

if __name__ == "__main__":
    
    usuario = {'nombre': 'Ethan Damian', 'apPat': 'Sanchez','apMat': 'Salmeron', 'password': 'Ethan1234', 'email': 'ethand.san@gmail.com'}
    pelicula = {'nombre': 'Duro de Matar', 'genero': 'Accion', 'duracion': 131,'inventario': 3}
    renta = {'fecha_renta': date.today(), 'dias_de_renta': 5, 'estatus': 0}
    
    # insertar_en_todas_las_tablas(usuario, pelicula, renta)

    print(filtar_usuario_por_apellido('s'))

    # print(cambiar_genero_pelicula('Duro de Matar', 'Accion y suspenso'))

    # print(eliminar_rentas_anteriores_a_tres_dias())

