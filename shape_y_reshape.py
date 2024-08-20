import numpy as np

#generamos numeros aleatorios entre 1 y 9 con una estructura de 3x2
arr = np.random.randint(1,10,(3,2))
#arr = np.reshape(arr,(2,3))
print("forma original:", arr.shape) # imprime la forma original del arreglo
print(arr)
# cambiamos la forma del arreglo a una forma de (1,6)
arr_reshape = arr.reshape((1,6))
#imprimimos el arreglo despues del cambio de forma
print("arreglo despues  reshape:", arr_reshape)
