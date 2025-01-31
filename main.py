from textual.app import App
from textual.widgets import Header, Label, Footer, RadioButton, RadioSet, Checkbox, Digits, Button
from textual.widget import Widget
from textual.screen import Screen
from textual import on
from textual.containers import HorizontalScroll, Horizontal
from model.dao.ConfiguracionDAO import ConfiguracionDAO
from model.dao.CanalDAO import CanalDAO
from model.dao.FuenteDAO import FuenteDAO
from model.orm.model import *
from textual.widgets import Select

#textual run --dev main.py

class InterfazWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: str = None, pConfiguracionDAO: ConfiguracionDAO = None, pCanalDAO: CanalDAO = None):
        super().__init__()
        self.id = id
        self.configuracionDAO = pConfiguracionDAO or ConfiguracionDAO()
        self.canalDAO = pCanalDAO or CanalDAO()

    def compose(self):

        interfaces = Interfaz_De_Audio.select()

        opciones = [(interfaz.nombre_corto, interfaz.id_interfaz) for interfaz in interfaces]
        yield Select(options=opciones, prompt="Interfaces")
        

    def on_select_changed(self, event: Select.Changed):

        #Cuando cambia el select de interfaces, llamo a InterfazDAO para que me traiga la información de esta interfaz
        interfaz = Interfaz_De_Audio.get_by_id(event.value)

        #Cuando tengo la informacion, obtengo la configuracion correspondiente por medio de la id de la interfaz

        self.configuracionDAO.getConfiguracion(interfaz)

        opciones2 = [(str(q.valor), str(q.id_frecuencia)) for q in self.configuracionDAO.frecuencias]
        self.app.query_one("#selectFrecuencias", Select).set_options(options=opciones2)

        ##Actualizado las entradas que pertenecen a esta interfaz y configuración
        self.app.query_one("#horizontalEntradas", HorizontalScroll).remove_children()

        for q in self.configuracionDAO.entradas:
            self.app.query_one("#horizontalEntradas", HorizontalScroll).mount(EntradaWidget(id= q.id_entrada, idEntrada= q.id_entrada))

        #Actualizando los canales que pertenecen a esta interfaz y configuración

        self.app.query_one("#horizontalCanales", HorizontalScroll).remove_children()

        for q in self.configuracionDAO.canales:
            self.app.query_one("#horizontalCanales", HorizontalScroll).mount(CanalWidget(id= q.id_canal, idCanal= q.id_canal))

class FrecuenciaWidget(Widget):

    CSS_PATH = "style.css"

    def compose(self):

        opciones = [
            ("Valor 1", "1"),
            ("Valor 2", "2"),
            ("Valor 3", "3"),
        ]

        yield Select(id="selectFrecuencias", options=opciones, prompt="Frecuencias", classes="selectFrecuencias")

class EntradaWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: str = None, idEntrada: str = -1):
        super().__init__()
        self.id = f"idEntrada{id}"
        self.idEntrada = idEntrada

    def compose(self):

        queryEntrada = Entrada.get_by_id(self.idEntrada) 

        with RadioSet():
            yield RadioButton(f"Entrada {queryEntrada.etiqueta}")

class VolumenWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id : str = None, idCanal: str = None):
        super().__init__()
        self.id = f"idVolumen{id}"
        self.idCanal = idCanal
        self.canalDAO = CanalDAO()

    def compose(self):

        volumen = self.canalDAO.getConfiguracionVolumen(self.idCanal)

        yield Digits(f"{volumen}", id= f"VolumenCanal{self.idCanal}", classes="displayVolumen")

class VolumenUp(Widget):

    CSS_PATH = "style.css"

    def __init__(self, idCanal: str = None):
        super().__init__()
        self.idCanal = idCanal
        self.canalDAO = CanalDAO()

    def compose(self):

        yield Button("▲", variant="primary", id=f"buttonUpCanal{self.idCanal}", classes="volumenButton")

    def on_button_pressed(self, event: Button.Pressed):

        valueDigits = self.app.query_one(f"#VolumenCanal{self.idCanal}", Digits)
        volumenActual = int(valueDigits.value)
        if volumenActual == 100:
            valueDigits.update(value=f"{str(volumenActual)}")
        else:
            volumenActual += 1
            valueDigits.update(value=f"{str(volumenActual)}")
            self.canalDAO.cambiarVolumen(volumenActual, self.idCanal)
            

class VolumenDown(Widget):

    CSS_PATH = "style.css"

    def __init__(self, idCanal: str = None):
        super().__init__()
        self.idCanal = idCanal
        self.canalDAO = CanalDAO()

    def compose(self):

        yield Button("▼", variant="default", id=f"buttonDownCanal{self.idCanal}", classes="volumenButton")

    def on_button_pressed(self, event: Button.Pressed):

        valueDigits = self.app.query_one(f"#VolumenCanal{self.idCanal}", Digits)
        volumenActual = int(valueDigits.value)
        if volumenActual == 0:
            valueDigits.update(value=f"{str(volumenActual)}")
        else:
            volumenActual -= 1
            valueDigits.update(value=f"{str(volumenActual)}")
            self.canalDAO.cambiarVolumen(volumenActual, self.idCanal)
            
class SoloWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: str = None, idCanal: str = None):
        super().__init__()
        self.id = f"idSolo{id}"
        self.idCanal = idCanal
        self.canalDAO = CanalDAO()

    def compose(self):

        solo = bool(self.canalDAO.getConfiguracionSolo(pCanal=self.idCanal))
        yield Checkbox("SOLO", value=solo)

    def on_checkbox_changed(self, event: Checkbox.Changed):

        self.canalDAO.cambiarSolo(pSolo=int(event.value), pCanal=self.idCanal)

class MuteWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: str = None, idCanal: str = None):
        super().__init__()
        self.id = f"idMute{id}"
        self.idCanal = idCanal
        self.canalDAO = CanalDAO()

    def compose(self):

        mute = bool(self.canalDAO.getConfiguracionMute(pCanal=self.idCanal))
        yield Checkbox("MUTE", value=mute, classes="muteSelect")

    def on_checkbox_changed(self, event: Checkbox.Changed):

        self.canalDAO.cambiarMute(pMute=int(event.value), pCanal=self.idCanal)

class LinkWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: str = None, idCanal: str = None):
        super().__init__()
        self.id = f"idLink{id}"
        self.idCanal = idCanal
        self.canalDAO = CanalDAO()

    def compose(self):

        link = bool(self.canalDAO.getConfiguracionLink(pCanal=self.idCanal))
        yield Checkbox("LINK", value=link)

    def on_checkbox_changed(self, event: Checkbox.Changed):

        self.canalDAO.cambiarLink(pLink=int(event.value), pCanal=self.idCanal)

class CanalWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: str = None, idCanal: str = -1, pCanalDAO: CanalDAO = None):
        super().__init__()
        self.id = f"idCanal{id}"
        self.idCanal = idCanal
        self.canalDAO = pCanalDAO or CanalDAO()

    def compose(self):

        queryCanal = Canal.get_by_id(self.idCanal)

        fuenteConfigurada = self.canalDAO.getConfiguracionFuente(queryCanal.id_canal)

        yield Label(f"{queryCanal.etiqueta}")

        yield TipoWidget(id=self.idCanal, tipo= fuenteConfigurada.id_fuente.id_tipo.id_tipo, idCanal=self.idCanal)
        yield FuenteWidget(id=self.idCanal, idCanal= self.idCanal )

        yield VolumenWidget(id= self.idCanal, idCanal=self.idCanal)

        with Horizontal(classes="horizontalVolumen"):
            yield VolumenUp(idCanal= self.idCanal)
            yield VolumenDown(idCanal= self.idCanal)

        with Horizontal(id="horizontalCanalAtributes", classes="horizontalCanalAtributes"):
            yield SoloWidget(id= self.idCanal, idCanal= self.idCanal)
            yield MuteWidget(id= self.idCanal, idCanal= self.idCanal)
            yield LinkWidget(id= self.idCanal, idCanal= self.idCanal)

class FuenteWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, idCanal: str = None, id: str = None):
        super().__init__()
        self.idCanal = idCanal
        self.id = f"idFuente{id}"
        self.idFuente = f"{idCanal}"
        self.canalDAO = CanalDAO()

    def compose(self):

        queryCanal = Canal.get_by_id(self.idCanal)

        fuenteConfigurada = self.canalDAO.getConfiguracionFuente(queryCanal.id_canal)

        opcionesF = [("Tipo 1", 1), ("Tipo 2", 2)]
        yield Select(prompt="Fuente", options=opcionesF, classes="selectFuente", id=f"selectFuente{self.idFuente}", allow_blank=True)
        yield Label(f"Fuente precargada: {fuenteConfigurada.id_fuente}",id=f"labelFuente{self.idFuente}")

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed):

        if event.value is not Select.BLANK:

            #self.app.query_one(f"#labelFuente{self.idFuente}", Label).update(f"{event.value}")
            self.canalDAO.cambiarFuente(pFuente= event.value, pCanal= self.idCanal)

class TipoWidget(Widget):

    CSS_PATH = "style.css"

    def __init__(self, id: int = None, tipo = None, idCanal: str = None):
        super().__init__()
        self.tipo = tipo
        self.fuenteDAO = FuenteDAO()
        self.id = f"idTipo{id}"
        self.idTipo = f"{idCanal}"
    
    def compose(self):

        tipos = Tipo.select()

        opcionesT = [(tipo.nombre, tipo.id_tipo) for tipo in tipos]
        yield Select(prompt="Tipo", options=opcionesT, classes="selectTipo", id=f"selectTipo{self.idTipo}", value= self.tipo)

    def on_select_changed(self, event: Select.Changed):

        self.fuenteDAO.getFuentesIns(event.value)

        opciones = [(q.etiqueta, q.id_fuente) for q in self.fuenteDAO.fuentesIns]

        self.app.query_one(f"#selectFuente{self.idTipo}", Select).set_options(options=opciones)

class DashBoardGeneral(Screen):

    CSS_PATH = "style.css"

    def compose(self):
        configuracionDAO = ConfiguracionDAO()
        canalDAO = CanalDAO()

        yield Header()

        with Horizontal(id="horizontalInicio"):

            yield InterfazWidget(id="widgetInterfaz", pConfiguracionDAO = configuracionDAO, pCanalDAO=canalDAO)
            yield FrecuenciaWidget(id="widgetFrecuencias")

        with HorizontalScroll(id="horizontalEntradas"):
            yield Label()        

        with HorizontalScroll(id="horizontalCanales"):
            yield Label()

        yield Footer()

class MezcladorAudio(App):

    CSS_PATH = "style.css"

    def on_ready(self):
        self.push_screen(DashBoardGeneral())

MezcladorAudio().run()