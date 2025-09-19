#Variabel = tempat menyimpan data

Umur = 12
Nama = "azzam"

print(str(Umur) + Nama)

if Umur <=18 :
    print("Dewasa")
else :
    print("bocil")



# Casting
#Casting dalam pemrograman artinya mengubah tipe data satu nilai ke tipe data lain.
#👉 Jadi casting itu ibaratnya “menyamakan bahasa” antara tipe data.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)
print(x)

anka_int = "20"
angka_int = int(anka_int) # ubah string "20" jadi angka 20
print(Umur + angka_int)      # hasil: 32
"""
int() → jadi bilangan bulat
float() → jadi bilangan desimal
str() → jadi teks
bool() → jadi True/False
"""

#Get the Type
#Fungsinya untuk mengecek tipe data dari suatu variabel.
print(type(Umur))

#Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

print(x)

#Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a

print(A, a)