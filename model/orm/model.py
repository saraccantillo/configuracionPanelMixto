from peewee import *

# Define the database
db = SqliteDatabase('./db/consolaAudio.db')

class Usuario(Model):
    id_usuario = AutoField()  # AUTOINCREMENT
    email = CharField(unique=True)
    contraseña = CharField()

    class Meta:
        database = db  # Define the database here


class Frecuencia(Model):
    id_frecuencia = AutoField()  # AUTOINCREMENT
    valor = FloatField()

    class Meta:
        database = db

class Tipo(Model):
    id_tipo = AutoField()  # AUTOINCREMENT
    nombre = CharField()  # Campo 'Nombre' no puede ser nulo
    descripcion = TextField(null=True)  # Campo 'Descripcion' es opcional (puede ser nulo)

    class Meta:
        database = db

class Fuente(Model):
    id_fuente = AutoField()  # AUTOINCREMENT
    etiqueta = CharField()
    id_tipo = ForeignKeyField(
        Tipo,
        db_column = 'id_tipo', #Nombre en la clase presente
        to_field= 'id_tipo' #Nombre en la clase a la que hace referencia, Arbol
    )

    class Meta:
        database = db

class Interfaz_De_Audio(Model):
    id_interfaz = AutoField()  # AUTOINCREMENT
    nombre_corto = CharField()
    modelo = CharField(null=True)
    nombre_comercial = CharField(null=True)
    precio = FloatField()

    class Meta:
        database = db


class Configuracion(Model):
    id_configuracion = AutoField()  # AUTOINCREMENT
    fecha = DateField()

    class Meta:
        database = db


class Dispositivo(Model):
    id_dispositivo = AutoField()  # AUTOINCREMENT
    nombre = CharField()
    descripcion = TextField(null=True)

    class Meta:
        database = db


class Entrada(Model):
    id_entrada = AutoField()  # AUTOINCREMENT
    etiqueta = CharField()
    descripcion = TextField(null=True)

    class Meta:
        database = db


class Canal(Model):
    id_canal = AutoField()  # AUTOINCREMENT
    etiqueta = CharField()
    id_interfaz = ForeignKeyField(
        Interfaz_De_Audio,
        db_column = 'id_interfaz', #Nombre en la clase presente
        to_field= 'id_interfaz' #Nombre en la clase a la que hace referencia, Arbol
    )
    class Meta:
        database = db

class Interfaz_Frecuencia(Model):
    id = AutoField()  # AUTOINCREMENT
    id_interfaz = ForeignKeyField(
        Interfaz_De_Audio,
        db_column = 'id_interfaz', #Nombre en la clase presente
        to_field= 'id_interfaz' #Nombre en la clase a la que hace referencia, Arbol
    )
    id_frecuencia = ForeignKeyField(
        Frecuencia, 
        db_column = 'id_frecuencia', #Nombre en la clase presente
        to_field= 'id_frecuencia')  # Foreign key to Frecuencia

    class Meta:
        database = db

class Interfaz_Fuente(Model):
    id = AutoField()  # AUTOINCREMENT
    id_interfaz = ForeignKeyField(
        Interfaz_De_Audio, 
        db_column = 'id_interfaz', #Nombre en la clase presente
        to_field= 'id_interfaz')  # Foreign key to Interfaz_de_Audio
    id_fuente = ForeignKeyField(
        Fuente, 
        db_column = 'id_fuente', #Nombre en la clase presente
        to_field= 'id_fuente')  # Foreign key to Fuente

    class Meta:
        database = db

class Interfaz_Entrada(Model):
    id = AutoField()
    id_interfaz = ForeignKeyField(
        Interfaz_De_Audio, 
        db_column = 'id_interfaz', #Nombre en la clase presente
        to_field= 'id_interfaz')
    id_entrada = ForeignKeyField(
        Entrada,
        db_column = 'id_entrada', #Nombre en la clase presente
        to_field= 'id_entrada')

    class Meta:
        database = db

class UsuarioFrecuenciaInterfazConfig(Model):
    id = AutoField()
    id_usuario = ForeignKeyField(
        Usuario,
        db_column = 'id_usuario', #Nombre en la clase presente
        to_field= 'id_usuario'
    )
    id_frecuencia = ForeignKeyField(
        Frecuencia,
        db_column = 'id_frecuencia', #Nombre en la clase presente
        to_field= 'id_frecuencia'
    )
    id_interfaz = ForeignKeyField(
        Interfaz_De_Audio, 
        db_column = 'id_interfaz', #Nombre en la clase presente
        to_field= 'id_interfaz')
    id_configuracion = ForeignKeyField(
        Configuracion,
        db_column = 'id_configuracion', #Nombre en la clase presente
        to_field= 'id_configuracion'
    )

    class Meta:
        database = db

class Entrada_Dispositivo_Config(Model):
    id = AutoField()
    id_entrada = ForeignKeyField(
        Entrada,
        db_column = 'id_entrada', #Nombre en la clase presente
        to_field= 'id_entrada'
    )
    id_dispositivo= ForeignKeyField(
        Dispositivo,
        db_column = 'id_dispositivo', #Nombre en la clase presente
        to_field= 'id_dispositivo'
    )
    id_configuracion = ForeignKeyField(
        Configuracion,
        db_column = 'id_configuracion', #Nombre en la clase presente
        to_field= 'id_configuracion'
    )

    class Meta:
        database = db

class Config_Canal_Fuente(Model):
    id = AutoField()
    volumen = IntegerField()
    solo = BooleanField()
    link = BooleanField()
    mute = BooleanField()
    id_configuracion = ForeignKeyField(
        Configuracion,
        db_column = 'id_configuracion', #Nombre en la clase presente
        to_field= 'id_configuracion'
    )
    id_canal = ForeignKeyField(
        Canal,
        db_column = 'id_canal', #Nombre en la clase presente
        to_field= 'id_canal'
    )
    id_fuente = ForeignKeyField(
        Fuente,
        db_column = 'id_fuente', #Nombre en la clase presente
        to_field= 'id_fuente'
    )

    class Meta:
        database = db


