from flask import Flask
from model import Usuarios_model
from model import Peliculas_model
from model import Rentar_model
from MenuFlask import menu
from alchemyClasses import db
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        menu()
        

                