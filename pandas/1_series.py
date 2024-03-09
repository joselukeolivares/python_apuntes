import pandas as pd
import numpy as np

#1.1. Creamos una serie de pandas
groceries=pd.Series(data=[30,6,'Yes','NO'],index=['eggs','apples','milk','bread'])
print(groceries)

"""
eggs       30
apples      6
milk      Yes
bread      NO
dtype: object
"""

#1.2. Atrobutos: shape,ndim y size
print('Groceries tiene forma (shape): ',groceries.shape)
print('Groceries tiene dimension (shape): ',groceries.ndim)
print('Groceries tiene un total: ',groceries.size, ' elementos')

#1.3. Indices y datos de groceries
print('Los datos en Groceries : ',groceries.values)
print('Los indices en Groceries : ',groceries.index)

#1.4. Verificar si el indice esta dispoble en la serie
x='bananas' in groceries
y='bread' in groceries

print('bananas esta como indice en groceries: ',x)
print('bread esta como indice en groceries: ',y)

#2.1 Accediendo a los elementos con indices de etiqueta
#Indice de etiqueta sencillo
print("Cuantos huevos hay: \n", groceries['eggs'])
print()

#Indice de etiqueta multiple
print("Hay leche y pan la serie:\n ",groceries[['milk','bread']])
print()
#Usamos loc (location) para acceder a multiples indices de etiqueta
print('Cuantos huevos y manzanas hay:\n',groceries.loc[['eggs','apples']])
print()
#Acceder a los elementos usando indices numericos
print('Cuantos huevos y manzanas hay:\n',groceries.iloc[[0,1]])
print()
#Accedemos al ultimo elemento
print("Necesitamos pan: ",groceries.iloc[[-1]])
print()

#2.2 Mutacion de elementos usando indices de etiquetas
print("Lista original:\n",groceries)
print()
#Actualizamos el numero de huevos
groceries['eggs']=2
print()
#Lista modificada
print("Lista modificada:\n",groceries)

#2.3 Elemimando elementos usando la funcion drop
print("Lista original:\n",groceries)
print()

#Eliminamos las manzanas de la lista, pero no de la orginal
print('Eliminamos las manzanas de la lista:\n ',groceries.drop('apples'))

#Para eliminar los elementos de la lista y actulizarla la original con inplace
print('Eliminamos las manzanas de la lista:\n ',groceries.drop('apples', inplace=True))

print("Lista original:\n",groceries)
print()


#3.0 Creamos una serie con pandas que almacene frutas
fruits=pd.Series(data=[10,6,3],index=['apples','oranges','bananas'])
print(fruits)

#3.1 Operaciones aritmeticas basicas
print()
print("fruits + 2:\n",fruits+2)#Añadimos dos a cada elemento en la lista
print()
print("fruits - 2:\n",fruits-2)#Restamos dos a cada elemento en la lista
print()
print("fruits * 2:\n",fruits*2)#Multiplicamos por dos a cada elemento en la lista
print()
print("fruits / 2:\n",fruits/2)#Dividimos entre dos a cada elemento en la lista

#3.2 Funciones matematicas de NumPy para operar en Series
print("Lista original de frutas: \n",fruits)
print()
print("EXP(X) = \n",np.exp(fruits))
print()
print("SQRT(X) = \n",np.sqrt(fruits))
print()
print("POW(X) = \n",np.power(fruits,2))#Todos los elementos en frutas son elevados a 2
print()

#3.3 Operaciones aritmeticas en elementos seleccionados
print("Lista original de frutas: \n",fruits)
print()
print("Bananas + 2 = \n",fruits['bananas']+2)
print()
print("Manzanas - 2 = \n",fruits.iloc[0]-2)
print()
print("Duplicamos el numero de manzanas y naranjas = \n",fruits.loc[['apples','oranges']]*2)
print()
print("Dividimos a la mitad el numero de manzanas y naranjas = \n",fruits.loc[['apples','oranges']]/2)
print()





