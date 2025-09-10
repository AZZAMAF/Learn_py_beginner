#Operator dalam betuk Methods
## Merubah Case from the string

# == merubah semua ke upper Case
salam = "woi!"
print("normal = " + salam)
salam = salam.upper()
print("Upper Case = " + salam)

# Change to Lower Case
alay = " Aku KECE Awebiess"
print("\nNormal = " + alay)
alay = alay.lower()
print("LowerCAse = " + alay)

## Pengecekan with IS Method 

#contoh pengecekan lower Case
salam = '\nsist'
apakah_lower = salam.islower() # the output is bolean
print(salam + " is lower = " + str(apakah_lower)) # must be casting to String
is_Upper = salam.isupper()
print("is Upper = " + str(is_Upper)) # must be casting to String

# isalpha( ) == for chek huruf
# isalnum( ) == for chek pasword dan angka
# isdecimal() == only number
# isspcae() == spasi, tab, newlin \n
# istitle() == semua kata start from huruf besar

judul = "\nIt Is Okay Not To Be Orkay\n"
cek_judul = judul.istitle() # hasil Bolean

print(judul + "is title = " + str(cek_judul),"\n")

## Chek Komponent == Startswitch() endswitch()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end),'\n')

# Penggambungan Komponen Join() == mengaubungkan // split() === Memisahkan
pisah =['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabungan = ''.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

# Split == bakal jadi List lagi
gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'),'\n')

# Alokasi Karakter // rjust(), ljust(), center()

print(5*"=" + "data" + "="*5)

kanan = "kanan".rjust(10)
print('\n',"'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "Tengah".center(20,"-") # tambahkan argument lain 
print("'"+tengah+"'")

# kebalikannya ==> Strip()
tengah = tengah.strip("-") #Menghilangkan tanda :
print("'" + tengah + "'")



