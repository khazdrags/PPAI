from clases.publico_destino import Publico_destino
from clases.tipo_exposicion import Tipo_exposicion
import clases.detalle_exposicion as detalle
from datetime import datetime, date, time, timedelta

class Exposicion():
    def __init__(self, fecha_fin, fecha_fin_replanificada, fecha_inicio, fecha_inicio_replanificada, hora_apertura, hora_cierre, nombre,
                 detalle_exposicion,tipo_exposicion, publico_destino):
        self.fecha_fin=fecha_fin
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

    # Este metodo devuelve el horario de apertura y cierre de una exposicion.
    def get_horario_habilitado(self):
        inicio = self.get_hora_apertura()
        cierre = self.get_hora_cierre()
        return 'Desde ' + str(inicio) + ' Hasta ' + str(cierre)

    # Este metodo devuelve el nombre, publico destino y horario de las exposiciones que son temporales y vigentes.
    def get_temp_vigentes(self,fecha_hora_actual):
        array=[]
        publico_desti = []
        if Tipo_exposicion.es_temporal(self.tipo_exposicion):
            if self.fecha_fin>=fecha_hora_actual.date(): 
                horario = self.get_horario_habilitado()
                nombre = self.get_nombre()
                for publico in self.publico_destino:
                   publico_desti.append(Publico_destino.get_nombre(publico))
            return[nombre,publico_desti,horario]
               
    # Este metodo obtiene la duracion extendida de las obras de una exposicion.
    def buscar_dur_extendida_obra(self):  
        x= detalle.Detalle_exposicion.buscar_durac_ext_obra(self.detalle_exposicion)
        return x
