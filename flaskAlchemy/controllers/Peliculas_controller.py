from flask import Blueprint, request, render_template, flash, url_for, redirect

from model import Peliculas_model as model

peliculas_blueprint = Blueprint('peliculas', __name__, url_prefix='/pelicula')


@peliculas_blueprint.route('/peliculas')
def ver_peliculas():
    peliculas = model.obtener_peliculas()
    return render_template('mostrar-registros-peliculas.html', peliculas=peliculas)


@peliculas_blueprint.route('/crear-pelicula', methods=['GET', 'POST'])
def crear_pelicula():
    if request.method == 'GET':
        return render_template('crear-pelicula.html')
    else:
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        model.crear_pelicula(nombre, genero, duracion, inventario)
        flash('Pelicula creada correctamente')
        return redirect(url_for('home'))

@peliculas_blueprint.route('eliminar-pelicula', methods=['GET', 'POST'])
def eliminar_pelicula():
    if request.method == 'GET':
        return render_template('solicitar-id-peliculas.html', texto1="Eliminar", texto2="eliminar")
    else:
        id = request.form['idPelicula']
        respuesta = model.eliminar_pelicula_por_id(id)
        if respuesta == -1:
            flash('Error al eliminar la pelicula- Id inexistente')
        else:
            flash('Pelicula eliminada correctamente')
        return redirect(url_for('peliculas.eliminar_pelicula'))

@peliculas_blueprint.route('/pedir-id-pelicula',methods=['GET','POST'])
def pedir_id_pelicula():
    if request.method == 'POST':
        id_pelicula = request.form.get('idPelicula')
        if id_pelicula and model.obtener_pelicula_por_id(id_pelicula) is not None:
            return redirect(url_for('peliculas.actualizar_pelicula', id_pelicula=id_pelicula))
        else:
            flash('Por favor, ingrese un ID de pelicula válido', 'error')
    return render_template('solicitar-id-peliculas.html',texto1="Buscar", texto2="actualizar")

@peliculas_blueprint.route('/actualizar-pelicula/<int:id_pelicula>', methods=['GET', 'POST'])
def actualizar_pelicula(id_pelicula):
        
    pelicula = model.obtener_pelicula_por_id(id_pelicula)
        
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        respuesta =model.actualizar_pelicula(id_pelicula, nombre, genero, duracion, inventario)
        if respuesta == -1:
            flash('Error al actualizar la pelicula')
            return redirect(url_for('peliculas.actualizar_pelicula', id_pelicula=id_pelicula))
        else:
            flash('Pelicula actualizada correctamente')
            return redirect(url_for('home'))
    
    return render_template('actualizar-pelicula.html', pelicula=pelicula)