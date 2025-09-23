import time
import os
from . import Database
from .Util import random_str
def delete(no_buku):
    try:
        with (open(Database.DB_NAME,'r')) as file :
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1 :
                    pass
                else:
                    with open("data_temp.txt",'a',encoding='utf-8',) as temp_file:
                        temp_file.write(content)
                counter +=1
    except:
        print('database error')
    os.rename("data_temp.txt", Database.DB_NAME)
def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("error dalam update data")

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data['pk'] = random_str(6)
    data['data_add'] = time.strftime('%Y-%M-%D-%H-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun) 

    data_str = f'{data['pk']},{data['data_add']},{data['penulis']},{data['judul']},{data['tahun']}\n' 
    
    try:
        with open(Database.DB_NAME,'a', encoding='utf-8') as file :
            file.write(data_str)
    except:
        print('Data gagal di tambahkan')


def create_first_data():

    penulis = input('Penulis :')
    judul =  input('Judul :')
    
    while True:
        try:
            tahun = int(input('Tahun \t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun Harus angka, silahkan Masukan tahun  lagi (yyyy)')
        except:
            print("Tahun harus angka, Silahkan Masukan Tahun lagi (yyyy)")


    data = Database.TEMPLATE.copy()

    data['pk'] = random_str(6)
    data['data_add'] = time.strftime('%Y-%M-%D-%H-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)   

    data_str = f'{data['pk']},{data['data_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w', encoding='utf-8') as file :
            file.write(data_str)
    except:
        print('Udah lah gagal')

    try:
        with  open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            
            if "index" in kwargs :
                index_Buku = kwargs["index"]-1
                if index_Buku < 0 or index_Buku > jumlah_buku:
                    return False
                else:
                    return content[index_Buku]
            else: 
                return content
    except:
        print('Membaca Datbase error')
        return False
    
def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:    
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    