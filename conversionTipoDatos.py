#Conversion de tipos de datos
#Python Master
#Convertir de cadena a numero
nuevaCadena = '10'
nuevaCadenaInt = int(nuevaCadena)*7
print('La nueva cadena de {}, sera: {} multiplicado por 7, dandonos como resultado {}'.format(nuevaCadena,nuevaCadena,nuevaCadenaInt))
#Para el ejemplo de cadena pero para un tipo de dato float
nuevaCadena = '3.14'
nuevaCadenaFloat = float(nuevaCadena)
print(f'Cadena flotante = {nuevaCadenaFloat}')
#Ahora para un numero a Cadena
nuevaCadena = 25
nuevaCadenaStr = str(nuevaCadena)
print(f'Cadena de tipo Str : {nuevaCadenaStr}')
#Para el caso del valor booleano, tenemos
#Si el valor es 0, cadena vacia, o None, entonces regresa False
#regresa True, si el valor es distinto de 0, si es distinto de cadena vacia
# Y tambien si es distinto de None
nuevaCadena = 'True con texto'
booleano = bool(nuevaCadena)
print('El valor de la cadena {}, en Booleano es de {}'.format(nuevaCadena, booleano))
#Para una cadena Vacia nos va a retornar False
nuevaCadena = ''
booleano = bool(nuevaCadena)
print('El valor de la cadena {}, en Booleano es de {}'.format(nuevaCadena, booleano))
#Para una cadena donde tenga un valor distinto de 0, nos va a retornar True
nuevaCadena = 4
booleano = bool(nuevaCadena)
print('El valor de la cadena {}, en Booleano es de {}'.format(nuevaCadena, booleano))
#Si el largo de la cadena es 0, retorna False
nuevaCadena = 0
booleano = bool(nuevaCadena)
print('El valor de la cadena {}, en Booleano es de {}'.format(nuevaCadena, booleano))

#True == 1, False == 0. Entonces al operarlos por un entero o un flotante estos devolveran un numero
resultado = False * 7
print(resultado)
