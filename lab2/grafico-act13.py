import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definición del dataframe
datos = {
    "n": [2, 3, 4, 5, 6, 7, 8, 9],
    "frecuencia-teo[hz]": [13.78, 20.67, 27.56, 34.45, 41.34, 48.23, 55.12, 62.01],
    "frecuencia-exp[hz]": [13.70, 20.70, 27.60, 34.30, 41.00, 47.80, 56.20, 62.10],
    "longitud-onda[m]": [1.57, 1.04, 0.79, 0.63, 0.54, 0.45, 0.37, 0.30],
    "velocidad[m*hz]": [21.57, 21.63, 21.80, 21.78, 22.34, 21.74, 20.79, 18.69],
}

# Agregar la columna "1/n"
datos["1/n"] = [1/valor for valor in datos["n"]]
datos['producto'] = [longitud * nodos for longitud, nodos in zip(datos['longitud-onda[m]'], datos['n'])]

# Crear el DataFrame
df = pd.DataFrame(datos)

# Calcular la diferencia porcentual entre frecuencia-teo[hz] y frecuencia-exp[hz]
df['diferencia'] = ((df['frecuencia-teo[hz]'] - df['frecuencia-exp[hz]']) / df['frecuencia-teo[hz]']) * 100

# Calcular la línea de ajuste lineal
x = df["1/n"]
y = df["longitud-onda[m]"]
coef = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coef)

# Calcular la correlación
correlacion = np.corrcoef(x, y)[0, 1]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Datos experimentales')
plt.plot(x, poly1d_fn(x), color='r', linestyle='--', label=f'Ajuste lineal: y = {coef[0]:.2f}x + {coef[1]:.2f}\nCorrelación: {correlacion:.2f}')

# Configurar el título y las etiquetas de los ejes
plt.title('Longitud de onda vs 1/n')
plt.xlabel('1/n')
plt.ylabel('Longitud de onda [m]')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()

# Calculos estadisticos (promedio entre otros)
print("El promedio de las velocidades es:", df["velocidad[m*hz]"].mean())
print("El promedio de los productos de lambda por los nodos es:", df['producto'].mean())

# Mostrar el DataFrame actualizado con la nueva columna
print(df)

# Exportar a Excel
#df.to_excel('Tabla1.xlsx', index=False)
