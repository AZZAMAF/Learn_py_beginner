# Continue, pass, break
# pass > berfungsi s dummy = tidak akan di eksekusi
"""
angka = 0

while angka < 5:
    angka += 1
    if angka == 3:
        pass
        
    print(angka)
    
"""

angka = 0

print(f"angka sekarang :{angka}")

while angka < 5 :
    angka += 1
    print(f"angka sekarang :{angka}")

    if angka == 3:
        print('ote')
        continue # akan membuat loop meloncat ke step selanjutnya

    print(f"woi") # Actoin 2

print(f"Beres")