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

# 11. 

data['Nombre departamento'].value_counts().head(10)

# 12. 

aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()
aux.sort_values(ascending=False).head(10)

# 13.

aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()
aux.sort_values(ascending=False).head(10)

# 14. 

data['Nombre municipio'].value_counts().head(10)

# 15. 

aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()
aux.sort_values(ascending=False).head(10)

# 16.

aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()
aux.sort_values(ascending=False).head(10)

# 17.

aux = data.groupby(['Nombre departamento', 'Nombre municipio']).size()
aux.sort_values(ascending=False)

# 18.

aux = data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo']).size()
aux.sort_values(ascending=False)

# 19. 

data.groupby(['Nombre departamento', 'Nombre municipio', 'Sexo'])['Edad'].mean()

# 20.

aux = data.groupby(['Nombre del país']).size()
aux.sort_values(ascending=False)

# 21.

aux = data.groupby(['Fecha de diagnóstico']).size()
aux.sort_values(ascending=False)

# 22.

canti_muertes = data[data['Estado'] == 'Fallecido'].shape[0]

canti_recuperados = data.query('Recuperado == "Recuperado"').shape[0]
cantidad_casos = data.shape[0]

tasa_mortalidad = canti_muertes / cantidad_casos * 100

tasa_recuperacion = canti_recuperados / cantidad_casos * 100

# 23. 

canti_muertes_departamento = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()

canti_recuperados_departamento = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
cantidad_casos = data.groupby('Nombre departamento').size()

tasa_mortalidad = canti_muertes_departamento / cantidad_casos * 100

tasa_recuperacion = canti_recuperados_departamento / cantidad_casos * 100

data2 = pd.DataFrame({'tasa_mortalidad_dep': tasa_mortalidad, 'tasa_recuperacion_dep': tasa_recuperacion})

# 24.

canti_muertes_ciudad = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()

canti_recuperados_ciudad = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()

canti_casos_ciudad = data.groupby('Nombre municipio').size()

mortalidad_ciudad = canti_muertes_ciudad / canti_casos_ciudad * 100

recuperacion_ciudad = canti_recuperados_ciudad / canti_casos_ciudad * 100

data3 = pd.DataFrame({'tasa_mortalidad_ciu': mortalidad_ciudad, 'tasa_recuperacion_ciu': recuperacion_ciudad})

# 25.

data.groupby(['Nombre municipio', 'Ubicación del caso']).size()

# 26. 

data.groupby(['Nombre municipio', 'Sexo'])['Edad'].mean()

# 27.

data[(data['Recuperado'] == 'Recuperado')].groupby('Fecha de diagnóstico').size().plot()

data[(data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()

# 28. 

aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre departamento').size()

aux.sort_values(ascending=False).head(10).plot()


aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre departamento').size()

aux.sort_values(ascending=False).head(10).plot()

# 29.

aux = data[(data['Estado'] == 'Fallecido')].groupby('Nombre municipio').size()

aux.sort_values(ascending=False).head(10).plot()


aux = data[(data['Recuperado'] == 'Recuperado')].groupby('Nombre municipio').size()

aux.sort_values(ascending=False).head(10).plot()

# 30.

aux = data[(data['Estado'] == 'Fallecido')].groupby('Edad').size()

aux.sort_values(ascending=False).head(10)

# 31.

data.groupby('Ubicación del caso').mean()

# 32.

data.groupby('Ubicación del caso').size().plot(kind='bar')

# 33.

data.groupby('Sexo').size().plot(kind='bar')

# 34.

data.groupby('Tipo de contagio').size().plot(kind='bar')





