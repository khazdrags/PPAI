
class Escuela():
    def __init__(self, domicilio, mail, nombre, telef_celular, telef_fijo):
        self.domicilio = domicilio
        self.mail = mail
        self.nombre = nombre
        self.telef_celular = telef_celular
        self.telef_fijo = telef_fijo

    # Metodos Get
    def get_domicilio(self):
        return self.domicilio

    def get_mail(self):
        return self.mail

    def get_nombre(self):
        return self.nombre

    def get_telef_celular(self):
        return self.telef_celular

    def get_telef_fijo(self):
        return self.telef_fijo

    # Metodos Set
    def set_domicilio(self, domicilio):
        self.domicilio = domicilio

    def set_mail(self, mail):
        self.mail = mail

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_telef_celular(self, telef_celular):
        self.telef_celular = telef_celular

    def set_telef_fijo(self, telef_fijo):
        self.telef_fijo = telef_fijo
