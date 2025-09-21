import numpy as np

listA = [1,2,3,4]
vectorA = np.array([1,2,3,4])

print(listA) # Tidak bisa menggunakan pangkat **
print(vectorA**2) # bisa coyy 

matrixB = np.array([(1,2,),(3,4)])
print(f'\n Matrix B =\n {matrixB}')
print(f'\n Matrix B =\n {matrixB**2}')

zeroC = np.zeros((2,2))
print(f'\nZeros = \n{zeroC}')

oneD = np.ones((2,2))
print(f'\n Ones = \n{oneD}')

