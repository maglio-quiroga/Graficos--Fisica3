import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Datos
datos = {
    'l-ondaA': [7065.2, 6678.1, 5875.6, 5015.7, 4921.9, 4713.1, 4471.5, 3888.6],
    'angulo': [24, 23.05, 20.5, 17.5, 16.75, 16, 15.5 , 13.1],
    'd-A': [17370.45, 17055.97, 16777.48, 16679.75, 17078.29, 17098.91, 16732.25, 17156.75]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Convertir d-A a pulgadas y milímetros
df['d-P'] = df['d-A'] * 3.93701e-9
df['d-M'] = df['d-A'] * 1e-7

# Calcular los promedios
promedio_dA = df['d-A'].mean()
promedio_dM = df['d-M'].mean()
promedio_dP = df['d-P'].mean()

print(f"Promedio de d-A: {promedio_dA}")
print(f"Promedio de d-M: {promedio_dM}")
print(f"Promedio de d-P: {promedio_dP}")

# Calcular las columnas de separación
df['separacionA'] = 1 / df['d-A']
df['separacionP'] = 1 / df['d-P']
df['separacionM'] = 1 / df['d-M']

promsepA = df['separacionA'].mean()
promsepM = df['separacionM'].mean()
promsepP = df['separacionP'].mean()

print(f"Promedio de separacionA: {promsepA}")
print(f"Promedio de separacionM: {promsepM}")
print(f"Promedio de separacionP: {promsepP}")

# Agregar columna 'sen(a)'
df['sen(a)'] = np.sin(np.radians(df['angulo']))

# Ajustar curva por mínimos cuadrados
coeffs, cov = np.polyfit(df['sen(a)'], df['l-ondaA'], 1, cov=True)
m, c = coeffs
error_m, error_c = np.sqrt(np.diag(cov))

# Generar gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['sen(a)'], df['l-ondaA'], 'o', label='Datos originales')
plt.plot(df['sen(a)'], m * df['sen(a)'] + c, '-', label=f'Ajuste lineal: y={m:.2f}x + {c:.2f}')
plt.xlabel('sen(a)')
plt.ylabel('l-ondaA')
plt.title('Gráfico de Longitud de onda vs Sen(a)')
plt.legend()
plt.grid(True)
plt.show()

print(df)
print(f"Pendiente (m): {m} ± {error_m}")
print(f"Término libre (c): {c} ± {error_c}")

# Generar segundo gráfico: l-ondaA vs angulo
plt.figure(figsize=(10, 6))
plt.plot(df['angulo'], df['l-ondaA'], 'o-', color='b', label='Longitud de onda vs Ángulo')
plt.xlabel('Ángulo (grados)')
plt.ylabel('l-ondaA')
plt.title('Gráfico de Longitud de onda vs Ángulo')
plt.grid(True)
plt.show()