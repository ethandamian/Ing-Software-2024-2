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
            return redirect(url_for('rentas.crear_renta'))
        else:
            flash('Renta creada correctamente')
            return redirect(url_for('home'))


    
@rentas_blueprint.route('/pedir-id-renta',methods=['GET','POST'])
def pedir_id_renta():
    if request.method == 'POST':
        id_renta = request.form.get('idRenta')
        if id_renta and model.obtener_renta_por_id(id_renta) is not None:
            return redirect(url_for('rentas.actualizar_renta', id_renta=id_renta))
        else:
            flash('Por favor, ingrese un ID de renta válido', 'error')
    return render_template('solicitar-id-renta.html',texto1="Buscar", texto2="actualizar")

@rentas_blueprint.route('/actualizar-renta/<int:id_renta>', methods=['GET', 'POST'])
def actualizar_renta(id_renta):
    renta = model.obtener_renta_por_id(id_renta)
    if request.method == 'POST':
        id_de_renta = id_renta
        eleccion = request.form['eleccion']
        estatus = None
        if eleccion == 1:
            estatus = 1
        elif eleccion == 2:
            estatus = 0
        model.actualizar_estatus_renta(id_renta,estatus)
        flash('Renta actualizada correctamente')
        return redirect(url_for('home'))
    return render_template('actualizar-renta.html', renta=renta)