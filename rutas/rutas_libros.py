from flask import Blueprint, jsonify, request
from modelos.entidades.libroDigital import LibroDigital
from modelos.entidades.libroFisico import LibroFisico
from modelos.repositorios.repositorios import obtenerRepoLibros

repo_libros = obtenerRepoLibros()

bp_libros = Blueprint('bp_libros', __name__)

@bp_libros.route('/libros', methods=['GET'])
def obtener_libros():
    libros = repo_libros.obtenerLibros()
    lista_libros = []
    for libro in libros:
        lista_libros.append(libro.toDiccionario())
    return jsonify(lista_libros), 200

@bp_libros.route('/libros/<int:ISBN>', methods=['GET'])
def obtener_libro(ISBN):
    libro = repo_libros.obtenerLibroPorISBN(ISBN)
    if libro == None:
        return jsonify({'mensaje': 'Libro no encontrado'}), 404
    return jsonify(libro.toDiccionario()), 200

@bp_libros.route('/libros', methods=['POST'])
def agregar_libro():
    if request.is_json:
        datos = request.json
        try:
            if repo_libros.existeLibro(datos['ISBN']):
                respuesta= {'mensaje': 'El libro ya existe'}
                codigoRespuesta = 400
            if 'formato' in datos:
                libro = LibroDigital.fromDiccionario(datos)
                tipo = "digital"
            else:
                libro = LibroFisico.fromDiccionario(datos)
                tipo = "fisico"            
            if repo_libros.agregarLibro(libro):
                respuesta = {"Mensaje":f"Libro ({tipo}) agregado con éxito.","libro":libro.toDiccionario()}
                codigoRespuesta = 201
        except Exception as e:
            respuesta = {'mensaje': str(e)}
            codigoRespuesta = 400
    else:
        respuesta = {'mensaje': 'El formato de los datos debe ser JSON'}
        codigoRespuesta = 400
    
    return jsonify(respuesta), codigoRespuesta

@bp_libros.route('/libros/<int:ISBN>', methods=['PUT'])
def actualizar_libro(ISBN):
    if request.is_json:
        datos = request.json
        try:
            if 'formato' in datos:
                libro = LibroDigital.fromDiccionario(datos)
                tipo = "digital"
            else:
                libro = LibroFisico.fromDiccionario(datos)
                tipo = "fisico"            
            if not repo_libros.existeLibro(ISBN):
                respuesta = {'mensaje': 'Libro no encontrado'}
                codigoRespuesta = 404
            else:                
                repo_libros.modificarLibro(ISBN, libro)
                respuesta = {"Mensaje":f"Libro ({tipo}) actualizado con éxito.","libro":libro.toDiccionario()}
                codigoRespuesta = 200
        except Exception as e:
            respuesta = {'mensaje': str(e)}
            codigoRespuesta = 400
    else:
        respuesta = {'mensaje': 'El formato de los datos debe ser JSON'}
        codigoRespuesta = 400
    
    return jsonify(respuesta), codigoRespuesta

@bp_libros.route('/libros/<int:ISBN>', methods=['DELETE'])
def eliminar_libro(ISBN):
    if repo_libros.eliminarLibro(ISBN):
        return jsonify({'mensaje': 'Libro eliminado'}), 200
    return jsonify({'mensaje': 'Libro no encontrado'}), 404