from datetime import datetime
import clases.escuela as escuela
import clases.sede as sede
import clases.tipo_visita as t_v
import clases.sesion as sesion
import clases.obra
import base_de_datos.base_de_datos as BD
import clases.reserva_visita
import clases.usuario
import clases.estado


class Gestor_reserva_visita:
    def __init__(self):
        cant_seleccionada=''
        confirmado=False
        duracion_estimada=''
        #empleados disponibles? ver cuando usar
        empleados_disponibles=''
        
        escuela_seleccionada=''
        estado=''
        exposiciones_seleccionadas=''
        fecha_hora_actual=''
        fecha_hora_reserva=''
        guias_seleccionados=''
        mayor=''
        #mayor seria mejor como ultima reserva o en el mejor caso usar el nro_reserva+1
        nro_reserva=''
        #reservaVisitaNueva=''   creo q no iria ya q carece de sentido
        sede_seleccionada=''
        tipo_visita_seleccionada=''
        #falta sesion
        #esto no se si estaria encapsulado o si lo buscamos despues
        sesion=''
    
    #def tomar_reg_reserva_visita(self):
        #return
    
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
    
    #ver fecha actual
    def buscar_exposiciones_temp_vigentes(self):
        return sede.Sede.buscar_exposiciones(self.sede_seleccionada,self.fecha_hora_actual)

    def tomar_exposiciones(self,exposiciones_seleccionadas):
        self.exposiciones_seleccionadas=exposiciones_seleccionadas
    
    def tomar_fecha_hora_reserva(self,fecha_hora_reserva):
        self.fecha_hora_reserva=fecha_hora_reserva
    
    def calcular_duracion_estimada_reserva(self):
        self.duracion_estimada=sede.Sede.buscar_duracion_exposiciones(self.sede_seleccionada)
    
    #ver este hay q corregir
    def sobrepaso_cap_max(self):
        #calcular y devolver si se pasa
        return sede.Sede.buscar_reserva_para_fecha_hora(self.sede_seleccionada,self.fecha_hora_reserva)
    
    #def verificare cantidad maxima visirantes iria como def o arriba iria y eso retornaria el true o false?

    def calcular_cantidad_guias_necesarios(self):
        cant_max_guia=sede.Sede.get_cant_max_por_guia(self.sede_seleccionada)
        x = round(self.cant_seleccionada/cant_max_guia)
        if x == 0:
            x=1
        return x

    #def buscar_guias_disponibles

    def tomar_guias(self,guias):
        self.guias_seleccionados=guias
    
    def tomar_confirmacion(self):
        self.confirmado=True

    def buscar_empleado_logueado(self):
        return sesion.Sesion.get_empleado_en_sesion(self.sesion)
    


gestor_reserva_visita_nuevo=Gestor_reserva_visita()
print('\n------------------buscar escuelas')
print(gestor_reserva_visita_nuevo.buscar_escuelas())
print('\n------------------tomar escuela')
print(gestor_reserva_visita_nuevo.tomar_escuela(BD.escuela1))
print('\n------------------tomar cantidad')
print(gestor_reserva_visita_nuevo.tomar_cant_visitantes(50))
print('\n------------------buscar sede')
print(gestor_reserva_visita_nuevo.buscar_sede())
print('\n------------------tomar sede')
print(gestor_reserva_visita_nuevo.tomar_sede(BD.sede1))
print('\n------------------buscar tipo visita')
print(gestor_reserva_visita_nuevo.buscar_tipo_visita())
print('\n------------------ tomar tipo visita')
print(gestor_reserva_visita_nuevo.tomar_tipo_visita(BD.tipo_visita1))
print('\n------------------ tomar fecha hora actual')
print(gestor_reserva_visita_nuevo.tomar_fecha_hora_actual())
print('\n------------------buscar exposiciones temp vigentes')
print(gestor_reserva_visita_nuevo.buscar_exposiciones_temp_vigentes())

