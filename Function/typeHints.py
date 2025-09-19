# Penggunana type Hints

import string
def pangkatSepuluh(argument:int) -> int:
        output = 10**argument
        return output

hasil = pangkatSepuluh(12)
print(hasil)

def display(argument:string):
    print(argument)

display('ucup')