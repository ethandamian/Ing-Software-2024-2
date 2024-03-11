from datetime import date
from flask import Blueprint, request, render_template, flash, url_for,redirect

from model import Rentar_model as model

rentas_blueprint = Blueprint('rentas', __name__, url_prefix='/renta')


@rentas_blueprint.route('/rentas')
def ver_rentas():
    rentas = model.obtener_rentas()
    return render_template('mostrar-registros-rentas.html', rentas=rentas)

@rentas_blueprint.route('/crear-renta', methods=['GET', 'POST'])
def crear_renta():
    if request.method == 'GET':
        return render_template('crear-renta.html')
    else:
        idUsuario = request.form['idUsuario']
        idPelicula = request.form['idPelicula']
        fechaRenta = request.form['fecha_renta']
        print(fechaRenta)
        dias_renta = request.form['dias_renta']
        if dias_renta == '':
            dias_renta = 5
        estatus = 0
        if 'estatus' in request.form:
            estatus = 1

        respuesta = model.crear_renta(idUsuario, idPelicula, fechaRenta, dias_renta,estatus)
        if respuesta == -1:
            flash('Error al crear la renta - Verifique que el id de usuario y pelicula existan')
        else:
            flash('Renta creada correctamente')
        return redirect(url_for('rentas.crear_renta'))