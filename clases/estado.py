
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

    # Este metodo verifica si el Ambito del estado es Reserva.
    def es_ambito_reserva(self):
        if self.ambito == 'Resrva':
            return True

    # Este metodo verifica que el estado sea Pendiente de confirmacion.
    def es_pendiente_de_confirmacion(self):
        if self.nombre == 'Pendiente de confirmacion':
            return True
