from publico_destino import Publico_destino
from tipo_exposicion import Tipo_exposicion
from detalle_exposicion import Detalle_exposicion


class Exposicion():
    def __init__(self, fecha_fin, fecha_fin_replanificada, fecha_inicio, fecha_inicio_replanificada, hora_apertura, hora_cierre, nombre,
                 tipo_exposicion, publico_destino, detalle_exposicion):
        self.fecha_fin = fecha_fin
        self.fecha_fin_replanificada = fecha_fin_replanificada
        self.fecha_inicio = fecha_inicio
        self.fecha_inicio_replanificada = fecha_inicio_replanificada
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre
        self.nombre = nombre
        self.tipo_exposicion = tipo_exposicion
        self.publico_destino = publico_destino
        self.detalle_exposicion = detalle_exposicion

    # Metodos Get
    def get_fecha_fin(self):
        return self.fecha_fin

    def get_fecha_fin_replanificada(self):
        return self.fecha_fin_replanificada

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_fecha_inicio_replanificada(self):
        return self.fecha_inicio_replanificada

    def get_hora_apertura(self):
        return self.hora_apertura

    def get_hora_cierre(self):
        return self.hora_cierre

    def get_nombre(self):
        return self.nombre

    def get_tipo_exposicion(self):
        return self.tipo_exposicion

    def get_publico_destino(self):
        return self.publico_destino

    def get_detalle_exposicion(self):
        return self.detalle_exposicion

    # Metodos Set

    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin

    def set_fecha_fin_replanificada(self, fecha_fin_replanificada):
        self.fecha_fin_replanificada = fecha_fin_replanificada

    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def set_fecha_inicio_replanificada(self, fecha_inicio_replanificada):
        self.fecha_inicio_replanificada = fecha_inicio_replanificada

    def set_hora_cierre(self, hora_cierre):
        self.hora_cierre = hora_cierre

    def set_hora_apertura(self, hora_apertura):
        self.hora_apertura = hora_apertura

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_tipo_exposicion(self, tipo_exposicion):
        self.tipo_exposicion = tipo_exposicion

    def set_publico_destino(self, publico_destino):
        self.publico_destino = publico_destino

    def set_detalle_exposicion(self, detalle_exposicion):
        self.detalle_exposicion = detalle_exposicion

    #
    def get_horario_habilitado(self):
        inicio = self.get_hora_apertura()
        cierre = self.get_hora_cierre()
        return 'Desde' + str(inicio) + 'Hasta ' + str(cierre)

    #
    def get_temp_vignetes(self):
        publico_desti = []
        horario = ''
        if Tipo_exposicion.es_temporal(self.get_tipo_exposicion()):
            horario = self.get_horario_habilitado()
            for publico in self.publico_destino:
                nombre = Publico_destino.get_nombre(publico)
                publico_desti.append(nombre)

    #
    def buscar_dur_extendida_obra(self):
        return Detalle_exposicion.buscar_dur_extendida_obra(self.detalle_exposicion)
