from model.orm.model import Usuario

class UsuarioDAO:

    def __init__(self):
        self.todosLosUsuarios= []


    def getUsuario(self, pUsuario) :

        self.usuarioEncontrado = Usuario.get_by_id(pUsuario)
        
        return self.usuarioEncontrado