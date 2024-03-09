from flask import Flask, render_template

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

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')   

if __name__ == '__main__':
    app.run()

        