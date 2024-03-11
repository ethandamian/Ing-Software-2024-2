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
        return redirect(url_for('peliculas.crear_pelicula'))

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