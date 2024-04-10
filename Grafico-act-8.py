import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

datos = {
    'So': [28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 48, 50, 52, 54, 56, 58, 62, 66, 70, 74, 78],
    'Si': [150, 115, 94.5, 81, 69.5, 63.9, 61, 53.9, 49, 45.5, 44.7, 41.5, 40, 38.4, 38, 36.5, 35.2, 32.5, 31, 30],
    'f': [23.949, 24.1, 24.39, 24.194, 23.931, 24.024, 24.339, 23.762, 23.32, 23.358, 23.6, 23.08, 22.978, 22.779, 22.958, 22.974, 22.956, 22.195, 21.847, 21.667],
}


nuevos_datos = datos.copy()


nuevos_datos['R'] = [2 * valor for valor in nuevos_datos['f']]


df = pd.DataFrame(nuevos_datos)

des_stndr1 = df['f'].std()
prom1 = df['f'].mean()
error1 = df['f'].sem() 

des_stndr2 = df['R'].std()
prom2 = df['R'].mean()
error2 = df['R'].sem()


print(df)

print("promedio: ", prom1)
print("error: ", error1)
print("desviacion: ",des_stndr1)

print("promedio: ", prom2)
print("error: ", error2)
print("desviacion: ",des_stndr2)

# Ajustar una regresión lineal a los datos
modelo = LinearRegression()
X = df['So'].values.reshape(-1, 1)
y = df['Si'].values.reshape(-1, 1)
modelo.fit(X, y)

# Ajuste polinomial de grado 2
coeffs = np.polyfit(df['So'], df['Si'], 2)
poly = np.poly1d(coeffs)

# Coeficiente de correlación para el ajuste polinomial
correlation_poly = np.corrcoef(df['Si'], poly(df['So']))[0, 1]

# Gráfico de Datos y Ajuste Polinomial
plt.figure(figsize=(8, 6))
plt.scatter(df['So'], df['Si'], color='b', label='Datos')
plt.plot(df['So'], poly(df['So']), color='r', label=f'Ajuste Polinomial\nCorrelación: {correlation_poly:.2f}')
plt.xlabel('So')
plt.ylabel('Si')
plt.title('Ajuste Polinomial de Si vs. So (Grado 2)')
plt.legend()
plt.grid(True)
plt.show()

print("Coeficientes del Polinomio:", coeffs)
print("Coeficiente de Correlación (Ajuste Polinomial):", correlation_poly)
