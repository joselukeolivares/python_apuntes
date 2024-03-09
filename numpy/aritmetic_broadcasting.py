#BASIC OPERATIONS USING ARITHMETIC SYMBOLS AND FUNCTIONS
import numpy as np

#Element-wise arithmetic operations on 1-D arrays
# We create two rank 1 ndarrays
x=np.array([1,2,3,4])
y=np.array([5.5,6.5,7.5,8.5])


print()
print("x = ",x)
print()
print("y = ",y)
print()

# We perfrom basic element-wise operations using arithmetic symbols and functions
print( "x+ y = ", x + y)
print("x+ y = ", np.add(x,y))
print()

print('x - y = ',x-y)
print('subtract(x,y)=', np.subtract(x,y))
print()

print('x * y = ',x*y)
print('multiply(x,y)=', np.multiply(x,y))
print()

print('x / y = ',x/y)
print('divide(x,y)=', np.divide(x,y))
print()

#Element-wise arithmetic operations on a 2-D array (Same shape)
x=np.array([1,2,3,4]).reshape(2,2)
y=np.array([5.5,6.5,7.5,8.5]).reshape(2,2)
print()
print("x = ",x)
print()
print("y = ",y)
print()

print( "x+ y = ", x + y)
print("x+ y = ", np.add(x,y))
print()

print('x - y = ',x-y)
print('subtract(x,y)=', np.subtract(x,y))
print()

print('x * y = ',x*y)
print('multiply(x,y)=', np.multiply(x,y))
print()

print('x / y = ',x/y)
print('divide(x,y)=', np.divide(x,y))
print()

#Additional mathematical functions
x = np.array([1,2,3,4])
print("x = ",x)
print()

# We apply different mathematical functions to all elements of x
print('EXP(x) = ',np.exp(x))
print()
print('SQRT(x) = ', np.sqrt(x))
print()
print('POW(x,2) = ',np.power(x,2))

# Statistical functions
# We create a 2 x 2  ndarray
x=np.array([[1,2],[3,4]])

print()
print('x = \n', x)
print()

print('Promedio de todos los elementos: ',x.mean())
print('Promedio de todos los elementos en las columnas de x: ',x.mean(axis=0))
print('Promedio de todos los elementos en los renglones de x: ',x.mean(axis=1))
print()
print('Suma de todos los elementos: ',x.sum())
print('Suma de todos los elementos en las columnas de x: ',x.sum(axis=0))
print('Suma de todos los elementos en los renglones de x: ',x.sum(axis=1))
print()
print('Desviacion Estandar de todos los elementos: ',x.std())
print('Desviacion Estandar de todos los elementos en las columnas de x: ',x.std(axis=0))
print('Desviacion Estandar de todos los elementos en los renglones de x: ',x.std(axis=1))
print()
print('Maximo de todos los elementos: ',x.max())
print('Maximo de de todos los elementos en las columnas de x: ',x.max(axis=0))
print('Maximo de de todos los elementos en los renglones de x: ',x.max(axis=1))
print()
print('Minimo de todos los elementos: ',x.min())
print('Minimo de de todos los elementos en las columnas de x: ',x.min(axis=0))
print('Minimo de de todos los elementos en los renglones de x: ',x.min(axis=1))
print()

#Change value of all elements of an array
x=np.array([[1,2],[3,4]])

print()
print('x = \n',x)
print()

print('3 *x=\n',3*x)
print()
print('3 -x=\n',3-x)
print()
print('3 +x=\n',3+x)
print()
print('3 /x=\n',3/x)
print()

#Arithmetic operations on 2-D arrays (Compatible shape)
x=np.array([1,2,3])
y=np.array([[1,2,3],[4,5,6],[7,8,9]])
z=np.array([1,2,3]).reshape(3,1)

print()
print('x =\n',x)
print()
print('y =\n',y)
print()
print('z =\n',z)
print()

print(' x + y=\n',x+y)
print()
print(' z + y=\n',z+y)
print()