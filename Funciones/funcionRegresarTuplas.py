#Funcion donde retornamos una tupla.
from formateoCadenas import nombre


def personaMayusculas(nombre,apellido,edad):
    print('Esta funcion regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(),edad

#Programa principal
nombre,apellido,edad = personaMayusculas('Ivan', 'Ausecha',19)
print('Este programa va a retornar las mayusculas del individuo: {} {} {}'.format(nombre,apellido,edad))
