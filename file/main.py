#tutorial Membaca fiel eketernal

print(3*"=","Membaca file text",3*'=')
file = open('data.text', mode="r")

print(f'status read :{file.readable()}')
print(f'status read :{file.writable()}')

## read all of file
print(file.read())

# read one line
#print(file.readline(),end='')

## Baca all of line as List
#print(file.readlines())

print(f'apakah wes di close : {file.closed}')
file.close()
print(f'apakah wes di close : {file.closed}')

## salah satu teknin membuka file di python

print('\n',3*'=','Membaca file text dengan with', 3*'=')

with open('data.text', mode='r') as file:
    content = file.readline()
    print(content,end='')
    print(f'apakah wes di close : {file.closed}')

print(f'apakah wes di close : {file.closed}')