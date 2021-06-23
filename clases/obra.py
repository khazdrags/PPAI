
class Obra():
    def __init__(self, alto, ancho, codigo_sensor, descripcion, duracion_extendida, duracion_resumida, fecha_creacion, fecha_primer_ingreso, nombre_obra, peso, valuacion):
        self.alto = alto
        self.ancho = ancho
        self.codigo_sensor = codigo_sensor
        self.descripcion = descripcion
        self.duracion_extendida = duracion_extendida
        self.duracion_resumida = duracion_resumida
        self.fecha_creacion = fecha_creacion
        self.fecha_primer_ingreso = fecha_primer_ingreso
        self.nombre_obra = nombre_obra
        self.peso = peso
        self.valuacion = valuacion

    # Metodos Get
    def get_alto(self):
        return self.alto

    def get_ancho(self):
        return self.ancho

    def get_codigo_sensor(self):
        return self.codigo_sensor

    def get_descripcion(self):
        return self.descripcion

    def get_duracion_extendida(self):
        return self.duracion_extendida

    def get_duracion_resumida(self):
        return self.duracion_resumida

    def get_fecha_creacion(self):
        return self.fecha_creacion

    def get_fecha_primer_ingreso(self):
        return self.fecha_primer_ingreso

    def get_nombre_obra(self):
        return self.nombre_obra

    def get_peso(self):
        return self.peso

    def get_valuacion(self):
        return self.valuacion

    # Metodos Set
    def set_alto(self, alto):
        self.alto = alto

    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_(self, codigo_sensor):
        self.codigo_sensor = codigo_sensor

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_duracion_extendida(self, duracion_extendida):
        self.duracion_extendida = duracion_extendida

    def set_duracion_resumida(self, duracion_resumida):
        self.duracion_resumida = duracion_resumida

    def set_fecha_creacion(self, fecha_creacion):
        self.fecha_creacion = fecha_creacion

    def set_fecha_primer_ingreso(self, fecha_primer_ingreso):
        self.fecha_primer_ingreso = fecha_primer_ingreso

    def set_nombre_obra(self, nombre_obra):
        self.nombre_obra = nombre_obra

    def set_peso(self, peso):
        self.peso = peso

    def set_valuacion(self, valuacion):
        self.valuacion = valuacion
