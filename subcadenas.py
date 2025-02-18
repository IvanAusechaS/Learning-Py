#Subcadenas en python
#Una subcadena es una parte de una cadena principal, se pueden extraer, buscar y reemplazar subcadenas
mensaje = 'Hola, Mundo!'
# Vamos a obtener 'Hola' de la cadena mensaje
subcadenaMensaje = mensaje[0:4]
print('Esta es la subcadena de {}, donde sacamos {}'.format(mensaje, subcadenaMensaje))
print('Esta es la subcadena de :"{}", donde sacamos "{}"'.format(mensaje, mensaje[0:4]))
#Buscar cadenas con (find)
posicion = mensaje.find('Mundo!')
print(posicion)
print(mensaje.find('Mundo!'))
# Vamos a ponerlo en los parametros del format
print('La cadena que buscamos es {}'.format(mensaje[mensaje.find('M'):mensaje.find('!')]))

#Reemplazar una subcadena (.replace)
nuevoMensaje = mensaje.replace('Mundo!', 'a todos')
print(f'Reemplazamos la cadena: {mensaje} por la cadena {nuevoMensaje}')
print('Reemplazamos la cadena : "{}" por la cadena "{}"'.format(mensaje, mensaje.replace('Mundo!','a todos')))

# El mismo ejemplo pero queremos decir Adios a todos
print('Reemplazamos toda la cadena : "{}" por la cadena "{}"'.format(mensaje, mensaje.replace('Hola, Mundo!','Adios a todos')))
# Adios, Mundo!
print('Reemplazamos la cadena : "{}" por "{}"'.format(mensaje,mensaje.replace('Hola','Adios')))
#Extraer subcadenas, con el metodo (split) nos retorna una lista
datos = 'Ivan, 19,Colombia'
listaDatos = datos.split(',')
print(listaDatos)
#Por default el split separa el espacio
mensaje='Hola mundo'
print('Split del mensaje :"{}" por "{}"'.format(mensaje, mensaje.split()))



