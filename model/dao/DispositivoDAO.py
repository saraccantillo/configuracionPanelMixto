from model.orm.model import Dispositivo

class DispositivoDAO:

    def __init__(self):
        self.dispoEncontrado = None

    def getDispositivo(self, pDispositivo):

        self.dispoEncontrado = Dispositivo.get_by_id(pDispositivo)

        return self.dispoEncontrado