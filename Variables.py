# El nommbre no puede comenzar con digitos
# Buenas practicas. Snake case. minusculas separadas por guion bajo
# Procurar usar nombres descriptivos, para no tener confusion a la larga
#Declaracion e inicializacion de variables
nombre = 'Maria' # String
edad = 18 # int
peso = 50.7 # float
casado = False # booleano
# Accedemos a las variables
print ('Persona registrada :', nombre,",con la edad:", edad, ",con el peso :", peso, ",casado:", casado)
# Modificar el  valor de una variable
edad = 30
peso = 49.4
casado = True# Valores modificados
print ('Persona registrada :', nombre,",con la edad:", edad, ",con el peso :", peso, ",casado:", casado)
# En Python el tipo es dinamico, no debemos definir que tipo de dato es
peso = 'Grande'
print(peso)