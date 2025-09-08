#Oprasi yang dapat di lakukan dengan Penyingkatan
#Oprasi ditambah dengan Assigment

a = 5 #Adalah Asigment
print('nilai a =', a)

a += 1 # is mean a = a + 1
print('nilai a += 1, =', a)

a -= 2 # is mean a = a - 2
print('nilai a -= 2, =', a)

a *= 5 # is mean = a x 5
print('nilai a *= 5, =', a)

a /= 2 # a / 2
print('nilai a /= 2, =', a)

b = 10
print('nilai b =', b)

#MODULUS & Floor Divison
b %= 3
print('nilai a %= 3, Nilai B Menjai = ', b)

b = 10
print('\n Nilai B =',b)

b //= 3
print('nilai b //= 3, Nilai B Menjadi=', a)

# Pangkat Or Eksponen
a = 5
print("nilai a =", a)
a **= 3
print('nilai a **= 3, Nilai A menjadi=', a)

#Oprasi Bitwise

# ====== OR ======
c = True
print("\n Nilai c = ", c)
c |= False
print('nilai c |= FAlse, Nilai C Menjadi =', c)

c = False
print("\n Nilai c = ", c)
c |= False
print('nilai c |= FAlse, Nilai C Menjadi =', c)

# ====== AND =====
c = True
print("\n Nilai c = ", c)
c &= False
print('nilai c &= FAlse, Nilai C Menjadi =', c)

c = True
print("\n Nilai c = ", c)
c &= True
print('nilai c &= True , Nilai C Menjadi =', c)

# ======== XOR =======
c = True
print("\n Nilai c = ", c)
c ^= False
print('nilai c ^= FAlse, Nilai C Menjadi =', c)

c = True
print("\n Nilai c = ", c)
c ^= True
print('nilai c = FAlse, Nilai C Menjadi =', c)

# GEser2
d = 0b0100
print('\n Nilai D =', format(d,'04b'))
d >>= 2
print('nilai d >>= 2  , Nilai d Menjadi =', format(d,'04b'))
d <<= 1
print('Nilai d <<= 1, nilai d menjadi', format(d, '04b'))