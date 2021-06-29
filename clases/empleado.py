import clases.sede as sede
from clases.asignacion_visita import Asignacion_visita
from clases.horario_empleado import Horario_empleado
from clases.cargo import Cargo


class Empleado():
    def __init__(self, apellido, codigo_validacion, cuit, dni, domicilio, fecha_ingreso, fecha_nacimiento, mail, nombre, sexo,
                 telefono, cargo, horario_empleado):
        self.apellido = apellido
        self.codigo_validacion = codigo_validacion
        self.cuit = cuit
        self.dni = dni
        self.domicilio = domicilio
        self.fecha_ingreso = fecha_ingreso
        self.fecha_nacimiento = fecha_nacimiento
        self.mail = mail
        self.nombre = nombre
        self.sexo = sexo
        self.telefono = telefono
        self.cargo = cargo
        self.horario_empleado = horario_empleado

    # Metodos Get
    def get_apellido(self):
        return self.apellido

    def get_codigo_validacion(self):
        return self.codigo_validacion

    def get_cuit(self):
        return self.cuit

    def get_dni(self):
        return self.dni

    def get_domicilio(self):
        return self.domicilio

    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_mail(self):
        return self.mail

    def get_nombre(self):
        return self.nombre

    def get_sexo(self):
        return self.sexo

    def get_telefono(self):
        return self.telefono

    def get_cargo(self):
        return self.cargo

    def get_horario_empleado(self):
        return self.horario_empleado

    # Metodos Set
    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_codigo_validacion(self, codigo_validacion):
        self.codigo_validacion = codigo_validacion

    def set_cuit(self, cuit):
        self.cuit = cuit

    def set_(self, dni):
        self.dni = dni

    def set_domicilio(self, domicilio):
        self.domicilio = domicilio

    def set_fecha_ingreso(self, fecha_ingreso):
        self.fecha_ingreso = fecha_ingreso

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def set_mail(self, mail):
        self.mail = mail

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_horario_empleado(self, horario_empleado):
        self.horario_empleado = horario_empleado

    #no anda
    def es_de_sede(self, sede_selececionada):
        print(sede_selececionada)
        for i in sede.Sede.get_empleado(sede_selececionada):
            if i == self:
                return True
        else:
            return False

    #
    def get_guia_disp_en_horario(self, sede_selececionada, hora_reserva, fecha_reserva, duracion_estimada_reserva, asignaciones):
        if Cargo.es_guia(self.cargo) and self.es_de_sede(sede_selececionada):
            for franja_horaria in self.horario_empleado:
                if Horario_empleado.disp_en_fecha_hora_reserva(franja_horaria, duracion_estimada_reserva, hora_reserva):
                    print('get guia disp tRUE')
                    for asignacion in asignaciones:
                        if Asignacion_visita.es_asignacion_para_fecha_hora(asignacion, hora_reserva, fecha_reserva, duracion_estimada_reserva):
                            print('get guia disp TRUE')
                            return True
        else:
            print('get guia disp FALSE')
            return False
