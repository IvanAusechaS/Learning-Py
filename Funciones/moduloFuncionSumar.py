from multiplicacionCadenas import resultado  #Definimos la funcion sumar
def sumar(a,b):
     resultado = a + b
     return resultado
#Prueba de la funcion sumar
if __name__ == '__main__':#Esto es para que no se imprima el resultado en las pruebas del main
     print('El resultado de sumar(15+30): {}'.format(sumar(15+30)))