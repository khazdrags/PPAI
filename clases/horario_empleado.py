from datetime import datetime, date, time, timedelta
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class Horario_empleado():
    def __init__(self, hora_ingreso, hora_salida):
        self.hora_ingreso = hora_ingreso
        self.hora_salida = hora_salida

    # Metodos Get
    def get_hora_ingreso(self):
        return self.hora_ingreso

    def get_hora_salida(self):
        return self.hora_salida

    # Metodos Set
    def set_hora_ingreso(self, hora_ingreso):
        self.hora_ingreso = hora_ingreso

    def set_hora_salida(self, hora_salida):
        self.hora_salida = hora_salida


    def disp_en_fecha_hora_reserva(self, duracion_estimada_reserva, hora_reserva):
        bandera = False
       # formato = "%H:%M:%S"
        #tiempo = datetime.strptime(str(hora_reserva.hour), formato) + datetime.strptime(str(duracion_estimada_reserva.hour), formato)
        for i in self.hora_ingreso:

            if ((hora_reserva) >= i) and ((self.hora_salida[0])>hora_reserva):
                bandera = True
                return bandera
        return False