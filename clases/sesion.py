
from clases.usuario import Usuario


class Sesion ():
    def __init__(self, fecha_fin, fecha_inicio, hora_fin, hora_inicio, usuario):
        self.fecha_fin = fecha_fin
        self.fecha_inicio = fecha_inicio
        self.hora_fin = hora_fin
        self.hora_inicio = hora_inicio
        self.usuario = usuario

    # Metodo Get
    def get_fecha_fin(self):
        return self.fecha_fin

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_hora_fin(self):
        return self.hora_fin

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_usuario(self):
        return self.usuario

    # Metodos Set
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin

    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def set_hora_fin(self, hora_fin):
        self.hora_fin = hora_fin

    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def set_usuario(self, usuario):
        self.usuario = usuario

    #
    def get_empleado_en_sesion(self):
        return Usuario.get_nombre(self.usuario)
