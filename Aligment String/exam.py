# Date and time (Latihan)

import datetime as dt

print("Silahkan Masukan Tanggal, \n Bulan dan tahun lahir anda.")
tanggal = int (input ("Tanggal \t: "))
bulan =int ( input ("Bulan \t\t : "))
tahun = int ( input ("Tahun \t\t :" ))

tanggal_lahir = dt.date(tahun, bulan, tanggal)

print(f"Tanggal lahir anda adalah : ",tanggal_lahir)
print(f"Hari nya Adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")

umur_Hari = hari_ini - tanggal_lahir
Umur_Tahun = umur_Hari.days // 365
umur_bulan_sisa = (umur_Hari.days % 365) // 30
print(f"Umur Anda : {Umur_Tahun} Tahun, {umur_bulan_sisa} Bulan")


print(f"dd {hari_ini:%d}")



