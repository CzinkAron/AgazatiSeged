import random

def vszoveg(hossz):
    szoveg=""
    for i in range(hossz):
        betu=random.randint(97,122)
        sz=random.randint(0,1)
        if sz==0:
            szoveg+=chr(betu).upper()
        else:
            szoveg+=chr(betu)
    return szoveg

h=int(input("Milyen hosszú jelszó legyen: "))
print(vszoveg(h))