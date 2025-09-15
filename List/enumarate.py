# Looping List and enumarate

#for loop
print('\n====== for loop =======\n')
kumpulanAngka = [4,3,2,5,6,1]

for angka in kumpulanAngka:
    print(f'ini adalah angka: {angka}')

peserta = ['otong', 'dadang', 'agus']

for nama in peserta:
    print(f'nama Peserta : {nama}')

# for loop and range
print('\n====== for loop and range\n')

kumpulanAngka = [10,5,4,2,6,5]
panjang = len(kumpulanAngka)

for i in range(panjang):
    print(f' angka = {kumpulanAngka[i]}')

# While 
print('\n====== While ====\n')

kumpulanAngka = [10,5,4,2,6,5]
panjang = len(kumpulanAngka)
i = 0
while i < panjang :
    print(f' angka : {kumpulanAngka[i]}')
    i += 1

# List Comprehension
print('\n =====  List Comprehension ====')

data = ['ucup',1,2,3,'otong']
[print(f' data = {i}') for i in data ]


# tambahan
Angka = [10,5,4,2,6,5]

angkaKuadrat = [i**3 for i in Angka ]
print(f' angka Kuadrat{angkaKuadrat}')






# === Enumarate = mengambil index dan data
print('\n =====  Enumarate ====')

data_list = ['ucup',1,2,3,'otong']

for index,data in enumerate(data_list):
    print(f' index = {index}, data = {data}')
