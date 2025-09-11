#Format String
# ex : generic
# String
nama = 'azzam'
format_str = f"Hello {nama}" 

print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Number
number = 23923.3
format_str = f"Angka : {number}  " 
print(format_str)

# Bilangan Bulat
angka = 15
format_str = f"Bilangan bulat : {angka:d}"
print(format_str)

# Bilangan ribuatn //
angka = 2000
format_str = f"Ribuan : {angka:,}"
print(format_str)

# Bilangan Desimal  
number = 23923.3123
format_str = f"Angka : {number:.0f}" 
print(format_str)

# Menampilkan Leading Zero
number = 23923.3242
format_str = f"Angka : {number:8.3f}  " 
print(format_str)

# menampilkan tanda + or - 
angka_minus = -10
angka_plus = 10.234
format_minus = f"Minus {angka_minus:+d}"
format_plus = f"Plus {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# Memformat Persen 
persentase = 0.045
format_persen = f"Persen = {persentase:.4%}"

print(format_persen)

# do opration aritmatika in placeholder {}
harga = 10000
jumlah = 5

format_string = f"Harga total = Rp.{harga*jumlah:,}"
print(format_string)

# Format angka lain  (Binary, octal, hexadecimal)
angka = 255 
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hex = {hex(angka)}"

print(format_binary, format_octal, format_hex)

