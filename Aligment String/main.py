# Width and Multiline
# Data

data_Name = 'azzam pinter'
data_Umur = 12
data_tinggi = 160.3
data_Nomor_sepatu = 45

#String Standard
data_String = f"Nama ={data_Name}, Umur = {data_Umur}, Tinggi = {data_tinggi}, Ukuran Sepatu = {data_Nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_String)

#String Multiline (With Enter \n)
data_String = f"Nama ={data_Name},\n Umur = {data_Umur}, \n Tinggi = {data_tinggi},\n Ukuran Sepatu = {data_Nomor_sepatu}"
print('\n'+5*"="+"Data String"+5*"=")
print(data_String)

# String Multiline (Kutip Triplets)
data_String = f"""
nama = {data_Name}
umur = {data_Umur}
Tinngi = {data_tinggi}
"""
print('\n'+5*"="+"Data String"+5*"=")
print(data_String)

# Mengatur Lebar
data_String = f"""
nama   = {data_Name}
nama   = {data_Name:>5}
umur   = {data_Umur:>12}
Tinngi = {data_tinggi:>12}
"""
print('\n'+5*"="+"Data String"+5*"=")
print(data_String)
