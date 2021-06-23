
class Rerserva_visita():
    def __init__(self, cantidad_alumnos, cantidad_alumno_confirmada, duracion_estimada, fecha_hora_creacion, fecha_reserva, hora_final_real, hora_inicio_real, hora_reserva, numero_reserva):
        self.cantidad_alumnos = cantidad_alumnos
        self.cantidad_alumno_confirmada = cantidad_alumno_confirmada
        self.duracion_estimada = duracion_estimada
        self.fecha_hora_creacion = fecha_hora_creacion
        self.fecha_reserva = fecha_reserva
        self.hora_final_real = hora_final_real
        self.hora_inicio_real = hora_inicio_real
        self.hora_reserva = hora_reserva
        self.numero_reserva = numero_reserva

    # Metodo Get
    def get_cantidad_alumnos(self):
        return self.cantidad_alumnos

    def get_cantidad_alumno_confirmada(self):
        return self.cantidad_alumno_confirmada

    def get_duracion_estimada(self):
        return self.duracion_estimada

    def get_fecha_hora_creacion(self):
        return self.fecha_hora_creacion

    def get_fecha_reserva(self):
        return self.fecha_reserva

    def get_hora_final_real(self):
        return self.hora_final_real

    def get_hora_inicio_real(self):
        return self.hora_inicio_real

    def get_hora_reserva(self):
        return self.hora_reserva

    def get_numero_reserva(self):
        return self.numero_reserva

    # Metodo Set
    def set_cantidad_alumnos(self, cantidad_alumnos):
        self.cantidad_alumnos = cantidad_alumnos

    def set_cantidad_alumno_confirmada(self, cantidad_alumno_confirmada):
        self.cantidad_alumno_confirmada = cantidad_alumno_confirmada

    def set_duracion_estimada(self, duracion_estimada):
        self.duracion_estimada = duracion_estimada

    def set_fecha_hora_creacion(self, fecha_hora_creacion):
        self.fecha_hora_creacion = fecha_hora_creacion

    def set_fecha_reserva(self, fecha_reserva):
        self.fecha_reserva = fecha_reserva

    def set_hora_final_real(self, hora_final_real):
        self.hora_final_real = hora_final_real

    def set_hora_inicio_real(self, hora_inicio_real):
        self.hora_inicio_real = hora_inicio_real

    def set_hora_reserva(self, hora_reserva):
        self.hora_reserva = hora_reserva

    def set_numero_reserva(self, numero_reserva):
        self.numero_reserva = numero_reserva
