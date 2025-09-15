#oprasi

# index 0(-3)        1(-2)         2(-1)
data = ["Ucup","Otong", "dudung"]
# Mengambil data dari list ini

data_0 = data[0]
print(f"data pertama (index 0 ) :{data_0}")

last_data = data[-1]
print(f"data Terakhir (index -1 ) :{last_data}")

data_ucup = data[-3]
print(f"data ucup (index -3 ) :{data_ucup}")

# Mengambil Info jumlah data pada List 
panjang_data = len(data)
print(f"Panjang Data :{panjang_data}")

# Manipulasi item pada List  sesuai posisi
print(f"data sebelum ditambah = \n {data} ")

data.insert(1, "asep")
print(f'data sesudah ditambah \n {data}')

# maneambah Di akhir List 
data.append("Jajang")
print(f"data ditambah lagi = \n {data}")

# Menambahkan List dengan List 
New_data = ['Ujang', 'Usep','Dadang']
data.extend(New_data)
print(f"data gabungan  = \n {data}")

# Merubah Data
# kita ubah data 2 menjadi mikail
data [2] = "mikail"
print(f"data Diuabah = {data}")

# Remove data
data.remove("mikail")
print(f'data REmove = \n{data}')

# merove data paling belakang 
data.pop()
print(f'Remove last data : {data}')


























































































































































