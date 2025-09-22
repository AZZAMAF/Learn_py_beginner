# ex : Make execption

from numbers import Number
def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(12,12))

angka = 0
try:
    hasil = 10/angka
except Exception as error_massage:
    print(error_massage)
