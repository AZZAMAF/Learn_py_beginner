# isalpha( ) == for chek huruf
# isalnum( ) == for chek pasword dan angka
# isdecimal() == only number
# isspcae() == spasi, tab, newlin \n

huruf_Check = "adsdkad".isalpha()
print("Chek huruf = ", huruf_Check)

pwd_Check = "azzamidn123".isalnum()
print("Check PWD = ", pwd_Check)

decimal_Check = "2345".isdecimal()
print('Check Decimal =', decimal_Check)

Space_Check = "  ".isspace()
print('Check Space =', Space_Check)
