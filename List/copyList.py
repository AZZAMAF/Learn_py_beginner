# teknik copy list

a = ['ucup','otong','ddung']
print(f'a = {a}')

b = a # pass by refrence 
print(f' b = {b}')

# kita akan merubah index dari a
# ini akan merubaah kedua List
a[1] = 'mikail'
b.sort()
print(f'a = {a}')
print(f' b = {b}')

# Address dari list A dan B
print(f' Adress a = {hex(id(a))}')
print(f' Adress b = {hex(id(b))}')

# Duplikat List dengan copy
print('membuat list c dengan a.copy()')
c = a.copy() # full duplicat or data baru

print(f' Adress a = {hex(id(a))}')
print(f' Adress b = {hex(id(b))}')
print(f' Adress c = {hex(id(c))}')

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(" Kita ubah data 0")
c[0] ='Dadang'

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(" Kita ubah data 0")
c[0] ='bandru'

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")