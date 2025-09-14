# Latihan Perulangan

sisi = 1
# 1. use Fo
# dummy variabel
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("\n ===== While =====")
# 2. use whil
count = 1
while True:
    print("*"*count)
    print("baka")
    count += 1

    if count > sisi:
        break
    
print('==== ganji ====')
# 3. Hanya ganjil saja

count = 1
while True:
    # akan kembali ke atas jika ganjil
    if count%2: 
        print('*'*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
        
print("last line ei")

    
print('==== ganji ====')
# 3. Hanya ganjil saja

count = 100
while True:
    # akan kembali ke atas jika ganjil
    if count%2: 
        print('*'*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
        
print("last line ei")

# 3. Segitiga sama kaki
sisi = 10
count = 0
spasi = int(sisi/2)
print(spasi)
while True:
    # akan kembali ke atas jika ganjil
    if count%2: 
        print('-'*spasi,'+'*count)
        spasi -= 1
        count += 1
    else:
        count += 100
        continue

    if count > sisi:
        break
print("last line ei")
# di spasi sisi di bagi 2 = 10 % 2 = 5 kan
# gua gak ngerti ini paramater untuk apa ya
# kita buat hipotesis # 1. bagi misalakan count % 2 itu gak bisa jadi para mater gaksih 
#2. aing nemu coy ternyata itu modulus devision di code aku kemarn 
#nah jadi fungsinya untuk menemukan sisa dari pembagian misalkan ya, 10%3 = 1 karana 10 di bagi 3 itu hasilnya 1 coy
# nah tapi masalahnya ini kan sebagai paramater konsepnya jadi agak bingung coy
# oke kemabali lagi ke 5, sama count, gini count kan = 1 ya terus ada modulu devision isinya %2 gin kan, nah berarti sama dengan gini,
# 1 di bagi biasa 2 = 0,5 tapi kalau modulus nya berapa sisanya = 0
# nah terus ya, inikan paramater kalau pake ginikan gampang 1 < 2 = true kalau pakai paramter biasa
# nah kalau make paramater yang kek gini gimana cara nentuinnya.  
# kita buat count = 100 atau 12, 10, 8, , 3,  the output is = +++++++++++++++++++++ kek gini coyyy sampe seratur karena gak ganjil apa ya
#     +++++++
#    +++++++++
#   +++++++++++ this for 7 count nya
# oh isee jadi kalau ganjil baru jalan ya, kita sudah temukan bahwa count = 1 % 2 ini akan jalan jika ganjil,
# ya gini masih bingung, jadikan 1%2 = 0, 0 ini apakah angkan ganjil atau tetep gitu, dan emang kalau misalkan
# 3 % 2 = 1 sisanya gitu ini kan ganjil jadi code berjalan. ya gitulah kurang lebih

#kita lanjut ke print nya coy, oke itukan spasi tuh = sisis di bagi 2 ya = 5
# berarti " " spasi nya akan di buat 5 kali gitukan,
"""
----- +++ ini gua ganti spasi nya dengan - strip beginian
---- +++++ ternyata si sepasi itu berkurang ya setiap di jalainin -1 karena kita tambahin itukan
--- +++++++
-- +++++++++
- +++++++++++  
"""

#si count ini kan 3 ya jadi dia pertama bakal print 3 coy + ini nya 
# gua bingung nya ini coy * ini untuk apa ya
# terus kalau di jalanin bakal nambah + 1 teruss git dah yang ini
# pokok nya bakal berhenti samap count = 3 lebih dari sisi = 10 
# nah untuk continue ini kan berfungsim agar output lanjut ke step berikutnya gitu kan
# gu juga gak terlalu ngarti matrik nya gimana cokk, udh mentok banget di continue ini 

# simple nya code run : > kalau bilangan ganjil true kalau gak ya else gitu kan
# gua coba ganti count nya ke 5 tapi kok kode nya jadi false ya is mean bakal jalan si false nya
#oh iya terus skip si if yang di bawah continue inijadi code berhenti dan gak bentuk segitiga lagi
# oke disini masalanya balik lagi ke paramaternya itu kan katanya modulus sisa bagi yang dimana ganjil, 10 % 2 = 0 harusnya jalan dong
# karena 0 itu termasuk ganjil wettt, oke darimana kamu tahu 0 itu ganjil lets prove it.
#dan yap hipotesis kamusalah selama ini coyy, jadi si parameter itu eror coy, so how the code run.

#. gini kan 1%2 = 0 modulus nya sisanya 0 kok bisa jalan sih, karena kenapa count itu angka nya ganjil, tapi hasilnya bukan ganjil, kok tetep bisa jalan ya,
#. gak tau pokok nya kalu count nya ganjil bisa jalan, tapi aku masih bingung disiin kenapanya. oke stuck lagi dan tanya ai

# ternyata aku salah konsep guys tentang modulus, aku paham guys itu teh sisa dari pembagian tapi bukan pembagain
# ex: 1 % 2 = 1 kenapa 1 kalau dibagi itu 0,5 secera hitugan ya, tapi tetep aja secara logika gak bisa
# u have 1 candy for sharing 2 kids, with logic is can't gitu, jadi tetep permennya sisa 1 