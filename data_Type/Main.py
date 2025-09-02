#Tipe data : Angka yang tidak memiliki koma (Integer)
data_integer = 1
print("data:", data_integer, ",bertipe:", type(data_integer))

#Tipe data: angka dengan koma (Float)
data_float = 1.5
print("data:", data_float, ",bertipe:", type(data_float))

#Tipe data : String = kumpulan karakter
data_String = "ucup"
print("data:", data_String, ",bertipe:", type(data_String))

#Tipe data : Bolean = True/False
data_bool = True
print("data:", data_bool, ",bertipe:", type(data_bool))



#TIPE DATA KHUSUS

#Tipe data : Komplex
data_complex = complex(5,6)
print("data:", data_complex, ",bertipe:", type(data_complex))

#Tipe data : Dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data:", data_c_double, ",bertipe:", type(data_c_double) )
