import numpy as np
import matplotlib.pyplot as plt

# Definir dimensiones del dominio
L, H = 10, 1  # Largo y alto del canal (puedes ajustar estos valores)
Nx, Ny = 400, 40  # Número de puntos en cada dirección

# Tamaño de celda
hx = L / (Nx - 1)
hy = H / (Ny - 1)

# Crear malla
x = np.linspace(0, L, Nx)
y = np.linspace(0, H, Ny)
X, Y = np.meshgrid(x, y)

# Graficar la malla
plt.figure(figsize=(10, 2))
plt.plot(X, Y, 'ko', markersize=0.5)  # Puntos de la malla
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Malla de discretización')
plt.show()

# Inicializar los campos de velocidad y presión
vx = np.zeros((Ny, Nx))  # Velocidad en X
vy = np.zeros((Ny, Nx))  # Velocidad en Y
P = np.zeros((Ny, Nx))   # Presión

# Aplicar la condición inicial de velocidad en X
for j in range(Ny):
    vy[j, :] = 0  # Velocidad en Y es 0 en todo el dominio
    vx[j, :] = (3 * j / 20) * (1 - j / 40)  # Perfil parabólico

# Aplicar gradiente de presión constante
for i in range(Nx):
    P[:, i] = -12 * i * hx  # P(x) = -12 * x (suponiendo P = 0 en x=0)
# Entrada: Fijamos el perfil de velocidad
vx[:, 0] = (3 * np.arange(Ny) / 20) * (1 - np.arange(Ny) / 40)
vy[:, 0] = 0  # No hay velocidad en Y

# Salida: Condición de Neumann (derivada cero)
vx[:, -1] = vx[:, -2]
P[:, -1] = P[:, -2]

# Paredes: Condición de no deslizamiento
vx[0, :] = 0
vx[-1, :] = 0
vy[0, :] = 0
vy[-1, :] = 0
