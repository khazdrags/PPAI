
class Asignacion_visita():
    def __init__(self, fecha_fin, fecha_inicio, hora_fin, hora_inicio, empleado):
        self. fecha_fin = fecha_fin
        self.fecha_inicio = fecha_inicio
        self.hora_fin = hora_fin
        self.hora_inicio = hora_inicio
        self.empleado = empleado

    # Metodos Get
    def get_fecha_fin(self):
        return self.fecha_fin

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_hora_fin(self):
        return self.hora_fin

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_empleado(self):
        return self.empleado
    
    # Metodos Set
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin

    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def set_hora_fin(self, hora_fin):
        self.hora_fin = hora_fin

    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def set_empleado(self, empleado):
        self.empleado = empleado

    # Corrobora que un guia no tenga asignada una reserva para la fecha y hora de la reserva a crear
    def es_asignacion_para_fecha_hora(self, hora_reserva, fecha_reserva, duracion_estimada_reserva):
        libre = True
        if(fecha_reserva == self.fecha_inicio) and (hora_reserva == self.hora_inicio):
            libre = False
            return libre
        else:
            return libre
