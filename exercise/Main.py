#Latihan konversi satuan penteratur

#Program konversi celcius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan Suhu Ke dalam Celcius :'))
print("Suhu Adalah :", celcius, "Celcius")

#Reamour
reamour = (4 / 5) * celcius
print("Suhu dalam remour adalah:", reamour, "remour")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah:", fahrenheit, "Fahrenheit")

#kelvin
Kelvin = celcius + 273
print("Suhu dalam kelvin adalah:", Kelvin, "kelvin")

# Latihan

print("\n === Latihan === \n")



cal = float(input('Masukan Suhu Ke dalam Celcius :'))
print("Suhu Adalah :", cal, "Celcius")

fahren = ((9/5) * cal) + 32
print("Suhu dalam Fahrenheit adalah:", fahren, "Fahrenheit")

print("\n Fahrenheit > Kelvin \n")
cal = (5/9) * (fahren -32) 
print("Suhu Fahrenheit ke celcius:", cal, "Celcius")

kelvn = cal + 273
print("Suhu celcius ke Kelvin :", kelvn, "kelvin")

print("\n Kelvin > Fahrenheit \n")
celcius = kelvn - 273
print("Suhu kelvin ke Celcius:", celcius, "Celcius")
fahrenheit = ((9/5) * celcius) + 32
print("Suhu Celcius ke fahrenheit:", fahrenheit, "Fahrenheit")

print("\n === Calcius > Remour ===")
if cal :
    kelvin = cal +273 #change to kelvin
    if kelvin:
        Remour = (4/5) * (kelvin - 273)
        print("Suhu Calcisu To Remour", Remour,"Remour")