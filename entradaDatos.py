#Entrada de datos por Consola
#Caracteristicas de la funcion Input
#Permite a los usuarios de nuestros programas proporcionar valores dinamicos
nombre = input('Digita tu nombre: ')
print('Recibiendo el valor de nombre : {}'.format(nombre))
#Vamos a pedir la edad
edad = int(input('Introduce tu edad: '))#Lo pasamos a tipo de dato Int para procesarlo, ya que solo recibimos de tipo string
print('Tu edad en un anio sera de : {}'.format(edad+1))#Podemos ver que podemos hacer operaciones al operar sobre un tipo de dato Int


