import pandas as pd
# Manejando NaN en DataFrame
#1.1 Creamos DataFrame
#Creamos una lista de diccionarios de python
items2=[{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

#Creamos el DataFrame y proporcionamos los indices de los renglones
store_items=pd.DataFrame(items2,index=['store 1','store 2','store 3'])
print(store_items)
print()
#1.2 Contamos el total de los valores NaN
x=store_items.isnull().sum().sum()
print(x)
# el metodo .isnull() regresa un DataFrame de las mismas dimensiones, indicando True donde hay Nan y False con elementos que no lo son
# Usamemos el metodo .sum() para contar los True, pero lo usamos dos veces por que el primero
# cuenta los True por columna, el seundo suma el conteo de las columnas

#1.3 Contamos el total de valores no-NaN
print()
print("Elnumero de valores no-Nan en las columnas del DataFrame: \n",store_items.count())
print()

#1.4 Eliminamos renglones con valores NaN
store_items.dropna(axis=0)
#1.5 Eliminamos columnas con valores NaN
store_items.dropna(axis=1)
#El metdo .dropna() no modifica el DataFrame original, para ello debemos utilizar la palabra reservada .dropna(inplace=true)


#Sustituyendo valores NaN
#1.6 Reemplazando valores NaN con 0
store_items.fillna(0)

#1.7 Llenado hacia adelante (forward)
#Reemplaza valores NaN, con el valor previo en la misma columna
store_items.fillna(method='ffill',axis=0)

#1.8 Llenado hacia adelante (forward)
#Reemplaza valores NaN, con el valor previo en el mismo renglon
store_items.fillna(method='ffill',axis=1)

#1.9 Llenado hacia adelante (backward)
#Reemplaza valores NaN, con el valor siguiente en la misma columna
store_items.fillna(method='ffill',axis=0)

#1.10 Llenado hacia adelante (backward)
#Reemplaza valores NaN, con el valor siguiente en el mismo renglon
store_items.fillna(method='ffill',axis=1)

#1.11 Interporlación (estimada) NaN values down (axis=0)
store_items.interpolate(method='linear',axis=0)

#1.12 Interporlación (estimada) NaN values across (axis=1)
store_items.interpolate(method='linear',axis=1)



