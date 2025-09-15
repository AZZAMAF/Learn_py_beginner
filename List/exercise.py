# Program List Buku

listBuku = []
while True:

    print('===== Masukan Data Buku =====')

    Judul = input('masukan Judul Buku\t:')
    penulis = input('Penulis\t:')

    bukuBaru = [Judul,penulis]
    listBuku.append(bukuBaru)

    print('\n\n','='*10,' Data Buku')
    print('No \t.| Judul \t\t | Penulis')
    for index,buku in enumerate(listBuku):
        print(f'{index+1}\t{bukuBaru[0]}\t\t {bukuBaru[1]}.')
    
    print('\n\n','='*20)
    isLanjut = input('Apakah Di lanjutkan ?(y/n)')

    if isLanjut=='n':
        break
print('\n=== Program Finish ===')