import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import numpy as np

datos = {
    'So': [28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 48, 50, 52, 54, 56, 58, 62, 66, 70, 74, 78],
    'Si': [150, 115, 94.5, 81, 69.5, 63.9, 61, 53.9, 49, 45.5, 44.7, 41.5, 40, 38.4, 38, 36.5, 35.2, 32.5, 31, 30],
}

datos_nuevos = datos.copy()
datos_nuevos['1/so'] = [ 1/num for num in datos['So']] 
datos_nuevos['1/si'] = [ 1/num for num in datos['Si']] 

df = pd.DataFrame(datos_nuevos)
print(df)

# Ajuste de regresión lineal
modelo = LinearRegression()
X = df['1/so'].values.reshape(-1, 1)
y = df['1/si'].values.reshape(-1, 1)
modelo.fit(X, y)

# Coeficientes del modelo
intercepto = modelo.intercept_[0]
pendiente = modelo.coef_[0][0]

# Coeficiente de correlación (R cuadrado)
y_pred = modelo.predict(X)
r2 = r2_score(y, y_pred)

print("Coeficiente de Correlación (R cuadrado):", r2)
print("Término Independiente (Intercepto):", intercepto)
print("Pendiente:", pendiente)

# Gráfico con ajuste de regresión lineal
plt.figure(figsize=(8, 6))
plt.scatter(df['1/so'], df['1/si'], color='b', label='Datos')
plt.plot(df['1/so'], y_pred, color='r', label=f'Regresión Lineal\nCorrelación: {r2:.2f}\nIntercepto: {intercepto:.2f}, Pendiente: {pendiente:.2f}')
plt.xlabel('1/So')
plt.ylabel('1/Si')
plt.title('Regresión Lineal de 1/Si vs. 1/So')
plt.legend()
plt.grid(True)
plt.show()

print("Coeficiente de Correlación (R cuadrado):", r2)
print("Término Independiente (Intercepto):", intercepto)
print("Pendiente:", pendiente)

