import time
from . import Database
from .Util import random_str
def create_first_data():

    penulis = input('Penulis :')
    judul =  input('Judul :')
    tahun =  input('Tahun :')

    data = Database.TEMPLATE.copy()
    data['pk'] = random_str(6)
    data['data_add'] = time.strftime('%Y-%M-%D-%H-%S%z',time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun 

    data_str = f'{data['pk']},{data['data_add']},{data['penulis']},{data['judul']},{data['tahun']}'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w', encoding='utf-8') as file :
            file.write(data_str)
    except:
        print('Udah lah gagal')

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print('Membaca Datbase error')
        return False