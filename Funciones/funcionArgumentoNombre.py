print('Funcion con argumentos por nombre')

def imprimirPersona (nombre,apellido,edad):
    print('Persona: nombre = {}, apellido = {}, edad = {}'.format(nombre,apellido,edad))

#Primero llamamos la funcion pasando los argumentos de manera posicional
imprimirPersona('Ivan','Ausecha', 19)
#Llamamos la funcions usando argumentos por nombre
imprimirPersona(nombre='Ivan',apellido='Ausecha',edad=19)
#Tambien podemos cambiar el orden cuando llamamos por nombre
imprimirPersona(apellido='Ausecha', edad=19, nombre='Ivan')
#Argumentos con valores por default
def imprimirPersona (nombre,apellido='',edad=0):
    print('Persona: nombre = {}, apellido = {}, edad = {}'.format(nombre,apellido,edad))
imprimirPersona(apellido='Ausecha', nombre='Ivan')
