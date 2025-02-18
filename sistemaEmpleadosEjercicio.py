#crea un programa para solicitar la informacion de un empleado
nombreEmpleado = input('Digita tu nombre: ')
edadEmpleado = int(input('Digita tu edad: '))
salarioEmpleado = float(input('Digita tu salario: '))
inputJefe =(input("Digita si eres jefe de departamento donde (Si/no): "))
boolJefe = inputJefe.lower() == 'si'
print(nombreEmpleado + '\n' + str(edadEmpleado) + '\n' + str(salarioEmpleado) + '\n' + str(boolJefe))
