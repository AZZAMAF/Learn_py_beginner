# Latihan
# kalkulator sederhana 
number1 = int( input( 'angka 01 : '))
number2 = int(input('angka 02 : '))

Option = input(" add = Tambah // Kurang // Bagi :")

if Option == "+":
    output = number1 + number2
    print('Success add TAMBAH : ', output)
elif Option == "-":
    output = number1 - number2
    print('Success add', output)
elif Option == "/":
    output = number1 / number2
    print('Success add', output )
else:
    print('error kaga ada woi!!')




