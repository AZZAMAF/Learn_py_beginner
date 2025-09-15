data_angka = [1,2,3,4,5,3,5,7,9,0,7,5,3,5,0,1,3,3,4]

print(f'data angka = \n {data_angka}')

#Count Data
jumlah_data_4 =  data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f'Jumlah angka 4 = {jumlah_data_4}')
print(f'Jumlah angka 3 = {jumlah_data_3}')

# Ambil Posisi data (index)
data = ['Ucup', ' Otong', 'Dudung', 'Ujang']
print(f"data ={data}")

index_dudung = data.index('Dudung')
index_Ujang= data.index('Ujang')
print(f'Index si dudung : {index_dudung}')
print(f'Index si Ujang : {index_Ujang}')

# Mengurutkan list
print(f'data angka sebelum di sort \n {data_angka}')
data_angka.sort()
print(f'data angka sort = \n {data_angka}')

print(f'data = {data}')
data.sort()
print(f'data sort = {data}')

# Balik List coy
data_angka.reverse()
print(f'Data angka di balik lagi coy : {data_angka}')
