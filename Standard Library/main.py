import datetime

dataWaktu =  datetime.datetime.now()
print(dataWaktu)
print(dataWaktu.year)

from collections import Counter

data = ['a','b','g','r','a','a']
dataCount = Counter(data)

print(f'ini adalah data count : {dataCount}')
print(f'jumlah :{dataCount['a']}')

import io

file = io.open('file_text.text','r')
print(file.read())