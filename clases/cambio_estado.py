
class Cambio_estado():
    def __init__(self, fecha_fin, fecha_inicio, hora_fin, hora_inicio, estado):
        self.fecha_fin = fecha_fin
        self.fecha_inicio = fecha_inicio
        self.hora_fin = hora_fin
        self.hora_inicio = hora_inicio
        self.estado = estado

    # Metodos Get
    def get_fecha_fin(self):
        return self.fecha_fin

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_hora_fin(self):
        return self.hora_fin

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_estado(self):
        return self.estado

    # Metodos Set
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin

    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def set_hora_fin(self, hora_fin):
        self.hora_fin = hora_fin

    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def set_estado(self, estado):
        self.estado = estado

    #
    def conocer_estado(self):
        return self.estado
