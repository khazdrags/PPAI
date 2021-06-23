import clases.escuela as escuela
import clases.estado,clases.obra,clases.reserva_visita,clases.sede,clases.sesion,clases.tipo_visita,clases.usuario
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
        
    
    def buscar_esculas(self):
        array_contador=[]
        for i in BD.array_escuelas:
            array_contador.append(escuela.Escuela.get_nombre(i))
        return array_contador
