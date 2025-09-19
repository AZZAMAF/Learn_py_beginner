def hello(nama = 'kamu'):

    print(f'hallo {nama}')

hello('azzam')
hello()

def sapaei(pesan ='Apa Kabar', nama = 'siapa'):
    print(f'Hai {nama}, {pesan}')

sapaei('Hai ganteng','dudung')
sapaei('Otong')

def Pangkat(angka,pangkat):
    hasil = angka **pangkat
    return hasil
print(Pangkat(2,4))

hasil = Pangkat(pangkat=2,angka=3)
print(hasil)

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))