from modelos.repositorios.repositorio_Libros import RepositorioLibros

repo_libros=None

def obtenerRepoLibros():
    global repo_libros
    if repo_libros==None:
        repo_libros=RepositorioLibros()
    return repo_libros