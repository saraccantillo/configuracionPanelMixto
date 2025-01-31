from model.orm.model import Configuracion
from model.orm.model import Frecuencia
from model.orm.model import Interfaz_Frecuencia
from model.orm.model import Canal
from model.orm.model import Interfaz_De_Audio
from model.orm.model import Entrada
from model.orm.model import Interfaz_Entrada
from model.orm.model import UsuarioFrecuenciaInterfazConfig

class ConfiguracionDAO:

    def __init__(self):
        self.configEncontrada = None
        self.frecuencias = []
        self.canales = []
        self.entradas = []
                    
    def getConfiguracion(self, pInterfaz):

        #Configuración que corresponde a la interfaz

        self.configEncontrada = (
            Configuracion
            .select(Configuracion.id_configuracion, Configuracion.fecha)
            .join(UsuarioFrecuenciaInterfazConfig, on=(UsuarioFrecuenciaInterfazConfig.id_configuracion == Configuracion.id_configuracion))
            .where(UsuarioFrecuenciaInterfazConfig.id_interfaz == pInterfaz)
        )

        if self.configEncontrada:

        #Frecuencias de la configuración y la interfaz

            self.frecuencias = (
            Frecuencia
            .select(Frecuencia.id_frecuencia, Frecuencia.valor)
            .join(Interfaz_Frecuencia, on=(Interfaz_Frecuencia.id_frecuencia == Frecuencia.id_frecuencia))
            .where(Interfaz_Frecuencia.id_interfaz == pInterfaz)
            )

            #Canales de la configuración y la interfaz

            self.canales = (
                Canal
                .select(Canal.id_canal, Canal.etiqueta)
                .join(Interfaz_De_Audio, on=(Interfaz_De_Audio.id_interfaz == Canal.id_interfaz))
                .where(Interfaz_De_Audio.id_interfaz == pInterfaz)
            )

            self.entradas = (
            Entrada
                .select(Entrada.id_entrada, Entrada.etiqueta)
                .join(Interfaz_Entrada, on=(Interfaz_Entrada.id_entrada == Entrada.id_entrada))
                .where(Interfaz_Entrada.id_interfaz == pInterfaz)
            )
        
        return self.configEncontrada


