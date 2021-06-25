
class Tipo_exposicion():
    def __init__(self, descripcion, nombre):
        self.descripcion = descripcion
        self.nombre = nombre

    # Metodos Get
    def get_descripcion(self):
        return self.descripcion

    def get_nombre(self):
        return self.nombre

    # Metodos Set
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_nombre(self, nombre):
        self.nombre = nombre

    #
    def es_temporal(tipo_expo):
        if tipo_expo.get_nombre() == 'temporal':
            return True
        else:
            return False
