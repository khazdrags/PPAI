from datetime import datetime, date, time, timedelta
from datetime import datetime
from datetime import timedelta



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

    # Este metodo verifica que el empleado trabaja en la sede en el horario de la reserva a crear.
    def disp_en_fecha_hora_reserva(self, duracion_estimada_reserva, hora_reserva):
        bandera = False
        for i in self.hora_ingreso:
            if ((hora_reserva) >= i) and ((self.hora_salida[0])>hora_reserva):
                bandera = True
                return bandera
        return False