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
        return redirect(url_for('home'))

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
    
@usuario_blueprint.route('/pedir-id-usuario',methods=['GET','POST'])
def pedir_id_usuario():
    if request.method == 'POST':
        id_usuario = request.form.get('idUsuario')
        if id_usuario and model.obtener_usuario_por_id(id_usuario) is not None:
            # Redirigir a la vista para actualizar el usuario con el ID proporcionado
            return redirect(url_for('usuario.actualizar_usuario', id_usuario=id_usuario))
        else:
            flash('Por favor, ingrese un ID de usuario válido', 'error')
    return render_template('solicitar-id-usuario.html',texto1="Buscar", texto2="actualizar")


@usuario_blueprint.route('/actualizar-usuario/<int:id_usuario>',methods=['GET','POST'])
def actualizar_usuario(id_usuario):
    usuario = model.obtener_usuario_por_id(id_usuario)
    if request.method == 'POST':
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
            super_user = 1
        respuesta = model.actualizar_usuario(id_usuario,nombre,apPat,password,email,apMat,super_user,profilePicture=None)
        if respuesta == -1:
            flash('Error al actualizar el usuario')
            return redirect(url_for('usuario.actualizar_usuario', id_usuario=id_usuario))
        else:
            flash('Usuario actualizado correctamente')
            return redirect(url_for('home'))
    return render_template('actualizar-usuario.html',usuario=usuario)