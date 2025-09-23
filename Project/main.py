import os
import CRUD as CRUD

if __name__ == "__main__" :
    sistem_Oprasi = os.name


    match sistem_Oprasi:
        case "posix" : os.system('clear')
        case 'nt' : os.system('cls')

    print('SELAMAT DATANG DI PROGRAM')
    print('Database Perpustakaan')
    print(30*'=')

    # Check database itu ada atau tidak
    CRUD.init_console()


    while(True):

        match sistem_Oprasi:
            case "posix" : os.system('clear')
            case 'nt' : os.system('cls')


        print('SELAMAT DATANG DI PROGRAM')
        print('Database Perpustakaan')
        print(30*'=')

        print(f'1.Read Data')
        print(f'2.Create Data')
        print(f'3.Update Data')
        print(f'4.Delete Data\n')

        user_Option = input('Masukan Opsi:')


        match user_Option:
            case "1": CRUD.read_console()
            case "2": print('Create Data')
            case "3": print('Update Data')
            case "4": print('Delete Data')

        
        isDone = input('\nApakah Selesay y/n ?')
        if isDone == 'y' or isDone == "Y":
            break
    print('program done thank u')