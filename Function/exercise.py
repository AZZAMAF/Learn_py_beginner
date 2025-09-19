import os


# Menghintung luas dan keliling persegi panjang

'''
# Header
os.system('clear')

print(f"{'Menghitung Luas':^40}")
print(f"{'Dan Keliling Persegi Panjang':^40}")
print(f"{'-'*40:^40}")

# TAke user Input
LEBAR =int(input('Masukan Nilai Lebar :'))
PANJANG =int(input('Masukan Nilai Panjang :'))

# Menghitung Luas
LUAS = PANJANG*LEBAR
KELILING = 2*(PANJANG+LEBAR)

#OUTPUT
print(f'Hasil Perhitungan Luas = {LUAS}')
print(f'Hasil Perhitungan Keliling = {KELILING}')
'''
def header():
    # Header
    os.system('clear')

    print(f"{'Menghitung Luas':^40}")
    print(f"{'Dan Keliling Persegi Panjang':^40}")
    print(f"{'-'*40:^40}") 

def inputUser():
    # TAke user Input
    LEBAR =int(input('Masukan Nilai Lebar :'))
    PANJANG =int(input('Masukan Nilai Panjang :'))
    return LEBAR,PANJANG

def hitungLuas(LEBAR,PANJANG):
    # Menghitung Luas
    return LEBAR*PANJANG
def hitungKeliling(Lebar,Panjang):
    # fungsi keliling
    return 2*(Lebar+Panjang)    

def display(massage, value):
    print(f'Hasil Perhitungan {massage} = {value}')  
while True:
    header() 

    Lebar, Panjang = inputUser()
    list_Option = ['1 = Luas','2 = Keliling','3 = Luas & Keliling']

    for index,list in enumerate(list_Option):
        print(f'{list_Option[index]}')
    Option = input('\nWhat u wanna do ? ') 

    if Option == '1':
        LUAS = hitungLuas(Lebar,Panjang)
        print('INI adalah Luas : ', LUAS)
    elif Option == '2':
        KELILING =hitungKeliling(Lebar,Panjang)
        print('This is Keliling :', KELILING)     
    elif Option == '3':
        LUAS = hitungLuas(Lebar,Panjang)
        KELILING =hitungKeliling(Lebar,Panjang)
        LUAS = hitungLuas(Lebar,Panjang)
        KELILING =hitungKeliling(Lebar,Panjang)

        #OUTPUT
        display('Luas = ', LUAS)
        print('Keliling = ', KELILING)
    else :
        print('\nyang bener aja lu?')
        print('ULANG LAGI SONO !!\n')

    isContinue = input('Apakah Lanjut (y/n)? ')   
    if isContinue == 'n':
        print('The Program Finish')
        break

print('Program Selesai')

