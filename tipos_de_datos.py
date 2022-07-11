import numpy as np

array = np.array([1,2,3,4])
print(array.dtype ) #Devuelve el tipo de dato

#Indicando el tipo de datos que contiene el array
array = np.array([1,2,3,4], dtype = 'float64')
print(array.dtype )
print(array)

#Cambiando el tipo de datos de un array existente
array.astype(np.int64) #directamente desde la libreria 

