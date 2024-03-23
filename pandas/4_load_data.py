import pandas as pd

#1.1 Cargar datos desde un archivo CSV
google_stock=pd.read_csv("./goog.csv")

print("google_stock es del tipo: ", type(google_stock))
print("google_stock tiene una forma: ",google_stock.shape)

#1.2 Obtener el DataFrame
print(google_stock)

#1.3 Obtener los primeros 5 renglones del DataFrame
print(google_stock.head())

#1.4 Obtener los ultimos 5 renglones del DataFrame
print(google_stock.tail())

#1.5 Revisar si alguna columna contiene NaN
print(google_stock.isnull().any())

#1.6 Ver las descripciones estadisticas del DataFrame
print(google_stock.describe())

#1.7 Ver las descripciones estadisticas del DataFrame de una columna especifica
print(google_stock['Adj Close'].describe())

#1.8 Operaciones estadisticas: Min,Max y la media
print()
print("Valor maximo en cada ecolumna", google_stock.max())
print("Valor minimo en 'Close' ", google_stock['Close'].min())
print("Valor promedio en cada ecolumna", google_stock.mean())

#1.9 Correlacion entre columnas
print(google_stock.corr())

#1.10 Metodo groupby()
data=pd.read_csv('./fake-company.csv')
#Se muestra el monto total de dinero gasta en salario por año
data.groupby(['Year'])['Salary'].sum()
#1.11 Se muestra el salario promedio por año
data.groupby(['Year'])['Salary'].mean()
#1.12 Se muestra el salario total de cada empleado por todos los años trabajados
data.groupby(['Name'])['Salary'].sum()
#1.13 Se muestra distribución de salario  por departamento por año
data.groupby(['Year','Department'])['Salary'].sum()



