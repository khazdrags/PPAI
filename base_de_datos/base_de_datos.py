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

escuela1=clases.escuela.Escuela('villa del soto','escuela@.com', 'Juan XXIII', '351987987', '351654654')
escuela2=clases.escuela.Escuela('alcira gigena','escuela3@.com', 'Pio XII', '358988582', '358644457')
escuela3=clases.escuela.Escuela('cordoba','escuela2@.com', 'Sarmiento', '358988383', '358644757')
escuela4=clases.escuela.Escuela('rio cuarto','escuela4@.com', 'Ipem 152', '358388382', '358544457')
escuela5=clases.escuela.Escuela('berrotaran','escuela5@.com', 'San Martin', '358988484', '358444457')


horario_empleado1 = clases.horario_empleado.Horario_empleado([time(7)], [time(11)])
horario_empleado2 = clases.horario_empleado.Horario_empleado([time(9)], [time(22)])
horario_empleado3 = clases.horario_empleado.Horario_empleado([time(12)], [time(17)])
horario_empleado4 = clases.horario_empleado.Horario_empleado([time(7)], [time(10)])
horario_empleado5 = clases.horario_empleado.Horario_empleado([time(13)], [time(22)])


estado1=clases.estado.Estado('reserva','es reservada','reservada')
estado2=clases.estado.Estado('obra','es obra ','pendiente de reparacion')
estado3=clases.estado.Estado('reserva','es reservada','pendiente de confirmacion')

cambioEstado1=clases.cambio_estado.Cambio_estado('20/06/2021','25/06/2021', '08:00','18:00',estado1)
cambioEstado2=clases.cambio_estado.Cambio_estado('20/07/2021','20/09/2021', '08:00','18:00',estado3)
cambioEstado3=clases.cambio_estado.Cambio_estado('25/06/2021','30/07/2021', '08:00','18:00',estado2)

publicoDestino1 = clases.publico_destino.Publico_destino('Estudiantes', 'estudiantes universitarios')
publicoDestino2 = clases.publico_destino.Publico_destino('Estudiantes de ciencias exactas', 'dirigido estudiantes de ciencias exactas')
publicoDestino3 = clases.publico_destino.Publico_destino('Aficionados', 'dirigido a personas con gran interes')



tipoExposicion1 = clases.tipo_exposicion.Tipo_exposicion('temporal', 'arte historico siglo xi-xii')
tipoExposicion2 = clases.tipo_exposicion.Tipo_exposicion('temporal', 'acripto arte')


cargo1 = clases.cargo.Cargo('Guia', 'Guia')
cargo2 = clases.cargo.Cargo('conserje', 'conserje')

empleado1 = clases.empleado.Empleado('Muñoz', 'AX2014', 23409638529, 40963852, 'cordoba', '10/05/2016',
                                     '10/05/1995', 'muñoz@hotmail.com', 'Tomas', 'masculino', '54935865412', cargo1, [horario_empleado1])
empleado2 = clases.empleado.Empleado('Fronte', 'AF6023', 23419638589, 41963858, 'cordoba', '10/10/2016',
                                     '19/06/1998', 'sofia@hotmail.com', 'Sofia', 'femenino', '54935865445', cargo1, [horario_empleado2])
empleado3 = clases.empleado.Empleado('Diaz', 'AC9827', 23419638589, 41589652, 'cordoba', '02/11/2016',
                                     '25/09/1996', 'benjamin@hotmail.com', 'Benjamin', 'masculino', '54935865445', cargo1, [horario_empleado3])
empleado4 = clases.empleado.Empleado('Gomez', 'AC4501', 23419638589, 41589652, 'cordoba', '14/04/2016',
                                     '13/12/1996', 'natalia@hotmail.com', 'Natalia', 'femenino', '54935865445', cargo1, [horario_empleado4])         
empleado5 = clases.empleado.Empleado('Sanchez', 'AC4501', 23419638589, 41589652, 'cordoba', '02/09/2015',
                                     '01/12/1993', 'mirta@hotmail.com', 'Mirta', 'femenino', '54935865445', cargo1, [horario_empleado5])   


obra1 = clases.obra.Obra('5m', '2m', '123456afd', 'cuadro y', 2, '01:00',
                         '20/10/2020', '20/10/2020', 'la gioconda', '500kg', '$2321,5 pesos',empleado1)
obra2 = clases.obra.Obra('4m', '3cm', '000456afd', 'cuadro y', 3, '00:45',
                         '20/09/2020', '20/09/2020', 'la gioconda 2', '5kg', '$100000 pesos',empleado2)

detalle_exposicion1 = clases.detalle_exposicion.Detalle_exposicion('sala 1', obra1)
detalle_exposicion2 = clases.detalle_exposicion.Detalle_exposicion('sala 2', obra2)
detalle_exposicion3 = clases.detalle_exposicion.Detalle_exposicion('sala 3', obra2)    


asignacion_visita1=clases.asignacion_visita.Asignacion_visita(date(2021,6,20),date(2021,6,20),time(8),time(12),empleado1)
asignacion_visita2=clases.asignacion_visita.Asignacion_visita(date(2021,7,20),date(2021,7,20),time(8),time(12),empleado2)

exposicion1 = clases.exposicion.Exposicion(date(2022,6,20),date(2022,6,20), date(2021,6,20), date(2021,6,20), time(8),
                                           time(21), 'Arte gotico', detalle_exposicion1, tipoExposicion1, [publicoDestino1, publicoDestino2])

exposicion2 = clases.exposicion.Exposicion(date(2022,6,20),date(2022,6,20), date(2021,6,20), date(2021,6,20), time(8),
                                           time(21), 'Moderna', detalle_exposicion2, tipoExposicion2, [publicoDestino3,publicoDestino2])

exposicion3 = clases.exposicion.Exposicion(date(2022,6,20),date(2022,6,20), date(2021,6,20), date(2021,6,20), time(8),
                                           time(21), 'Abstracta', detalle_exposicion3, tipoExposicion2, [publicoDestino3])

sede1 = clases.sede.Sede(400, 80, 'Sede 1: Malvinas Argentinas', [exposicion1,exposicion2], [empleado1,empleado2,empleado3])
sede2 = clases.sede.Sede(100, 80, 'Sede 2: Belgrano', [exposicion1, exposicion2], [empleado4,empleado5])

tipo_visita1=clases.tipo_visita.Tipo_Visita('completa')
tipo_visita2=clases.tipo_visita.Tipo_Visita('por exposicion')

usuario1=clases.usuario.Usuario(1, 'hola', 'muñoz',empleado1)

sesion1=clases.sesion.Sesion('17/06/2021', '14/06/2020', '08:02', '08:00', usuario1)


array_escuelas = [escuela1,escuela2,escuela3,escuela4,escuela5]
array_sede = [sede1,sede2]
array_tipo_visita = [tipo_visita1,tipo_visita2]
array_exposiciones=[exposicion1,exposicion2]
array_asignaciones = [asignacion_visita1,asignacion_visita2]
array_empleados=[empleado1,empleado2,empleado3,empleado4,empleado5]
array_reservas = []
array_estado = [estado1,estado2,estado3]