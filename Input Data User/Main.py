
"""
data = input("Masukan Data:")
print("data =",data,"type =", type(data))

data_int = int(input("Masukan angka: "))
print("data =",data_int,"type =", type(data_int))

#===== Login =====

print("===Register====")
username = input("Name:")
id = int(input("id:"))

if username == "azzam" and id == (1234):
    print("Succes Login")
else :
    print("error")
"""
"""
def Register():

    name = input("Name:")
    user_id = input("ID:")

    if name and user_id:
        print("Regist is Successfuly")
        return name, user_id
    else:
        print("❌ Registrasi gagal! Data tidak boleh kosong.")
        return None, None


def Login(Saved_user, Saved_id):
    print("===Login====")
    name = input("Name:")
    id = input("Id:")

    if name == Saved_user and id == Saved_id:
        print("Login Succes")
    else:
        print("Try Again")

user, id = Register()
if user and id:
    Login(user, id)


"""

def Regist():
    print("regist")
    Name = input("Name:")
    id = input("Id:")
    return Name, id

saveName, saveId = Regist()

if saveName  and saveId :
    print("succes")
else:
    print("Try again")

def Login():
    print("====Login===")
    name = input("Name:")
    id = input("Id:")
    return(name ,id)
    
user, id = Login()

if saveName == user and saveId == id:
    print("yes ey")
else:
    print("salah sia")
