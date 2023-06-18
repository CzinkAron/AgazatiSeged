def primszam(x):
    db=0
    for i in range(1,x+1):
        if x%i==0:
            db+=1
    if db<=2:
        return True
    else:
        return False

szam=int(input("Kérem a számot: "))
if primszam(szam):
    print("A szám primszám.")
else:
    print("A szám nem primszám.")