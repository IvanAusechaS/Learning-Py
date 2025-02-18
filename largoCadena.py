#Funcion para obtener el largo de una cadena, pueden ser listas, etc.
mensaje = 'Este es un ejemplo de longitud de cadena'
print('El largo de la cadena: "{}", es de {} caracteres'.format(mensaje, len(mensaje)))
# Tambien se puede hacer de esta manera.
largoCadena = len(mensaje)
print(f'El largo de la cadena {mensaje}, es de {largoCadena} caracteres')