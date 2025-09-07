#Oprasi Bitwsie = Operasi Biner/ Binery
# Bitwise / masing2 bit


a = 9 
b = 5

#Bitwise
c = a| b
print("\n =========OR========")
print('Nilai :',a,'binary',format(a,'08b'))
print('Nilai :',b,'binary',format(b,'08b'))
print('---------------------------(|)')
print('Nilai :',c,'binary',format(c,'08b'))

#Bitwise AND (&)
c = a & b
print("\n =========AND========")
print('Nilai :',a,'binary',format(a,'08b'))
print('Nilai :',b,'binary',format(b,'08b'))
print('---------------------------(&)')
print('Nilai :',c,'binary',format(c,'08b'))

#Bitwise XOR (^)
c = a^ b
print("\n =========XOR========")
print('Nilai :',a,'binary',format(a,'08b'))
print('Nilai :',b,'binary',format(b,'08b'))
print('---------------------------(^)')
print('Nilai :',c,'binary',format(c,'08b'))

#Bitwise NOT (^)
c = ~a 
print("\n =========NOT========")
print('Nilai :',a,'binary',format(a,'08b'))
print('---------------------------(~)')
print('Nilai :',c,'binary',format(c,'08b'))
