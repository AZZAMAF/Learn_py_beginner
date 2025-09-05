#Komparasi = mebandingkan 2 nilai
# every output komparasi is bolean
#>, <, >=, <=, ==, !=, is, is not

a = 12
b = 3

print( a < b)
print( b < a)

print (a == b)

# 'IS' Sebagai komparasi Object Indentfy

x = 5 # asigment make object
y = 5 # jadi hex id akan di masukan di memory yang sama

print('nilai x =', x,'id:', hex(id(x)))
print('nilai y =', y,'id:', hex(id(y)))

hasil = x is y
print(hasil)


x = 6
y = 4


print('nilai x =', x,'id:', hex(id(x)))
print('nilai y =', y,'id:', hex(id(y)))

hasil = x is not y
print(hasil)