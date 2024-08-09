import numpy as np


scalar = np.array(42)
print(scalar)
print(scalar.ndim)

#cero dimensiones 
vector = np.array([1, 2, 3])
print(vector)
print(vector.ndim)
#Dos dimensiones

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)  #imprime la matriz
print(matriz.ndim)

#Mas de  dimensiones
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(tensor)
print(tensor.ndim)

#agregar o eliminar dimensiones
vector = np.array([1, 2, 3, 4], ndmin=10)
print(vector)
print(vector.ndim)

#expandir dimensiones
expand = np.expand_dims(np.array([1, 2, 3, 4]), axis=0)
print(expand)
print(expand.ndim)

#eliminar dimensiones que no stas usando
print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector.ndim)



