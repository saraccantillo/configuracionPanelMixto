from model.orm.model import *

objeto = (
        Config_Canal_Fuente
        .select(Config_Canal_Fuente.id_configuracion, Config_Canal_Fuente.id_canal, Config_Canal_Fuente.id_fuente)
        .where(Config_Canal_Fuente.id_canal == 1)
        .get()
        )

print(type(objeto))
print(type(objeto.id_configuracion.id_configuracion))
print(type(objeto.id_canal))
print(type(objeto.id_fuente))






