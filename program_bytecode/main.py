import time
start_time = time.time()
for i in range(1,1000):
    a = 10
print(time.time() - start_time, "detik")


#kita bisa mengcompile python ke namanya bytecode
#bytecode = bahasa penengah antara python sama mesin
#compli = penerjemah ke bahasa komputer
# jadi sesuatu yang sudah di compile atau bahasa programan compiler 
# akan lebih cepat karena langsung menggukana bahasa komputer

#make compailer = python3 -m py_compile main.py
# TATA CARA RUN
#cd __pycache__ -> python3 main tab/ enter/ jalan deh
#cd.. = turun satu folder

import dis

def my_code():
    a = 7
    b = 3
    c = a * b
    print(c)

dis.dis(my_code)
