#Készíts egy listát az alábbi elemekkel:
#lista=['alma',1.45,'Budapest',46,78,152,1.75,'Barack']
#A feladat: válogasd ki a páros egész számokat, és írasd ki,
#helyiérték pontosan egymás alá

lista=['alma',1.45,'Budapest',46,78,152,1.75,'Barack']
szamok=[]
for i in range(len(lista)):
    try:
        a=int(lista[i])
        if a%2==0:
            szamok.append(a)
    except:
        print(f"{lista[i]} nem egész szám")
        continue
print(szamok)
