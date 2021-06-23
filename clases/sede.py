
class Sede():
    def __init__(self, cant_maxima_visitantes, cant_max_por_guia, nombre):
        self.cant_maxima_visitantes = cant_maxima_visitantes
        self.cant_max_por_guia = cant_max_por_guia
        self.nombre = nombre

    # Metodos Get
    def get_cant_maxima_visitantes(self):
        return self.cant_maxima_visitantes

    def get_cant_max_por_guia(self):
        return self.cant_max_por_guia

    def get_nombre(self):
        return self.nombre

    # Metodos set
    def set_cant_maxima_visitantes(self, cant_maxima_visitantes):
        self.cant_maxima_visitantes = cant_maxima_visitantes

    def set_cant_max_por_guia(self, cant_max_por_guia):
        self.cant_max_por_guia = cant_max_por_guia

    def set_nombre(self, nombre):
        self.nombre = nombre
