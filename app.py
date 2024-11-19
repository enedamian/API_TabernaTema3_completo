from flask import Flask
from rutas.rutas_libros import bp_libros

app = Flask(__name__)

app.register_blueprint(bp_libros)

if __name__ == '__main__':
    app.run(debug=True)