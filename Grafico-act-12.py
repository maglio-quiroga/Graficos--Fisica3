import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos del DataFrame
datos = {
    'So': [28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 48, 50, 52, 54, 56, 58, 62, 66, 70, 74, 78],
    'Si': [150, 115, 94.5, 81, 69.5, 63.9, 61, 53.9, 49, 45.5, 44.7, 41.5, 40, 38.4, 38, 36.5, 35.2, 32.5, 31, 30],
}

df = pd.DataFrame(datos)
df['Suma_So_Si'] = df['So'] + df['Si']

# Función y = So + 22.95
def funcion_y(so_values):
    return so_values + 22.95

# Crear el gráfico con los datos y la función
plt.figure(figsize=(8, 6))

# Graficar los datos de dispersión
plt.scatter(df['So'], df['Suma_So_Si'], color='b', label='Datos')

# Calcular los valores de y usando la función y = So + 22.95
y_vals = funcion_y(df['So'])
plt.plot(df['So'], y_vals, color='r', linestyle='--', label='y = S + 22.95')

# Modificar el gráfico existente para marcar el punto (44.5, 93.5)
plt.scatter(44.5, 93.5, color='r', label='Punto Minimo (44.5, 93.5)')

plt.xlabel('S')
plt.ylabel("S+S'")
plt.title("Gráfico de S+S' vs. So con Función y = S + 22.95")
plt.legend()
plt.grid(True)
plt.show()
