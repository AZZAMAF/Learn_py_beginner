from . import Oprasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Oprasi.read(index=no_buku)

        if data_buku:

            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Data yang ingin anda hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Yakin akan dihapus(y/n)? ")
            if is_done == "y" or is_done == "Y":
                Oprasi.delete(no_buku)
                break
            
        else:
            print("nomor tidak valid, silahkan masukan lagi")
    
    print('Data Berhasil Dihapus')

def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Oprasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid, silahkan masukan lagi")
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")    
                    except:
                        print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")
            case _: print("index tidak cuocuoook")

        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah data sudah sesuai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    
    Oprasi.update(no_buku,pk,data_add,tahun,judul,penulis)
            

def create_console():
    print('\n\n'+'='*100)
    print('Silahkan tambah data buku\n')
    penulis = input('Penulis\t: ') 
    judul = input('Judul \t: ')
    while True:
        try:
            tahun = int(input('Tahun \t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun Harus angka, silahkan Masukan tahun  lagi (yyyy)')
        except:
            print("Tahun harus angka, Silahkan Masukan Tahun lagi (yyyy)")

    Oprasi.create(tahun,judul,penulis)
    print('Berikut adalah data baru anda')
    read_console()

def read_console():
    data_file = Oprasi.read()

    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'

    # Header
    print('\n'+'='*100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print('-'*100)
        

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}',end='') 
    # Footer
    print('='*100+'\n')