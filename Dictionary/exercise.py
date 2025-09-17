import datetime
import os
import string
import random

mahasiswa_Template ={
    'nama' : 'nama',
    'nim'  : '0000000',
    'sks_lulus' : 0,
    'lahir' :datetime.datetime(1111,1,11)
}

data_mahasiswa ={}

#os.system('cls') # for windows
while True:
    os.system("clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA DATANG':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_Template.keys())
    mahasiswa['nama']= input("Nama Mahasiswa:")
    mahasiswa['nim']= input("NIM Mahasiswa:")
    mahasiswa['sks_lulus']= int(input("SKS Kelulusan:"))
    TAHUN_LAHIR = int(input('Tahun Lahir (YYYY) :'))
    BULAN_LAHIR = int(input('Bulan lahir (1-12) :'))
    TANGGAL_LAHIR = int(input('Bulan lahir (1-31) :'))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6}{'NAMA':<17}{'sks':<8}{'Lahir':<10}")
    print("-"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM  = data_mahasiswa[KEY]['nim']
        SKS  = data_mahasiswa[KEY]['sks_lulus']  
        LAHIR   =  data_mahasiswa[KEY]['lahir'].strftime("%x") 

        print(f"{KEY:<6}{NAMA:<17}{SKS:<8}{LAHIR:<10}")

    print('\n')
    is_done = input('Sudah beres bro (y/n) ?')
    if is_done == 'n':
        break

print('Akhir dari program, Terimakasih')