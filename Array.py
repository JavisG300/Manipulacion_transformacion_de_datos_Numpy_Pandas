import numpy as np
#Definiendo una lista
lista = [1,2,3,4,5,6,7,8,9]
print(lista)

#Convirtiendo la lista en un array
array = np.array(lista)
print(array, type(array))

#Definiendo una matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)

#Indexado
#Se puede operar entre valores del arreglo
sum_array = array[1] + array [4]
print(f'La suma del indice 1 y 4 es: {sum_array}')

#La matriz tiene índices, los de siempre
matriz_02 = matriz[0,2]
print(f'El elemento 0,2 de la matriz es: {matriz_02}')