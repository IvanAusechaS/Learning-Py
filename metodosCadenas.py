#Metodos de cadenas
#UPPER que es para pasar todo a mayuscula
mensaje = 'ESte Es uN TEXTo'
print(f'Este metodo convierte a mayuscula: {mensaje.upper()}')
#LOWER pasa todo a minuscula
print('Este metodo convierte a minuscula: {}'.format(mensaje.lower()))

mensaje2 = ' Ivan Ausecha '
print(f'esta cadena tiene espacios: {mensaje2}')
#Strip quita espacios innecesarios
print('Cadena sin espacios: {}'.format(mensaje2.strip()))