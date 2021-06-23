
class Usuario():
    def __init__(self, caducidad, contrasena, nombre):
        self.caducidad = caducidad
        self.contrasena = contrasena
        self.nombre = nombre

    # Metodo Get
    def get_caducidad(self):
        return self.caducidad

    def get_contrasena(self):
        return self.contrasena

    def get_nombre(self):
        return self.nombre

    # Metodo Set
    def set_caducidad(self, caducidad):
        self.caducidad = caducidad

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_nombre(self, nombre):
        self.nombre = nombre
