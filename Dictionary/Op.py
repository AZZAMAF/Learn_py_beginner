# Operator Dictionary

data_dict = {
    'cup':'ucup',
    'tg' :'otong',
    'dg' :'dudung'
}

# Panjang Dictionary
LENDICT = len(data_dict)
print(f' panjang Dictionary : {LENDICT}')

# chcek key  axist atau tidak
KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data dict : {CHECKKEY}')

# Mengakses Value (read) dengan get
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis', 'key henteu aya')) # check key with masagge ' key henteuy aya'

# Update Data
data_dict['cup'] = 'ucup siganting'
print(data_dict)
data_dict['tg'] = 'asep si kanting'
print(data_dict)

data_dict.update({'cup' :'ucup'})
print(data_dict)
data_dict.update({'faktu' : 'Azaam ganteng'}) # kalau gak ada di update aja
print(data_dict)

# Mendelete data
del data_dict['cup']
print(data_dict)