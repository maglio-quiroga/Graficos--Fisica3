import numpy as np
import pandas as pd

# Datos
datos_hidrogeno = {
    'color': ['Rojo', 'Azul', 'Violeta1'],
    'angulo': [22.7, 16.6, 14.65],
    'longitud_onda': [6735.97, 4989.67, 4414.59]
}

# Constantes
d = 16856.50  
Delta_d = 489.60  
Delta_theta = 0.1  

# Convertir datos a DataFrame
df_hidrogeno = pd.DataFrame(datos_hidrogeno)

# Convertir ángulos a radianes
df_hidrogeno['angulo_radianes'] = np.radians(df_hidrogeno['angulo'])

# Calcular sen(theta) y tan(theta)
df_hidrogeno['sen(theta)'] = np.sin(df_hidrogeno['angulo_radianes'])
df_hidrogeno['tan(theta)'] = np.tan(df_hidrogeno['angulo_radianes'])

# Calcular el error de la longitud de onda (Delta lambda)
df_hidrogeno['Delta_lambda'] = d * df_hidrogeno['sen(theta)'] * (Delta_d / d + Delta_theta / df_hidrogeno['tan(theta)'])

# Mostrar resultados
print(df_hidrogeno[['color', 'longitud_onda', 'Delta_lambda']])
