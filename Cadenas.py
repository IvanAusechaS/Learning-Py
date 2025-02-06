# Cadenas
# Inmutabilidad de una cadena, Una vez que se crea una cadena , los cracteres dentro de ella no pueden ser modificados
# Tendriamos que crear una nueva cadena
cadena1= 'hola'
cadena2 = "Hola Mundo"
cadena3 = '''Esto es una cadena 
de varias lineas, 
donde podemos hacer salto de linea'''
print(cadena1)
print(cadena2)
print(cadena3)
# Indices d e cadenas
cadena4 = 'Hola mundo'
primerCaracter = cadena4[1] # Recuperamos el caracter 'o'
print(primerCaracter)
# Ejemplo de direccion de memoria apuntando a los objetos (variables)
cadena5 = cadena4
cadena4 = 'Adios'
print(cadena4)
print(cadena5)