 #Funciones en Python
from moduloFuncionSumar import sumar
 #definimos la funcion
def saludarMiFuncion(mensaje): #Firma del metodo
    #Cuerpo de la funcion
    print('Mensaje recibido por el usuario :"{}"'.format(mensaje))

#Programa principal, llamamos a la funcion
saludarMiFuncion('Hola a todos')
saludarMiFuncion(10)
print('El resultado de la suma de {} + {} = {}'.format(4,7,sumar(4,7)))
