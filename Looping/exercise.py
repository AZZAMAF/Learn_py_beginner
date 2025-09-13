# Latihan Perulangan

sisi = 4
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
    count += 1

    if count > sisi:
        break
    
print('==== ganji ====')
# 3. Hanya ganjil saja

count = 1
while True:
    # akan kembali ke atas jika ganjil
    if count%2:
        continue
    
    # akan print jika genap
    print("*"*count)
    count += 1

    
    if count > sisi:
        break
        
