from datetime import datetime, time
import clases.escuela as escuela
import clases.sede as sede
import clases.tipo_visita as t_v
import clases.sesion as sesion
import clases.obra
import base_de_datos.base_de_datos as BD
import clases.reserva_visita
import clases.usuario
import clases.estado
import clases.empleado as empleado
import clases.reserva_visita as reserva_visita

class Gestor_reserva_visita:
    def __init__(self):
        cant_seleccionada=''
        confirmado=False
        duracion_estimada=''
        empleados_disponibles=''
        escuela_seleccionada=''
        estado=''
        exposiciones_seleccionadas=''
        fecha_hora_actual=''
        fecha_hora_reserva=''
        guias_seleccionados=''
        nro_reserva=''
        sede_seleccionada=''
        tipo_visita_seleccionada=''

    
    def buscar_escuelas(self):
        array_contador=[]
        for i in BD.array_escuelas:
            nombre_escuela = escuela.Escuela.get_nombre(i)
            array_contador.append(nombre_escuela)
        return array_contador

    def tomar_escuela(self,escuela_seleccionada):
        self.escuela_seleccionada=escuela_seleccionada
        return self.escuela_seleccionada

    def tomar_cant_visitantes(self,cant_visitantes):
        self.cant_seleccionada=cant_visitantes
        return self.cant_seleccionada
    
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
            nombre_tipo_visita = t_v.Tipo_Visita. get_nombre(i)
            array_contador.append(nombre_tipo_visita)
        return array_contador
    
    def tomar_tipo_visita(self,tipo_visita_seleccionada):
        self.tipo_visita_seleccionada=tipo_visita_seleccionada
    
    def tomar_fecha_hora_actual(self):
        self.fecha_hora_actual= datetime.now()
        return self.fecha_hora_actual
    
    def buscar_exposiciones_temp_vigentes(self):
        return sede.Sede.buscar_exposiciones(self.sede_seleccionada,self.fecha_hora_actual)

    def tomar_exposiciones(self,exposiciones_seleccionadas):
        self.exposiciones_seleccionadas=exposiciones_seleccionadas
    
    def tomar_fecha_hora_reserva(self,fecha_hora_reserva):
        self.fecha_hora_reserva=fecha_hora_reserva
    
    def calcular_duracion_estimada_reserva(self):
        self.duracion_estimada=time(sede.Sede.buscar_duracion_exposiciones(self.sede_seleccionada))
    
    def sobrepaso_cap_max(self):
        return sede.Sede.buscar_reserva_para_fecha_hora(self.sede_seleccionada,self.fecha_hora_reserva)
    
    def calcular_cantidad_guias_necesarios(self):
        cant_max_guia=sede.Sede.get_cant_max_por_guia(self.sede_seleccionada)
        x = round(self.cant_seleccionada/cant_max_guia)
        if x == 0:
            x=1
        return x

    def buscar_guias_disponibles(self):
        hora_reserva=datetime.time(self.fecha_hora_reserva)
        fecha_reserva=datetime.date(self.fecha_hora_reserva)
        asignaciones=BD.array_asignaciones
        empleados=BD.array_empleados
        array=[]
        for i in empleados:
            if empleado.Empleado.get_guia_disp_en_horario(i, self.sede_seleccionada, hora_reserva, fecha_reserva, self.duracion_estimada,asignaciones) == True:
                array.append(i)
                print('verdadero')
                print(i)
        return array

    def tomar_guias(self,guias):
        self.guias_seleccionados=guias
    
    def tomar_confirmacion(self): 
        self.confirmado=True
        self.buscar_empleado_logueado()
        self.buscar_ultimo_numero_reserva()
        self.buscar_estado_reserva()
        self.registrar_reserva()

    def buscar_empleado_logueado(self):
        return sesion.Sesion.get_empleado_en_sesion(BD.sesion1)
    
    def buscar_ultimo_numero_reserva(self):
        mayor=0
        for i in BD.array_reservas:
            x=i.getNumeroReserva()
            if mayor<x:
                mayor=x
        self.nro_reserva=mayor+1

    def buscar_estado_reserva(self):
        for i in BD.array_estado:
            ambito=i.es_ambito_reserva()
            pendiente=i.es_pendiente_de_confirmacion()
            if ambito ==True and pendiente==True:
                self.estado=i
    
    def registrar_reserva(self):
        if self.confirmado:
            fecha_reserva=datetime(self.fecha_hora_reserva.year,self.fecha_hora_reserva.month,self.fecha_hora_reserva.day)
            hora_reserva=time(self.fecha_hora_reserva.hour,self.fecha_hora_reserva.minute)
            
            nuevo=reserva_visita.Rerserva_visita(self.cant_seleccionada,self.cant_seleccionada, self.duracion_estimada, self.fecha_hora_actual, fecha_reserva,
                 '', '', hora_reserva, self.nro_reserva, self.escuela_seleccionada, self.estado,self.sede_seleccionada, self.exposiciones_seleccionadas, self.guias_seleccionados,'')
    
gestor_reserva_visita_nuevo=Gestor_reserva_visita()
gestor_reserva_visita_nuevo.tomar_fecha_hora_actual()
