data_0 =[1,2]
data_1 =[3,4]

data_2d =[data_0,data_1, 10]
data_2d_copy = data_2d.copy()

print(f'data = {data_2d}')
print(f'data_copy = {data_2d_copy}')

# mengambil data dari nested list

data = data_2d[0][0]
print(f'data : {data}')

# all adrees
print(f'Adrees data_2d {hex(id(data_2d))}')
print(f'Adrees data_copy {hex(id(data_2d_copy))}')

print('Adreeas member 01 ')
print(f'address asli = {hex(id(data_2d[0]))}')
print(f'addres copy ={hex(id(data_2d_copy[0]))}')

data_2d[0][0] = 5
data_2d[2] = 9
print(f'data = {data_2d}')
print(f'data_copy = {data_2d_copy}')

# kita harus melakukan deep copy agar ke copy semuanya sampe ke addres2nya
# karena kalau make .copy( doan itu hanya list nya saja yang di copy jadi gak sampe ke addresnya )
print('===== Deep copy ====')
from copy import deepcopy

data_2d =[data_0,data_1, 10]
data_2d_deepcopy = deepcopy(data_2d)


print(f'address asli = {hex(id(data_2d[0]))}')
print(f'addres deep copy ={hex(id(data_2d_deepcopy[0]))}')

print('\n Adreeas member 01 ')
print(f'address asli = {hex(id(data_2d[0]))}')
print(f'addres copy ={hex(id(data_2d_copy[0]))}')

data_2d[0][0] = 30
print(f'data = {data_2d}')
print(f'data_copy = {data_2d_copy}')
print(f'data_deep = {data_2d_deepcopy}')