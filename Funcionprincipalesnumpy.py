import numpy as np
#definamos numero leatorios de 1 a 20 en un vector
arr = np.random.randint(1,20,10)
print (arr)
#ahora lo llevaremos a una estructura matricial
matriz = arr.reshape(2,5)
print(matriz)
#con max voy a traer el maximo
maximo = arr.max()
print(maximo)
maximo = matriz.max()
print(maximo)
#crearemos un arr de dos dimensiones
a = np.array([[1, 2], [4, 5]])
b = np.array([[7, 8]])

# que pasa cuando quieres unir el array a con el array b
#con el comando contenate se hara la union de ambos arrays por el eje 0 axis
c = np.concatenate((a,b), axis = 0)
print(c)