from model.orm.model import Entrada

class EntradaDAO:

    def __init__(self):
        self.entradaEncontrada = None

    def getEntrada(self, pEntrada):

        self.entradaEncontrada = Entrada.get_by_id(pEntrada)

        return self.entradaEncontrada