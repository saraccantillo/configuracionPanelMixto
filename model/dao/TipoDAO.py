from model.orm.model import Tipo

class TipoDAO:

    def __init__(self):
        self.tipoEncontrado = None
        self.todosLosTipos= []

    def getTipo(self, pTipo):

        self.tipoEncontrado = Tipo.get_by_id(pTipo)

        return self.tipoEncontrado