# Anonymouse funciton
# currying < haskel curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil
data_hasil = pangkat(5,2)

print('fungsi bisa',data_hasil)

#dengan currying menjadi
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f'pangkat 2 = {pangkat2(5)}')
pangkat3 = pangkat(3)
print(f'pangkat 3 = {pangkat3(3)}')