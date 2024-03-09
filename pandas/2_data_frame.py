import pandas as pd

#1.0.Creamos un diccionario de Series de Pandas
items={
    'Bob': pd.Series(data=[245,25,55],index=['bike','pants','watch']),
    'Alice': pd.Series(data=[40,110,500,45],index=['book','glasses','bike','pants'])
}

#1.1. Creamos un DataFrame usando un diccionario de Series
shopping_carts=pd.DataFrame(items)

print(shopping_carts)

#1.2 DataFrame asigna indices numericos si no es especifican los indices
data={
    'Bob': pd.Series(data=[245,25,55]),
    'Alice': pd.Series(data=[40,110,500,45])
}

df=pd.DataFrame(data)
print(df)

#1.3. Atributos de DataFrame
print('shopping_carts tiene la forma: \n',shopping_carts.shape)
print('shopping_carts tiene la dimension: \n',shopping_carts.ndim)
print('shopping_carts tiene :\n',shopping_carts.size," elementos")
print()

print('Los datos en shopping_carts: \n',shopping_carts.values)
print()
print('Los indices en shopping_carts: \n',shopping_carts.index)
print()
print('Los indices de columna en shopping_carts: \n',shopping_carts.columns)

#1.4 Seleccionando especificamente renglones del DataFrame

sel_shopping_cart=pd.DataFrame(items,index=['pants','book'])
print(sel_shopping_cart)

#1.5 Seleccionando especificamente columnas del DataFrame
alice_sel_shopping_cart=pd.DataFrame(items,index=['glasses','bike'],columns=["Alice"])
print(alice_sel_shopping_cart)

#1.6 Creando un DataFrame usando un diccionario de listas
data={'Integers':[1,2,3],
      'Floats':[4.5,8.2,9.6]
      }
df=pd.DataFrame(data)
print(df)

#1.7 Creando un DataFrame usando un diccionario de listas, con indices customizados
data={'Integers':[1,2,3],
      'Floats':[4.5,8.2,9.6]
      }

df=pd.DataFrame(data,index=['label 1','label 2','label 3'])
print(df)

#1.8 Creando DataFrame usando lista de diccionarios
items2=[
    {'bikes':20,'pants':30,'watches':35},
    {'watches':10,'glasses':50,'bikes':15,'pants':5}
]

store_items=pd.DataFrame(items2)
print(store_items)

#1.9 Creando DataFrame usando lista de diccionarios, con indices customizados
items2=[
    {'bikes':20,'pants':30,'watches':35},
    {'watches':10,'glasses':50,'bikes':15,'pants':5}
]

store_items=pd.DataFrame(items2,index=['store 1','store 2'])
print(store_items)

#2.1 Accediendo a elementos usando etiquetas
print("Cuantas bicicletas hay en cada tienda, \n",store_items[['bikes']])
print()
print("Cuantas bicicletas y pantalones hay en cada tienda, \n",store_items[['bikes','pants']])
print()
print("Que objetos hay en la tienda 1, \n",store_items.loc[['store 1']])
print()
print("Cuantas bicicletas  hay en la tienda 2, \n",store_items['bikes']['store 2'])
print()

#2.2 Añadir una columna a un DataFrame existente
# Insertaremos 15 shirts en store 1 y 2 shorts en store 2
store_items['shirts']=[15,2]
print(store_items)

#2.3 Añadir columna en base a una operación aritmetica en columnas existentes en el DataFrame
store_items['suits']=store_items['pants']+store_items['shirts']
print(store_items)

#2.4 Crear una fila para añadir al DataFrame
#creamos un diccionario
new_items=[{'bikes':20,'pants':30,'watches':35,'glasses':4}]

#Cremoa un nuevo DataFrame con los elementos, y la etiqueta para el indice 'store 3'
new_store=pd.DataFrame(new_items,index=['store 3'])

#2.4.1 Utilizamos el metodo .append() para añadir la fila al DataFrame
store_items = store_items.append(new_store)
print(store_items)

#2.5 Añadir una columna con datos de columnas existentes
store_items['new watches']=store_items['watches'][1:]
print(store_items)

#2.6 Insertar una columna en una colación especifica
#Insertamos una nueva columna con la etiqueta 'shoes' antes de la columna con el indice 4
store_items.insert(4,'shoes',[8,5,4])
print(store_items)

#2.7 Eliminando una columna del DataFrame
#El metodo pop solo permite eliminar columnas
store_items.pop('new watches')

#2.8 eliminando multiples columnas del DataFrame
#El metodo drop elimina tanto columnas como renglones, especificando con la palabra reservada axis
store_items=store_items.drop(['watches','shoes'],axis=1)

print(store_items)

#2.9 Eliminando renglones del DataFrame
store_items=store_items.drop(['store 2','store 1'],axis=0)
print(store_items)

#2.10 Modificando la etiqueta de columna
store_items=store_items.rename(columns={'bikes':'hats'})
print(store_items)

#2.11 Modificando la etiqueta de renglon
store_items=store_items.rename(index={'store 3':'last store'})
print(store_items)

#2.12 Usar valores de columna existente como indice de renglon
store_items=store_items.set_index('pants')
print(store_items)