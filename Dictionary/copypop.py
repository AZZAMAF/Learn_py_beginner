# Copy dictionary 
teman2 = {
    'cup':'ucup',
    'tg' :'otong',
    'dg' :'dudung',
    'lx' : 'ihsanlux',
    'od' : 'odosan'
}

friends = teman2.copy()

print(f'Teman-teman : {teman2}')
print(f'friends : {friends}\n')

teman2['cup']='ucup sutisnan'
print(f'Teman-teman : {teman2}')
print(f'friends : {friends}\n')

# Pop dictionary //  berdasarkan key
dataOtong = friends.pop("tg")
print(f' ini data otong: {dataOtong}')
print(f'friends : {friends}/n')

# Popitem ditctionary // only last 
dataTerakhir = friends.popitem()
print(f' ini data otong: {dataTerakhir}')
print(f'friends : {friends}/n')

