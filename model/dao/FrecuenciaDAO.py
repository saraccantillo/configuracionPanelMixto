from model.orm.model import Frecuencia

class FrecuenciaDAO:

    def __init__(self):
        self.frecuenciaEncontrada = None
        
    def getFrecuencia(self, pFrecuencia):

        self.frecuenciaEncontrada = Frecuencia.get_by_id(pFrecuencia)
