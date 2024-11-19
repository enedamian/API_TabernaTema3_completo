from modelos.entidades.libroDigital import LibroDigital
from modelos.entidades.libroFisico import LibroFisico
from modelos.entidades.libro import Libro
import json

class RepositorioLibros:
    __ruta_archivo = "datos/libros.json"

    def __init__(self):
        self.__libros = []
        self.__cargarLibros()

    def __cargarLibros(self):
        try:
            with open(RepositorioLibros.__ruta_archivo, 'r') as archivo:
                diccionario = json.load(archivo)
                for libro in diccionario:
                    if "formato" in libro:
                        self.__libros.append(LibroDigital.fromDiccionario(libro))
                    else:
                        self.__libros.append(LibroFisico.fromDiccionario(libro))
        except FileNotFoundError:
            print("No se encontró el archivo de libros")
        except Exception as e:
            print("Error cargando los libros del archivo.\n" + str(e))

    def __guardarLibros(self):
        try:
            with open(RepositorioLibros.__ruta_archivo, 'w') as archivo:
                lista_dicc = []
                for libro in self.__libros:
                    lista_dicc.append(libro.toDiccionario())
                json.dump(lista_dicc, archivo, indent=4)
        except Exception as e:
            print("Error guardando los libros en el archivo.\n" + str(e))

    def obtenerLibros(self):
        return self.__libros
    
    def obtenerLibroPorISBN(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                return libro
        return None
    
    def existeLibro(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        return self.obtenerLibroPorISBN(ISBN) != None
    
    def agregarLibro(self, libro:Libro):
        if not isinstance(libro, Libro):
            raise ValueError('El libro debe ser una instancia de la clase Libro')
        if not self.existeLibro(libro.obtenerISBN()):
            self.__libros.append(libro)
            self.__guardarLibros()
            return True
        return False
    
    def eliminarLibro(self, ISBN: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                self.__libros.remove(libro)
                self.__guardarLibros()
                return True
        return False
    
    def modificarLibro(self, ISBN: int, libro:Libro):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        if not isinstance(libro, Libro):
            raise ValueError('El libro debe ser una instancia de la clase Libro')
        for i in range(len(self.__libros)):
            if self.__libros[i].obtenerISBN() == ISBN:
                self.__libros[i] = libro
                self.__guardarLibros()
                return True
        return False
    
    