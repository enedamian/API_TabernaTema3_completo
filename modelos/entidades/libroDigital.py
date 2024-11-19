from modelos.entidades.libro import Libro

class LibroDigital(Libro):
    @classmethod
    def fromDiccionario(cls, diccionario: dict):
        return cls(
            diccionario['ISBN'],
            diccionario['titulo'],
            diccionario['autor'],
            diccionario['editorial'],
            diccionario['precio'],
            diccionario['stock'],
            diccionario['formato'],
            diccionario['tamanioMB'],
            diccionario['proteccionDeCopia']
        )

    def __init__(self, ISBN: int, titulo: str, autor: str, editorial: str, precio: float, stock: int, formato:str, tamanioMB:float, proteccionDeCopia:bool):
        super().__init__(ISBN, titulo, autor, editorial, precio, stock)
        if not isinstance(formato, str) or formato == "" or formato.isspace():
            raise ValueError('El formato no puede estar vacío')
        if not isinstance(tamanioMB, (int,float)) or tamanioMB <= 0:
            raise ValueError('El tamaño en MB debe ser un número positivo')
        if not isinstance(proteccionDeCopia, bool):
            raise ValueError('El valor de proteccionDeCopia debe ser un booleano')
        self.__formato = formato
        self.__tamanioMB = tamanioMB
        self.__proteccionDeCopia = proteccionDeCopia

    def obtenerFormato(self):
        return self.__formato
    
    def obtenerTamanioMB(self):
        return self.__tamanioMB
    
    def obtenerProteccionDeCopia(self):
        return self.__proteccionDeCopia
    
    def establecerFormato(self, formato: str):
        if not isinstance(formato, str) or formato == "" or formato.isspace():
            raise ValueError('El formato no puede estar vacío')
        self.__formato = formato

    def establecerTamanioMB(self, tamanioMB: float):
        if not isinstance(tamanioMB, (int,float)) or tamanioMB <= 0:
            raise ValueError('El tamaño en MB debe ser un número positivo')
        self.__tamanioMB = tamanioMB

    def establecerProteccionDeCopia(self, proteccionDeCopia: bool):
        if not isinstance(proteccionDeCopia, bool):
            raise ValueError('El valor de proteccionDeCopia debe ser un booleano')
        self.__proteccionDeCopia = proteccionDeCopia

    def toDiccionario(self):
        return {
            'ISBN': self.obtenerISBN(),
            'titulo': self.obtenerTitulo(),
            'autor': self.obtenerAutor(),
            'editorial': self.obtenerEditorial(),
            'precio': self.obtenerPrecio(),
            'stock': self.obtenerStock(),
            'formato': self.obtenerFormato(),
            'tamanioMB': self.obtenerTamanioMB(),
            'proteccionDeCopia': self.obtenerProteccionDeCopia()
        }
