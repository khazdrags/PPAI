import clases.cambio_estado as c_estado
from datetime import datetime, time
import clases.asignacion_visita as a_visita

class Rerserva_visita():
    def __init__(self, cantidad_alumnos, cantidad_alumno_confirmada, duracion_estimada, fecha_hora_creacion, fecha_reserva,
                 hora_final_real, hora_inicio_real, hora_reserva, numero_reserva, escuela, estado, sede, nombre_exposicion, empleado, asignacion_visita):
        self.cantidad_alumnos = cantidad_alumnos
        self.cantidad_alumno_confirmada = cantidad_alumno_confirmada
        self.duracion_estimada = duracion_estimada
        self.fecha_hora_creacion = fecha_hora_creacion
        self.fecha_reserva = fecha_reserva
        self.hora_final_real = hora_final_real
        self.hora_inicio_real = hora_inicio_real
        self.hora_reserva = hora_reserva
        self.numero_reserva = numero_reserva
        self.escuela = escuela
        self.sede = sede
        self.nombre_exposicion = nombre_exposicion
        self.empleado = empleado
        
        
        fecha=datetime(self.fecha_hora_creacion.year,self.fecha_hora_creacion.month, self.fecha_hora_creacion.day)
        hora=time(self.fecha_hora_creacion.hour,self.fecha_hora_creacion.minute)
        
        self.crear_cambio_estado(fecha,hora,estado)
        
        self.crear_asignacion_guia(fecha,hora,empleado)
        
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

    def get_escuela(self):
        return self.escuela

    def get_cambio_estado(self):
        return self.cambio_estado

    def get_sede(self):
        return self.sede

    def get_nombre_exposicion(self):
        return self.nombre_exposicion

    def get_empleado(self):
        return self.empleado

    def get_asignacion_visita(self):
        return self.asignacion_visita

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

    def set_escuela(self, escuela):
        self.escuela = escuela

    def set_cambio_estado(self, cambio_estado):
        self.cambio_estado = cambio_estado

    def set_sede(self, sede):
        self.sede = sede

    def set_nombre_exposicion(self, nombre_exposicion):
        self.nombre_exposicion = nombre_exposicion

    def set_asignacion_visita(self, asignacion_visita):
        self.asignacion_visita = asignacion_visita

    #
    def obtener_alumnos_reserva(self):
        return ([self.get_fecha_reserva(), self.get_hora_reserva, self.get_cantidad_alumnos])

    def crear_cambio_estado(self,fecha,hora,estado):
        self.cambio_estado = c_estado.Cambio_estado('',fecha,'',hora,estado)
    
    def crear_asignacion_guia(self,fecha,hora,empleado):
        array=[]
        for i in empleado:
            array.append(a_visita('',fecha,'',hora,i))
        self.asignacion_visita=array