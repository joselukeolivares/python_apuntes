import numpy

#Crear un arreglo con ceros segun la forma especificada en parametros
x=numpy.zeros((3,4))
print()
print('x= \n', x)

#Información acerca de x
#Dimensiones
print('x has dimensions: ', x.shape)
#Tipo
print('x has an object type: ', type(x))
#Los elementos en x son del tipo
print('The elements in x are of type: ', x.dtype)

#Crear un arreglo con unos segun la forma especificada en parametros
x=numpy.ones((3,4))
print()
print('x= \n', x)

#Información acerca de x
#Dimensiones
print('x has dimensions: ', x.shape)
#Tipo
print('x has an object type: ', type(x))
#Los elementos en x son del tipo
print('The elements in x are of type: ', x.dtype)

#Crear un arreglo con una constante segun la forma especificada en parametros
#Podemos especificar el tipo de dato con la palabra dtype
x=numpy.full((3,4),5)
#x=numpy.full((3,4),5,dtype=float64)
print()
print('x= \n', x)

#Información acerca de x
#Dimensiones
print('x has dimensions: ', x.shape)
#Tipo
print('x has an object type: ', type(x))
#Los elementos en x son del tipo
print('The elements in x are of type: ', x.dtype)

#Crear un arreglo con 1 en la diagonal y ceros en el resto de los espacios del arreglo
x=numpy.eye(5)
#x=numpy.full((3,4),5,dtype=float64)
print()
print('x= \n', x)

#Información acerca de x
#Dimensiones
print('x has dimensions: ', x.shape)
#Tipo
print('x has an object type: ', type(x))
#Los elementos en x son del tipo
print('The elements in x are of type: ', x.dtype)

#Crear un arreglo especificando  los numeros en la diagonal 
x=numpy.diag([10,20,30,40,50])
#x=numpy.full((3,4),5,dtype=float64)
print()
print('x= \n', x)

#Información acerca de x
#Dimensiones
print('x has dimensions: ', x.shape)
#Tipo
print('x has an object type: ', type(x))
#Los elementos en x son del tipo
print('The elements in x are of type: ', x.dtype)

#Crear un arreglo con valores secuenciales
x=numpy.arange(10)
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

#Crear un arreglo con valores secuenciales
#especificando el inicio (inluyente) y fin (excluyente)
x=numpy.arange(4,10)
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

#Crear un arreglo con valores secuenciales
#especificando el inicio (inluyente), fin (excluyente) e intervalos
x=numpy.arange(1,14,3)
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

#Crear un arreglo con N valores espaciados entre el valor de inicio y fin
#especificando el inicio (inluyente), fin (incluyente), número de valores en el array
x=numpy.linspace(0,25,10)
#Excluir el ultimo numero: fin (excluyente)
#x = np.linspace(0,25,10, endpoint = False) 
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

# a)Crear un arreglo con un rango de  valores  
# b)Convertir la forma de un arreglo a una nueva forma

#a)
x=numpy.arange(20) 
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

#b)
y=numpy.reshape(x,(4,5)) 
print()
print('y = ',y)
print()
print('y has dimensions; ',y.shape)
print('tx is an object of type: ',type(y))
print('The elements in x are of type',y.dtype)

#Crear un arreglo de 3X3 con valores flotantes aleatorios 
x=numpy.random.random((3,3))
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

#Crear un arreglo de 3X3 con valores enteros aleatorios dentro del intervalo (inicio y fin)
#especificando el inicio (excluyente), fin (excluyente) y forma del arreglo
x=numpy.random.randint(4,15,size=(3,2))
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)

#Crear un arreglo de 1000X1000 de numeros aleatorios de tipo flotante con
# distribución normal (gaussian) con media de 0 y desviacion estandar de 0.1
x=numpy.random.normal(0,0.1,size=(1000,1000))
print()
print('x = ',x)
print()
print('x has dimensions; ',x.shape)
print('tx is an object of type: ',type(x))
print('The elements in x are of type',x.dtype)
print('The elements in x have a mean of: ',x.mean)
print('The maximum value  in x is: ',x.max())
print('The minimum value  in x is: ',x.min())
print('x has ',(x<0).sum(),'negative numbers')
print('x has ',(x>0).sum(),'positive numbers')




