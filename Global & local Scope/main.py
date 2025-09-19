# Global and local Scope

global_nama = "oton" # ini variabel Global

#Akses Variabel Global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {global_nama}")

fungsi()

# akses variabel global dalam Loop

for i in range(0,5):
    print(f'loop {i} - {global_nama}')

# Percabangan 
if True:
    print(f'if manampilka {global_nama}')

# VAriabel Local Scope
def fungsi2():
    nama_lokal ='Ucup' # Variabel Local Scope 

fungsi()
#print(nama_local) #k tidak bisa di jalankan karena vareiabel local 

#EX : 1 # akses Variable
def say_Otong():
    print(f'hallo {nama}')

nama = 'Otong'
say_Otong()

# Ex : 2 # change to global Variabel
angka = 0
nama ='ucup'

def ubah(nilai_baru, nama_baru):
    global angka # this fungsi get akses to change global angka
    global nama
    angka = nilai_baru
    nama = nama_baru

print(f'sebelum {angka, nama}')
ubah(10,'kevin')
print(f'sesudah {angka, 'kevin'}')

# Ex : 3
angka = 0
for i in range(0,5):
    angka +=1
    angka_dumy = 0
print(angka)
print(angka_dumy)

if True:
    angka = 10
    angka_dumy = 10

print(angka)
print(angka_dumy)