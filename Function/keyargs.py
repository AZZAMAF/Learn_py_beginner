# key args = key argument

def fungsi(nama,tinggi,berat):
    print(f'{nama}, puya tingi{tinggi}, beranye{berat}')

fungsi('ucup',12,12)

def fungsi(**kwargs):
    # fungsi keyargs
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f'{nama}, puya tingi{tinggi}, beranye{berat}')

fungsi(nama ='ucup',tinggi =12,berat =12) # {'nama': 'ucup', 'tinggi': 12, 'berat': 12} # dictionary

# study case

def math(*args, **kwargs):
    output =0
    if kwargs['Option'] == "tambah":
        for angka in args:
            output += angka
    elif kwargs['Option'] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print('dahan')
    return output

print('='*10,'\n')
hasil = math(1,2,3,4,5,6,7,8,9, Option ="tambah")
print(f'Hasil Jumlah {hasil}')

hasil = math(1,2,3,Option ="kali")
print(f'Hasil Kali {hasil}')