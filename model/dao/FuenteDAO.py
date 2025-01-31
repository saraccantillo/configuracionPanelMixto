from model.dao.TipoDAO import TipoDAO
from model.orm.model import Fuente

class FuenteDAO:

    def __init__(self):
        self.fuenteEncontrada = None
        self.fuentesIns = []
    
    def getFuente(self, pFuente):

        self.fuenteEncontrada = Fuente.get_by_id(pFuente)

    def getFuentesIns(self, pTipo):

        self.fuentesIns = (
            Fuente
            .select(Fuente.etiqueta, Fuente.id_fuente )
            .where(Fuente.id_tipo == pTipo)
        )


        
        
    
    