Este repositorio contiene el desarrollo de código que simula el funcionamiento de un panel de control de una interfaz de audio, implementando un diseño modular y estructurado, junto con el uso de ORM y DAO para la gestión de datos.

El uso de DAO nos permite la abstracción de acceso a los datos y el uso de ORM nos brinda una interacción eficiente con la base de datos. El panel de control nos permite simular controles tipicos de una intefaz como volumen de los canales, selección de entradas o cambio de frecuencias.

Realizado con python, el framework ORM Peewee, base de datos en sqlite y la libreria Textual para el desarrollo de la interfaz. 

Para hacer uso de la interfaz hacer uso del comando

textual run --dev main.py
