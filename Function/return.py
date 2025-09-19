# Return woi
# Template Fungsi dengan kembalian 
# def name_fungsi(:
#       badan fungsi
#       return output


# Fungsi kuadrat

def Kuadrat(input_angka):
    output = input_angka**2
    return output

y = Kuadrat(2)
print(y)
    
def Tambah(angka1,angka2):
    return angka1 + angka2

Output = Tambah(12,12)
print(Output)

# Fungsi dengan return banyak

def Oprasi_math(angka1,angka2):
    Tambah = angka1 + angka2
    kurang = angka1 -angka2
    kali = angka1*angka2
    bagi = angka1/angka2

    return Tambah,kurang,kali,bagi

k,l,m,n = Oprasi_math(9,2)
print(f'Hasil Kali {k}')
print(k,l,m,n)
