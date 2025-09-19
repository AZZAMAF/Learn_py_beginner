# Function with input argument

def fungsi(): # defination // Name function(Paramater/input)
    # Body function
    keu ='welcome \n'
fungsi()


def Hello(name):
    print(f'Welcome to the world {name}')

Hello('ucup')

# Program tambah

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f'{angka1} + {angka2} = {hasil}')

tambah(1,2)

def sayHai(list_peserta):
    dataPeserta = list_peserta.copy() # copy tidak merubah data di luar fungsi
    for peserta in dataPeserta:
        print(f'Yang Terhormat {peserta}')

anggota =['ucup','agus','rudi']

sayHai(anggota)