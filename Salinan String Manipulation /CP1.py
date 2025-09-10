#Operaasi dan  Manipulasi String

#1. Menyambung String (concatenate)

nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap,'\n')

#2. Menghitung String
panjang = len(nama_lengkap)
print('panjang dari ' + nama_lengkap + ' = '+ str(panjang),'\n')

# Operator for String
#Chek is ther CHAR or String in String

d = 'Ucup'
status = d in nama_lengkap
print("STRING\t" + d + " ada di " + nama_lengkap + " = " +str(status),'\n')

# Mengulang String
print("WK" *10)

# Indexing
print("index ke  0 :" + nama_lengkap[0])
print("index ke  0 :" + nama_lengkap[-8],'\n')

# : = Sampai
print("index ke  [0:5] :" + nama_lengkap[0:5])
print("index ke  [3:5]" + nama_lengkap[ 3:5])
print("index ke  [0:3:5]" + nama_lengkap[ 0:3:5],'\n')

# item paling kecil
print("item Paling Kecil : " +  min(nama_lengkap))
# Item Paling Besar
print("item Paling Besar  : " +  max(nama_lengkap))

ascii_code = ord("'")
print("Asci code for space is " + str(ascii_code))
data = 200
print("char untuk ASCII 117 is " + chr(data),'\n')

# Operator dalam bentuk Method
# data = object ===== # .count = method 
data = " Oton si rotonG "
jumlah = data.count("o")
print("jumlah o pada" + data + " = " + str(jumlah))

