from flask import Blueprint, request, render_template, flash, url_for, redirect

from model import Usuarios_model as model

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')


@usuario_blueprint.route('/usuarios')
def ver_usuarios():
    usuarios = model.obtener_usuarios()
    return render_template('mostrar-registros-usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/crear-usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'GET':
        return render_template('crear-usuario.html')
    else:
        nombre = request.form['nombre']
        print(nombre)
        apPat = request.form['apPat']
        print(apPat)
        apMat = request.form['apMat']
        print(apMat)
        password = request.form['password']
        print(password)
        email = request.form['email']
        print(email)
        super_user = 0
        if 'superUser' in request.form:
            super_user = '1'
        print(super_user)
        model.crear_usuario(nombre, apPat, password, apMat, email, None, super_user)
        flash('Usuario creado correctamente')
        return redirect(url_for('usuario.crear_usuario'))

@usuario_blueprint.route('/eliminar-usuario',methods=['GET','POST'])
def eliminar_usuario():
    if request.method == 'GET':
        return render_template('solicitar-id-usuario.html',texto1="Eliminar", texto2="eliminar")
    else:
        id = request.form['idUsuario']
        respuesta = model.eliminar_usuario_por_id(id)
        if respuesta == -1:
            flash('Error al eliminar el usuario')
        else:
            flash('Usuario eliminado correctamente')
        return redirect(url_for('usuario.eliminar_usuario'))