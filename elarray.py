import numpy as np

lista = [1,2,3,4,5,6,7,8,9]
#print(lista)

### change from list to numpy array ###

arr = np.array(lista)
#print(arr)

###check type of the array###

#print(type(arr))

### create a matrix ###

matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix=np.array(matrix)
#print(matrix)

### indexing time ###

#print(arr[1])
#print(arr[0]+arr[5])
#print(matrix)
#print(matrix[0])

#print(matrix[1])
#print(matrix[2])
#print(matrix[3])
#print(matrix[0,2])

### indexing by pieces ###

#print(arr[:6])
#print(arr[2:])

print(arr[::3])

print(arr[-1])
print(arr[-3:])
print(matrix)

print(matrix[1:])

print(matrix[1:,0:2])

