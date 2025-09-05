#Oprasi Bilangan Aritmatika

a = 10
b = 10

#Pertambahan
hasil = a + b 


#Perkalian
hasil = a * b
print(a,"*", b, hasil)

#Pembagian
hasil = a / b
print(a,"/", b, hasil)

#Exsponen / pangkat
hasil = a ** b
print(a,"**", b, hasil)

#modulus / sisa pembagian
hasil = a % b
print(a,"%", b, hasil)

#floor division / kebalikan dari modulus
hasil = a // b
print(a,"//", b, hasil)

#Prioritas Oprasi, Oprationa Precedence

x = 3
y = 2
z = 4

hasil = y ** z * 9 + x % y
print(hasil)
