# Latihan Perulangan

sisi = 10
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

# 3. Segitiga sama kaki

count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    # akan kembali ke atas jika ganjil
    if count%2: 
        print(' '*spasi,'+'*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print("last line ei")
        