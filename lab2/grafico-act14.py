import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definición del dataframe
datos = {
    "n": [2, 3, 4, 5, 6, 7, 8, 9],
    "frecuencia-teo[hz]": [13.78, 20.67, 27.56, 34.45, 41.34, 48.23, 55.12, 62.01],
    "frecuencia-exp[hz]": [13.70, 20.70, 27.60, 34.30, 41.00, 47.80, 56.20, 62.10],
    "longitud-onda[m]": [1.57, 1.04, 0.79, 0.63, 0.54, 0.45, 0.37, 0.30],
    "velocidad[m*hz]": [2.15, 2.16, 2.18, 2.17, 2.23, 2.17, 2.07, 1.86],
}

# Agregar la columna "1/n"
datos["1/n"] = [1/valor for valor in datos["n"]]

# Crear el DataFrame
df = pd.DataFrame(datos)

#ajuste de curvas

x = df["n"]
y = df["frecuencia-exp[hz]"]
coef = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coef)
correlacion = np.corrcoef(x, y)[0, 1]

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(df["n"], df["frecuencia-exp[hz]"], marker='o', linestyle='-', color='b', label='frecuencia-exp[hz]')
plt.plot(x, poly1d_fn(x), color='r', linestyle='--', label=f'Ajuste lineal: y = {coef[0]:.2f}x + {coef[1]:.2f}\nCorrelación: {correlacion:.2f}')


# Configurar el título y las etiquetas de los ejes
plt.title('Frecuencia experimental vs n')
plt.xlabel('n')
plt.ylabel('Frecuencia experimental [hz]')
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
