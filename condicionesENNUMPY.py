import numpy as np  # importamos la libreria numpy
arr = np.linspace ( 1, 10, 10, dtype= "int8")
print(arr)
indices_con = arr > 5
print(indices_con)
print(arr[indices_con]) #imprime los elementos que superen el valor 5
print(arr[arr > 5&(arr<9)])
arr[arr>5]=99
print(arr)
