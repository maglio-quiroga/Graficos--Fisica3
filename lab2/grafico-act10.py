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

# Calcular el cuadrado de la velocidadT y velocidadE
df['velocidadT^2'] = df['velocidadT[m/s]'] ** 2
df['velocidadE^2'] = df['velocidadE[m/s]'] ** 2

# Ajuste de línea recta para velocidadT^2
coefficients_T = np.polyfit(df['velocidadT^2'], df['tension[N]'], 1)
poly_T = np.poly1d(coefficients_T)

# Ajuste de línea recta para velocidadE^2
coefficients_E = np.polyfit(df['velocidadE^2'], df['tension[N]'], 1)
poly_E = np.poly1d(coefficients_E)

#eje x y eje y
x1=df['tension[N]']
y1=df['velocidadT^2']

# Generación del gráfico para velocidadT^2 vs Tensión
plt.figure(figsize=(10, 6))
plt.plot(y1, x1, 'o', label='Datos Teóricos')
tension_fit_T = np.linspace(min(df['velocidadT^2']), max(df['velocidadT^2']), 100)
tension_T_fit = poly_T(tension_fit_T)
plt.plot(tension_fit_T, tension_T_fit, '-', label=f'Ajuste: $T = {coefficients_T[0]:.2f} v_T^2 + {coefficients_T[1]:.2f}$')
plt.title('Cuadrado de la Velocidad T vs Tensión')
plt.xlabel('Velocidad T^2 [m^2/s^2]')
plt.ylabel('Tensión [N]')
plt.legend()
plt.grid(True)
plt.show()

# Generación del gráfico para velocidadE^2 vs Tensión
plt.figure(figsize=(10, 6))
plt.plot(df['velocidadE^2'], df['tension[N]'], 'o', label='Datos Experimentales')
tension_fit_E = np.linspace(min(df['velocidadE^2']), max(df['velocidadE^2']), 100)
tension_E_fit = poly_E(tension_fit_E)
plt.plot(tension_fit_E, tension_E_fit, '-', label=f'Ajuste: $T = {coefficients_E[0]:.2f} v_E^2 + {coefficients_E[1]:.2f}$')
plt.title('Cuadrado de la Velocidad E vs Tensión')
plt.xlabel('Velocidad E^2 [m^2/s^2]')
plt.ylabel('Tensión [N]')
plt.legend()
plt.grid(True)
plt.show()
