from model import Usuarios_model as model

nombre = 'Ethan'
apPat = 'Hunt'
password = '1234'
apMat = 'StopIteration'
email = 'hola.com'

model.crear_usuario(nombre, apPat, password, apMat=None, email=None, profilePicture=None, superUser=0)