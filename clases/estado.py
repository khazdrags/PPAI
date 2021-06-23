
class Estado():
    def __init__(self, ambito, descripcion, nombre):
        self.ambito = ambito
        self.descripcion = descripcion
        self.nombre = nombre

    # Metodos Get
    def get_ambito(self):
        return self.ambito

    def get_descripcion(self):
        return self.descripcion

    def get_nombre(self):
        return self.nombre

    # Metodos Set
    def set_ambito(self, ambito):
        self.ambito = ambito

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_(self, nombre):
        self.nombre = nombre
