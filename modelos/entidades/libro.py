from abc import ABC, abstractmethod

class Libro(ABC):
    def __init__(self, ISBN: int, titulo: str, autor: str, editorial: str, precio: float, stock: int):
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError('El ISBN debe ser un entero positivo')
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError('El título no puede estar vacío')
        if not isinstance(autor, str) or autor == "" or autor.isspace():
            raise ValueError('El autor no puede estar vacío')
        if not isinstance(editorial, str) or editorial == "" or editorial.isspace():
            raise ValueError('La editorial no puede estar vacía')
        if not isinstance(precio, (int,float)) or precio < 0:
            raise ValueError('El precio debe ser un número positivo')
        if not isinstance(stock, int) or stock < 0:
            raise ValueError('El stock debe ser un entero positivo')
        self.__ISBN = ISBN
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__precio = precio
        self.__stock = stock


    def obtenerISBN(self):
        return self.__ISBN
    
    def obtenerTitulo(self):
        return self.__titulo
    
    def obtenerAutor(self):
        return self.__autor
    
    def obtenerEditorial(self):
        return self.__editorial
    
    def obtenerPrecio(self):
        return self.__precio
    
    def obtenerStock(self):
        return self.__stock
    
    def establecerTitulo(self, titulo: str):
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError('El título no puede estar vacío')
        self.__titulo = titulo

    def establecerAutor(self, autor: str):
        if not isinstance(autor, str) or autor == "" or autor.isspace():
            raise ValueError('El autor no puede estar vacío')
        self.__autor = autor

    def establecerEditorial(self, editorial: str):
        if not isinstance(editorial, str) or editorial == "" or editorial.isspace():
            raise ValueError('La editorial no puede estar vacía')
        self.__editorial = editorial

    def establecerPrecio(self, precio: float):
        if not isinstance(precio, (int,float)) or precio < 0:
            raise ValueError('El precio debe ser un número positivo')
        self.__precio = precio

    def establecerStock(self, stock: int):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError('El stock debe ser un entero positivo')
        self.__stock = stock
    
    def actualizarStock(self, cantidad: int):
        if not isinstance(cantidad, int):
            raise ValueError('La cantidad debe ser un entero')
        self.__stock += cantidad

            