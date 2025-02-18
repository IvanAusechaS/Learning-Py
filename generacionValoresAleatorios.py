#La funcion randint(), que es parte del modulo 'random'
#randint(a,b) devuelve un numero aleatorio entre a y b
# Siempre se debe importar el modulo antes de usar las funciones
#impor random
from random import randint
numeroAleatorio = randint(1,10)# Los numeros generados siempre podran tener el primer limite pero el segundo no.
print('El numero aleatorio que generamos desde 1 hasta 10 es {}'.format(numeroAleatorio))
#Simulando un dado de 6 caras
dado = randint(1,6)
print(dado)
