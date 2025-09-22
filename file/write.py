# 1. mode write : 
# always make new file when run jika tidak ada, dan menimpa isinya

with open('data_1.txt','w',encoding='utf-8') as file:
    file.write('jon si jhoney')


with open('data_1.txt','w',encoding='utf-8') as file:
    file.write('ucpup')

# 2. mode Append

with open('data_2.txt','a',encoding='utf-8') as file:
    file.write('ucpup\n')
with open('data_2.txt','a',encoding='utf-8') as file:
    file.write('jon si jhoney\n')

# 3. Mode R+

with open('data_3.txt','w',encoding='utf-8') as file:
    file.write('data ke 3\n')

with open('data_3.txt','r+',encoding='utf-8') as file:
    data = file.read()
    file.write('menambah dengan r+')
    print(data)