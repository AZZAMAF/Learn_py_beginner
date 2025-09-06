
"""
#Episode Latihan logika dan komparasi


#membuat gabungan area rentang dari angka
# ++++3----10+++++

inputUser = float(input ("masukan angka yang bernilai kurang dari 3 atau lebih besar dari sepuluh\n"))

#+++3------
#Memeriksa angka kurang dari 3
isKurangDari =  (inputUser < 3)
print('kurang dari 3',isKurangDari)

#--------10++++
isLebihDari = (inputUser > 10)
print('Lebih dari 10',isLebihDari)

#+++3-------10++++++
isCorrect = isKurangDari or isLebihDari
print('Angka Yang Anda Masukan:',isCorrect)

#-----3++++10------
#Kasus Irisan
inputUser = float(input ("\tmasukan angka yang bernilai kurang dari 3 atau lebih besar dari sepuluh\n"))

isLebihDari = (inputUser > 3)
print('Angka Lebih Dari 3',isLebihDari)

isKurangDari = (inputUser < 10)
print('Angka Kurang dari 10', isKurangDari)

isCorrect = (isLebihDari and isKurangDari)
print('Angka yang Anda masukan:',isCorrect)
"""
#Tugas

def inputUser1():
    input_Angka = float(input("InputNumber:"))
    limaNol = (input_Angka > 0 and input_Angka < 5) 
    # Jika menggunakan (AND) maka ke dua nya harus True maka code bisa di jalankan
    # Namun Jika OR maka hanya perlu salah satu saja yang betul
    # Oleh karena itu Kondisi di variabel LIMANOL harus menggukan AND agar dia bisa menjalankan IF statment dengan baik
    # Jika dia menggunakan OR maka ketikka (Input-ANGKA) melebihi 5(LIMA) atau kuran dari 0(NOL) Maka code tetap akan menjalakan IF 
    # Harusnya dia menjalanka else, Kenapa karena angka 6 dan 7 tidak termasuk kedalam kondisi
    # sedangkan kenapa IF tetap di jalankan ketika menggunakan OR karena itu bener salah satunya jadi tetep di jalani
    # oleh karena itu Pakai AND 
    lapanSebel = (input_Angka > 8 and input_Angka < 11)

    if limaNol:
        print("Angka lebih dari 0 dan kurang dari 5:", limaNol)
    elif lapanSebel:
        print("Angka lebih dari 8 dan kurang dari 11:", lapanSebel)
    else:
        print("Angka tidak dalam rentang yang ditentukan.")
    

inputUser1()

def inputUser2():
    input_Angka = float(input("Silahkan Input No:"))
    noLima = (input_Angka < 0 or input_Angka > 5)


    if noLima:
        print("Angka Kurang dari 0 atau Lebhi dari 5")
        print("NO:",input_Angka,noLima)
    else:
        print("NOT FOUND")
    return(noLima)
nolima =inputUser2()

def inputUser3():
    input_Angka = float(input("Silahkan Input No:"))
    lapanSebel = (input_Angka < 8 or input_Angka > 11)

    if lapanSebel:
        print("Angka Kurang dari 8 atau Lebih dari 11")
        print(lapanSebel)
    else:
        print("NOT FOUND")
    return(lapanSebel)

lapansebel = inputUser3()

isCorrect = nolima and lapansebel
print("chek: ",isCorrect)
