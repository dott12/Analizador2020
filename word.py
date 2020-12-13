from ply import lex
# JK: Nueva Clase que manejara los tokens y lexemas de cada palabra
# TODO: Encontrar una buena manera de retornar objetos del tipo TOKEN utilizando la libreria lex.

class Word:
    def __init__(self, lexema, token):
        self.lexema = lexema
        self.token = token

