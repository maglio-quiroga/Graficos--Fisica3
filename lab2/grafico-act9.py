import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Definición del dataframe
datos = {
    "masa[kg]":[0.067 , 0.12 , 0.17 , 0.22 , 0.27 , 0.32 , 0.37 , 0.42 , 0.47],
    "tension[N]":[0.65 , 1.14 , 1.63 , 2.12 , 2.61 , 3.10 , 3.59 , 4.08 , 4.57],
    "velocidadT[m/s]":[21.70 , 28.65 , 34.28 , 39.00 , 43.26 , 47.13 , 50.71 , 54.05 , 57.19],
    "frecuenciaT[hz]":[27.56 , 36.84 , 43.45 , 49.52 , 54.92 , 59.84 , 64.38 , 68.63 , 72.62],
    "frecuenciaE[hz]":[27.60 , 36.60 , 43.50 , 49.10 , 55.10 , 59.30 , 64.40 , 67.90 , 71.90],
    "longitudonda[m]":[79.00 , 80.10 , 79.50 , 79.50 , 79.00 , 79.50 , 78.50 , 79.00 , 79.00],
    "velocidadE[m/s]":[21.80 , 29.07 , 34.58 , 39.03 , 43.52 , 47.14 , 50.55 , 53.64 , 56.80],
}

df = pd.DataFrame(datos)

# Calcular el cuadrado de la frecuenciaT y frecuenciaE
df['frecuenciaT^2'] = df['frecuenciaT[hz]'] ** 2
df['frecuenciaE^2'] = df['frecuenciaE[hz]'] ** 2

# Ajuste de línea recta para frecuenciaT^2
coefficients_T = np.polyfit(df['tension[N]'], df['frecuenciaT^2'], 1)
poly_T = np.poly1d(coefficients_T)

# Ajuste de línea recta para frecuenciaE^2
coefficients_E = np.polyfit(df['tension[N]'], df['frecuenciaE^2'], 1)
poly_E = np.poly1d(coefficients_E)

# Generación del gráfico para frecuenciaT^2
plt.figure(figsize=(10, 6))
plt.plot(df['tension[N]'], df['frecuenciaT^2'], 'o', label='Datos Teóricos')
tension_fit_T = np.linspace(min(df['tension[N]']), max(df['tension[N]']), 100)
frecuenciaT2_fit = poly_T(tension_fit_T)
plt.plot(tension_fit_T, frecuenciaT2_fit, '-', label=f'Ajuste: $f_T^2 = {coefficients_T[0]:.2f} T + {coefficients_T[1]:.2f}$')
plt.title('Cuadrado de la Frecuencia T vs Tensión')
plt.xlabel('Tensión [N]')
plt.ylabel('Frecuencia T^2 [Hz^2]')
plt.legend()
plt.grid(True)
plt.show()

# Generación del gráfico para frecuenciaE^2
plt.figure(figsize=(10, 6))
plt.plot(df['tension[N]'], df['frecuenciaE^2'], 'o', label='Datos Experimentales')
tension_fit_E = np.linspace(min(df['tension[N]']), max(df['tension[N]']), 100)
frecuenciaE2_fit = poly_E(tension_fit_E)
plt.plot(tension_fit_E, frecuenciaE2_fit, '-', label=f'Ajuste: $f_E^2 = {coefficients_E[0]:.2f} T + {coefficients_E[1]:.2f}$')
plt.title('Cuadrado de la Frecuencia E vs Tensión')
plt.xlabel('Tensión [N]')
plt.ylabel('Frecuencia E^2 [Hz^2]')
plt.legend()
plt.grid(True)
plt.show()

# Calcular la diferencia porcentual
df['diffrec'] = ((df['frecuenciaT[hz]'] - df['frecuenciaE[hz]']) / df['frecuenciaT[hz]']) * 100
df['difvel'] = ((df['velocidadT[m/s]'] - df['velocidadE[m/s]']) / df['velocidadT[m/s]']) * 100

# Mostrar el DataFrame actualizado con las nuevas columnas
print(df)

# Exportar a Excel
df.to_excel('Tabla2masdiferencia.xlsx', index=False)
