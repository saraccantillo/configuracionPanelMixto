from model.orm.model import Interfaz_De_Audio

class InterfazDAO:

    def __init__(self):
        self.interfazEncontrada = None
    
    def getInterfaz(self, pInterfaz):

        self.interfazEncontrada = Interfaz_De_Audio.get_by_id(pInterfaz)

        return self.interfazEncontrada