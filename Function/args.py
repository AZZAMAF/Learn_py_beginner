# args 

# memasukan data / argument
def fungsi(nama,tinggi,berat):
    print(f'{nama}, puya tingi{tinggi}, beranye{berat}')

fungsi('ucup',12,12)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama}, puya tingi{tinggi}, beranye{berat}')

fungsi(['ragil',123,290])

# args = argument
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama}, puya tingi{tinggi}, beranye{berat}')

fungsi('dudung',123,124)

# Study case

def tambah(*data):
    # data type is tuple, and can di iterasi 
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(hasil)

hasil = tambah(10,120)
print(hasil)