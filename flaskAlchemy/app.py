from flask import Flask, render_template, redirect, url_for
from datetime import date


from alchemyClasses import db
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar

from controllers.Usuarios_controller import usuario_blueprint
from controllers.Peliculas_controller import peliculas_blueprint
from controllers.Rentas_controller import rentas_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)

db.init_app(app)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(peliculas_blueprint)
app.register_blueprint(rentas_blueprint)

@app.context_processor
def inject_datetime():
    return {'date': date}


@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():  # put application's code here
    return render_template('index.html')   

if __name__ == '__main__':
    app.run()

        