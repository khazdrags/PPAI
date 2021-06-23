from datetime import datetime
import clases.escuela as escuela
import clases.sede as sede
import clases.tipo_visita as t_v
import clases.estado,clases.obra,clases.reserva_visita,clases.sede,clases.sesion,clases.usuario
import base_de_datos.base_de_datos as BD

class Gestor_reserva_visita:
    def __init__(self):
        cant_seleccionada=''
        confirmado=''
        duracion_estimada=''
        empleados_disponibles=''
        escuela_seleccionada=''
        estado=''
        exposiciones_seleccionadas=''
        fecha_hora_actual=''
        fecha_hora_reserva=''
        guias_seleccionados=''
        mayor=''
        nro_reserva=''
        #reservaVisitaNueva=''   creo q no iria ya q carece de sentido
        sede_seleccionada=''
        tipo_visita_seleccionada=''
    
    def buscar_escuelas(self):
        array_contador=[]
        for i in BD.array_escuelas:
            array_contador.append(escuela.Escuela.get_nombre(i))
        return array_contador

    def tomar_escuela(self,escuela_seleccionada):
        self.escuela_seleccionada=escuela_seleccionada

    def tomar_cant_visitantes(self,cant_visitantes):
        self.cant_seleccionada=cant_visitantes
    
    def buscar_sede(self):
        array_contador=[]
        for i in BD.array_sede:
            if sede.Sede.get_cant_maxima_visitantes(i) >= self.cant_seleccionada:
                array_contador.append(sede.Sede.get_nombre(i))
        return array_contador

    def tomar_sede(self,sede_seleccionada):
        self.sede_seleccionada=sede_seleccionada
    
    def buscar_tipo_visita(self):
        array_contador=[]
        for i in BD.array_tipo_visita:
            array_contador.append(t_v.Tipo_Visita.get_nombre(i))
        return array_contador
    
    def tomar_tipo_visita(self,tipo_visita_seleccionada):
        self.tipo_visita_seleccionada=tipo_visita_seleccionada
    
    def tomar_fecha_hora_actual(self):
        self.fecha_hora_actual= datetime.now()
    
    def buscar_exposiciones_temp_vigentes(self):
        return sede.Sede.buscar_exposiciones(self.sede_seleccionada)

    def tomar_exposiciones(self,exposiciones_seleccionadas):
        self.exposiciones_seleccionadas=exposiciones_seleccionadas
    
    def tomar_fecha_hora_reserva(self,fecha_hora_reserva):
        self.fecha_hora_reserva=fecha_hora_reserva
    
    
    