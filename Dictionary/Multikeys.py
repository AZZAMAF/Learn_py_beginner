import datetime

mahasiswa1 ={
    'nama' : 'Ucup santos',
    'nim'  : '1235234556',
    'sks_lulus' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2021, 4, 10)
}

mahasiswa2 ={
    'nama' : 'totong santos',
    'nim'  : '1235234556',
    'sks_lulus' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2022, 10, 10)
}

mahasiswa3 ={
    'nama' : 'ASep santos',
    'nim'  : '1235234556',
    'sks_lulus' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(1919, 4, 10)
}

data_mahasiswa = {
    'MAHH001' : mahasiswa1,
    'MAHHOO2' : mahasiswa2,
    'MAHH003' : mahasiswa3,

}

print(f"{'KEY':<6}{'NAMA':<17}{'sks':<8}{'Beasiswa':<9}{'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM  = data_mahasiswa[KEY]['nim']
    SKS  = data_mahasiswa[KEY]['sks_lulus']  
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR   =  data_mahasiswa[KEY]['lahir'].strftime("%x") 

    print(f"{KEY:<6}{NAMA:<17}{SKS:<8}{BEASISWA:<9}{LAHIR:<10}")


