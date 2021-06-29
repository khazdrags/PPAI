import clases.obra
import clases.detalle_exposicion
import clases.exposicion
import clases.sede
import clases.empleado
import clases.tipo_exposicion
import clases.publico_destino
import clases.cargo
import clases.horario_empleado
import clases.escuela
import clases.estado
import clases.cambio_estado
import clases.asignacion_visita
import clases.tipo_visita
import clases.usuario
import clases.sesion
from datetime import datetime, date, time, timedelta
import calendar

estado1=('reserva','es reservada','reservada')
estado2=('obra','es obra ','pendiente de reparacion')
estado3=('reserva','es reservada','pendiente de confirmacion')

cambioEstado1=clases.cambio_estado.Cambio_estado('20/06/2021','25/06/2021', '08:00','18:00',estado1)
cambioEstado2=clases.cambio_estado.Cambio_estado('20/07/2021','20/09/2021', '08:00','18:00',estado3)
cambioEstado3=clases.cambio_estado.Cambio_estado('25/06/2021','30/07/2021', '08:00','18:00',estado2)




tipoExposicion1 = clases.tipo_exposicion.Tipo_exposicion(
    'temporal', 'arte historico siglo xi-xii')

tipoExposicion2 = clases.tipo_exposicion.Tipo_exposicion(
    'temporal', 'acripto arte')

publicoDestino1 = clases.publico_destino.Publico_destino(
    'estudiantes', 'estudiantes universitarios')
publicoDestino2 = clases.publico_destino.Publico_destino(
    'estudiantes de ciencias exactas', 'dirigido estudiantes de ciencias exactas')




cargo1 = clases.cargo.Cargo('Guia', 'Guia')
cargo2 = clases.cargo.Cargo('conserje', 'conserje')

horario_empleado1 = clases.horario_empleado.Horario_empleado([time(7)], [time(22)])
horario_empleado2 = clases.horario_empleado.Horario_empleado([time(7)], [time(22)])

empleado1 = clases.empleado.Empleado('muñoz', 'AX2014', 23409638529, 40963852, 'cordoba', '10/05/2016',
                                     '10/05/1995', 'muñoz@hotmail.com', 'tomas', 'masculino', '54935865412', cargo1, [horario_empleado1])
empleado2 = clases.empleado.Empleado('fronte', 'AF6023', 23419638589, 41963858, 'cordoba', '10/10/2016',
                                     '19/06/1998', 'sofia@hotmail.com', 'sofia', 'femenino', '54935865445', cargo1, [horario_empleado2])

obra1 = clases.obra.Obra('5m', '2m', '123456afd', 'cuadro y', 2, '01:00',
                         '20/10/2020', '20/10/2020', 'la gioconda', '500kg', '$2321,5 pesos',empleado1)
obra2 = clases.obra.Obra('4m', '3cm', '000456afd', 'cuadro y', 3, '00:45',
                         '20/09/2020', '20/09/2020', 'la gioconda 2', '5kg', '$100000 pesos',empleado2)

detalle_exposicion1 = clases.detalle_exposicion.Detalle_exposicion(
    'sala 1', obra1)
detalle_exposicion2 = clases.detalle_exposicion.Detalle_exposicion(
    'sala 2', obra2)

exposicion1 = clases.exposicion.Exposicion(date(2022,6,20),date(2022,6,20), date(2021,6,20), date(2021,6,20), time(8),
                                           time(21), 'exposicion 1', detalle_exposicion1, tipoExposicion1, [publicoDestino1, publicoDestino2])


exposicion2 = clases.exposicion.Exposicion(date(2022,6,20),date(2022,6,20), date(2021,6,20), date(2021,6,20), time(8),
                                           time(21), 'exposicion 2', detalle_exposicion2, tipoExposicion2, [publicoDestino1,publicoDestino2])



asignacion_visita1=clases.asignacion_visita.Asignacion_visita(date(2021,6,20),date(2021,6,20),time(8),time(12),empleado1)
asignacion_visita2=clases.asignacion_visita.Asignacion_visita(date(2021,7,20),date(2021,7,20),time(8),time(12),empleado2)

sede1 = clases.sede.Sede(
    400, 80, 'sede 1', [exposicion1,exposicion2], [empleado1,empleado2])
sede2 = clases.sede.Sede(
    100, 80, 'sede 2', [exposicion1, exposicion2], [empleado2])

escuela1=clases.escuela.Escuela('villa del soto','escuela@.com', 'escuela n1', '351987987', '351654654')
escuela2=clases.escuela.Escuela('alcira gigena','escuela3@.com', 'escuela n2', '358988582', '358644457')
escuela3=clases.escuela.Escuela('cordoba','escuela2@.com', 'escuela n3', '358988383', '358644757')
escuela4=clases.escuela.Escuela('rio cuarto','escuela4@.com', 'escuela n4', '358388382', '358544457')
escuela5=clases.escuela.Escuela('berrotaran','escuela5@.com', 'escuela n5', '358988484', '358444457')

tipo_visita1=clases.tipo_visita.Tipo_Visita('escolar')
tipo_visita2=clases.tipo_visita.Tipo_Visita('tecnica')

usuario1=clases.usuario.Usuario(1, 'hola', 'muñoz',empleado1)

sesion1=clases.sesion.Sesion('17/06/2021', '14/06/2020', '08:02', '08:00', usuario1)









array_escuelas = [escuela1,escuela2,escuela3,escuela4,escuela5]
array_sede = [sede1,sede2]
array_tipo_visita = [tipo_visita1,tipo_visita2]
array_exposiciones=[exposicion1,exposicion2]
array_asignaciones = [asignacion_visita1,asignacion_visita2]
array_empleados=[empleado1,empleado2]