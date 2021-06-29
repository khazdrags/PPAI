from clases.exposicion import Exposicion

import clases.reserva_visita as reserva_visita

class Sede():
    def __init__(self, cant_maxima_visitantes, cant_max_por_guia, nombre, exposicion, empleado):
        self.cant_maxima_visitantes = cant_maxima_visitantes
        self.cant_max_por_guia = cant_max_por_guia
        self.nombre = nombre
        self.exposicion = exposicion
        self.empleado = empleado

    # Metodos Get
    def get_cant_maxima_visitantes(self):
        return self.cant_maxima_visitantes

    def get_cant_max_por_guia(self):
        return self.cant_max_por_guia

    def get_nombre(self):
        return self.nombre

    def get_exposicion(self):
        return self.exposicion

    def get_empleado(self):
        return self.empleado

    # Metodos set
    def set_cant_maxima_visitantes(self, cant_maxima_visitantes):
        self.cant_maxima_visitantes = cant_maxima_visitantes

    def set_cant_max_por_guia(self, cant_max_por_guia):
        self.cant_max_por_guia = cant_max_por_guia

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_exposicion(self, exposicion):
        self.exposicion = exposicion

    def set_empleado(self, empleado):
        self.empleado = empleado

    # Este metodo guarda en una lista todas las exposiciones viegentes
    def buscar_exposiciones(self,fecha_hora_actual):
        exposiciones = []
        for i in self.exposicion:
            exposicion_vigente = Exposicion.get_temp_vigentes(i,fecha_hora_actual)
            exposiciones.append(exposicion_vigente)
        return exposiciones

    #
    def buscar_duracion_exposiciones(self):
        exposiciones = 0
        for exposicion in self.exposicion:
            exposiciones = exposiciones+(Exposicion.buscar_dur_extendida_obra(exposicion))
        return exposiciones

    #
    def verificar_cantidad_maxima_visitantes(self, cantidad_seleccionada, alumnos_reserva):
        if(cantidad_seleccionada + alumnos_reserva) <= self.cant_maxima_visitantes:
            return True
        return False

    def buscar_reserva_para_fecha_hora(self, reserva):
        cantidad_alumno = 0
        for alumno in reserva:
            cantidad_alumno += reserva_visita.Rerserva_visita.obtener_alumnos_reserva(
                alumno)
        return cantidad_alumno
