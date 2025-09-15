# ==== LIST =====

# Kumpulan data numbers
data_angka = [1,    2, 3]
print(data_angka)

# Kumpulan data string
data_String = [ 'odo', 'rara', 'ege']
print(data_String)

# Kumpulan data bolean
data_boolean = [True, False, True, False]
print(data_boolean)

# Campuran ei
data_campuran = ['bala2', 2, False, 'renginang', 2 ,True]
print(data_campuran)

# Cara Alternative membuat list
data_range = range(0, 10, 2) # Start, Stop, Step
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat List dengan Forloop, list comphrehnsian
list_pake_for =  [i**10 for i in range(0, 10)]
print(list_pake_for)

# Make List us For and IF
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if)

