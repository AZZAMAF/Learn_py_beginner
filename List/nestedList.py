# Nested List
data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4,]
print(f'list biasa = {data_list_biasa}')

list_2 = [data_0, data_1]
print(f'data list 2d: {list_2}')

#ex:

peserta_01 = ['ucup', 12, 'pria']
peserta_02 = ['yanti', 12, 'wanita']
peserta_03 = ['', 12, 'pria']

all_peserta = [peserta_01, peserta_02, peserta_03]

print(f'Para Peserta : \n{all_peserta}\n')

for peserta in all_peserta:
    print(f'nama: {peserta[0]}')
    print(f'usia: {peserta[1]}')
    print(f'kelamin: {peserta[2]}\n')

# Problem with refrence

list_copy = all_peserta.copy()
print(f'Para Peserta : \n{list_copy}\n')
peserta_01[0] = 'mikel'
print(f'Para Peserta : \n{list_copy}\n')
print(f'Para Peserta : \n{all_peserta}\n')
#[['mikel', 12, 'pria'], ['yanti', 12, 'wanita'], ['', 12, 'pria']]
# jadinya ikut ke copy coy jadi masih di satu reference yang sama gitu harusnya kan beda
