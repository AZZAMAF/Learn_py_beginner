#Lambda Function

def f_kuadrat(angka):
    return  angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

#Lambda
# output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f'hasil dari lambda {kuadrat(3)}')

pangkat = lambda num,pow : num**pow
print(f'hasil dari lambda {pangkat(3,4)}')

# kegunaan nya

# Sorting untuk list biasa
data_list = ['otong', 'dudung', 'akil']
data_list.sort()
print(f'sorted list = {data_list}')

# Sorting dia pkai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=len)
print(f'Sorted list by len = {data_list}')

# sort use lambda
data_list = ['otong', 'dudung', 'akil']
data_list.sort(key=lambda nama:len(nama))
print(f'Sorted list by len = {data_list}')

# filter
data_Angka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurang_dari_lima(angka):
    return angka < 5
data_Angka_baru = list(filter(kurang_dari_lima,data_Angka))
print(f'Hasilnya sama aja {data_Angka_baru} ini lebih ribet')

data_Angka_baru = list(filter(lambda x:x<5,data_Angka))
print(f'contoh {data_Angka_baru}')

# Kasus genap
data_genap =list(filter(lambda x:(x%2==0),data_Angka))
print('output dari data genap', data_genap)

# Kasus ganjil
data_ganjil =list(filter(lambda x:(x%2!=0),data_Angka))
print('output dari data ganjil', data_ganjil)

# kelipatan 3
data_3 =list(filter(lambda x:(x%3==0),data_Angka))
print('output dari data kelipatan 3', data_3)
