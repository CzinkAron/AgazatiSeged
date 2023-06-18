def osszead(x,y):
    return x+y

try:
    print(osszead(1,15))
except:
    print("nem összeadható")
else:
    print("összeadás elvégezve")
finally:
    print("feladat vége")