
class Publico_destino():
    def __init__(self, caracteristica, nombre):
        self.caracteristica = caracteristica
        self.nombre = nombre

    # Metodos Get
    def get_caracteristica(self):
        return self.caracteristica

    def get_nombre(self):
        return self.nombre

    # Metodos Set
    def set_caracteristica(self, caracteristica):
        self.caracteristica = caracteristica

    def set_nombre(self, nombre):
        self.nombre = nombre
