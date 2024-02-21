import pymysql.cursors

def establecer_conexion():
    conexion = pymysql.connect(
        host='localhost',
        user = 'lab',
        password = 'Developer123!',
        database = 'lab_ing_software',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return conexion

