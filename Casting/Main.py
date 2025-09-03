#Casting = Meruabh tipe data ke tipe yang lain

#INTEGER
print("=======Integer======")
data_int = 9 
print("data =", data_int, type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) # will false when int = 0

print("data =", data_float, type(data_float))
print("data =", data_string, type(data_string))
print("data =", data_bool, type(data_bool))

#FLOAT
print("=======Float=======")
data_float = 9.5 
print("data =", data_float, type(data_float))

data_int = int(data_float) #akan di bulatkan ke bawah
data_string = str(data_float)
data_bool = bool(data_float) # will false when int = 0

print("data =", data_int, type(data_int))
print("data =", data_string, type(data_string))
print("data =", data_bool, type(data_bool))

#Bolean
print("=======Bolean=======")
data_bool = False
print("data =", data_bool, type(data_bool))

data_int = int(data_bool) 
data_string = str(data_bool)
data_float = float(data_bool)

print("data =", data_int, type(data_int))
print("data =", data_string, type(data_string))
print("data =", data_float, type(data_float))
