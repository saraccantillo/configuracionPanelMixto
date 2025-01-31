from model.orm.model import Config_Canal_Fuente

class CanalDAO:

    def __init__(self):
        self.fuenteConfigurada = None
        
    def getConfiguracionFuente(self, pCanal):

        self.fuenteConfigurada = (
            Config_Canal_Fuente
            .select(Config_Canal_Fuente.id_canal, Config_Canal_Fuente.id_fuente)
            .where(Config_Canal_Fuente.id_canal == pCanal)
            .get()
        )

        return self.fuenteConfigurada
        

    def cambiarFuente(self, pFuente, pCanal):

        query = (
                Config_Canal_Fuente
                .update({Config_Canal_Fuente.id_fuente : pFuente})
                .where(Config_Canal_Fuente.id_canal == pCanal)
                )
        query.execute()

    def getConfiguracionVolumen(self, pCanal):

        queryVolumen = (
        Config_Canal_Fuente
        .select(Config_Canal_Fuente.volumen)
        .where(Config_Canal_Fuente.id_canal == pCanal)
        .get()
        )

        return queryVolumen.volumen

    def cambiarVolumen(self, pVolumen, pCanal):

        query = (
            Config_Canal_Fuente
            .update({Config_Canal_Fuente.volumen : pVolumen})
            .where(Config_Canal_Fuente.id_canal == pCanal)
        )
        query.execute()

    def getConfiguracionSolo(self, pCanal):

        querySolo = (
        Config_Canal_Fuente
        .select(Config_Canal_Fuente.solo)
        .where(Config_Canal_Fuente.id_canal == pCanal)
        .get()
        )

        return querySolo.solo

    def cambiarSolo(self, pSolo, pCanal):

        query = (
            Config_Canal_Fuente
            .update({Config_Canal_Fuente.solo : pSolo})
            .where(Config_Canal_Fuente.id_canal == pCanal)
        )
        query.execute()
        
    
    def getConfiguracionMute(self, pCanal):

        queryMute = (
        Config_Canal_Fuente
        .select(Config_Canal_Fuente.mute)
        .where(Config_Canal_Fuente.id_canal == pCanal)
        .get()
        )

        return queryMute.mute

    def cambiarMute(self, pMute, pCanal):

        query = (
            Config_Canal_Fuente
            .update({Config_Canal_Fuente.mute : pMute})
            .where(Config_Canal_Fuente.id_canal == pCanal)
        )
        query.execute()

    def getConfiguracionLink(self, pCanal):

        queryLink = (
        Config_Canal_Fuente
        .select(Config_Canal_Fuente.link)
        .where(Config_Canal_Fuente.id_canal == pCanal)
        .get()
        )

        return queryLink.link
        
    def cambiarLink(self, pLink, pCanal):

        query = (
            Config_Canal_Fuente
            .update({Config_Canal_Fuente.link : pLink})
            .where(Config_Canal_Fuente.id_canal == pCanal)
        )
        query.execute()