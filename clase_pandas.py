import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Conocer las dimensiones del archivo
data.shape

# Conocer las columnas del arhivo
data.columns

# Cantidad de elementos del arhivo
data.size

# Para saber cuantos registros hay por columna

data.count()

# Acceder a los elementos de una columna
data['Código ISO del país']

# Eliminar columnas de un dataset

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)


# Agrupar por columnas los resultados
data['Estado'].value_counts()

# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

# Cuantas personas murieron por covid en Colombia
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print(cantidad_muertes)

# Normalizar columna sexo

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

# Cuantas mujeres fallecieron en Colombia
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') ]
cantidad_muertes_mujeres = aux.shape[0]
print(cantidad_muertes_mujeres)

# Cuantas personas fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_BQ = aux.shape[0]

# Cuantas mujeres fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_mj_BQ = aux.shape[0]


# Tasa de mortalidad del covid en Colombia

cantidad_casos = data.shape[0]
tasa_mortalidad = cantidad_muertes / cantidad_casos * 100

# Agrupar por Coluna Sexo, Estado
data.groupby(['Sexo', 'Estado']).size()
data.groupby(['Estado', 'Sexo']).size()

# Normalizar columna Estado

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'


# Liste por orden descendente las 10 ciudades con mas casos reportados 

data['Nombre municipio' ].value_counts().head(10)

# Eliminar filas por condicion

# Curva de contagios en Barranquilla

data[(data['Nombre municipio'] == 'BARRANQUILLA') & (data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()


data['Tipo de recuperación'].value_counts()

data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'


# ----------------------------------------

# 1. Número de casos de Contagiados en el País.

data['Estado'].count()

# 7. Ordenar de Mayor a menor por tipo de caso

data.sort_values(by='Tipo de contagio',ascending=False)

# 8. Número de departamentos afectados

data['Nombre departamento'].nunique()

# 9. Liste los departamentos afectados(sin repetirlos)

data['Nombre departamento'].value_counts()

# 3. Liste los municipios afectados (sin repetirlos)

data['Nombre municipio'].value_counts()

# 2. Número de Municipios Afectados

data['Nombre municipio'].nunique()

# 4. Número de personas que se encuentran en atención en casa

aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
NumeroDePersonasEnCasa = aux.shape[0]

# 5. Número de personas que se encuentran recuperados

aux = data.loc[(data['Recuperado'] == 'Recuperado')]
NumeroDePersonasRecuper = aux.shape[0]

# 6. Número de personas que ha fallecido

aux = data.loc[(data['Estado'] == 'Fallecido')]
NumeroDePersonasFallecidas = aux.shape[0]

# 10. Ordene de mayor a menor por tipo de atención

data.sort_values(by='Tipo de recuperación',ascending=False )




