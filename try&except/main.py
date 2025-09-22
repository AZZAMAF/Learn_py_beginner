# execption akan terjadi saat program
# menglami error saat runtime error

# contoh sederhana untuk menangkap exception
'''
input_user = int(input("masukan angka :"))
hasil = None


try:
    hasil = 10/input_user
except:
    print('input tidak boleh 0')

print(f'hasil = {hasil}')
'''

# contoh di aplikasi

while(True):
    angka =   int(input('masukan angka pembagai:'))
    try:
        hasil = 10/angka
        print(f'Hasil = {hasil}')
        isDone = input('lanjutkan y/n?')
        if isDone == 'n':
            break

    except:
        print('Pembagai nol, silahkan masukan input lagi')

print('last program')

# contoh aplikasi untuk membuat file data.txt

try:
    with open('data.txt','r') as file:
            print(file.read())
        
except:
    print('file data.txt tidak ditemukan, membuat file baru')
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('file baru')

print('last program 1')

