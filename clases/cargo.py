
class Cargo():
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

    # Este metodo verifica que el empleado tenga el cargo 'guia'.
    def es_guia(self):
        if self.nombre == 'Guia':
            return True
