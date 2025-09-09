
#evrything in python is OBJECT  

data = "is this string"
print(data)
print(type(data))

print('"Hallo apakabar?"')
print("'Hallo apakabar?'")
print("TODAY IS Jum'at")

# Use \
# making sign ' to string
print('Lets pray jum\'at')
print('g\day, isn\'t it?' )

#Backlash
print("C:\\user\\Ucup")

# Tab
print("Ucup\t OTONG, jauhan")

#BackSpace
print("ucup \b otong, jadi deketan")

#NewLine
print("Baris pertama.\n baris kedua") # LF >> Line Feed >> unix = mac os / linux os
print("Baris pertama.\r baris kedua") # CR >> Carriage Return >> comodor, acron, lisp
print("Baris pertama.\r\n  baris kedua") # CRLF >> Line Feed carrieage return >> windows ey

# String literal / raw
# Hati-hati
print('C:\new Folder') # salah path
print('C:\\ew Folder')  # bener tapi gak efesien kalau banyak

#Use Raw String
#everything in side this is String (r = Rawrr)
print(r'C:\new Folder')

#Multiline
print(
    """
Nama : otong
Age : 1200
"""
)

# Multiline Literal String dan Raw
print(r"""
Name : Fak
Age : 12
WEB : www.ucup.com/newID
""")
