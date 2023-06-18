def terulet(a,b):
    ter=a*b
    if ter<100:
        raise ValueError("Hiba! Túl kicsi a telek!")
    return ter

print("Terület kiszámítása")

while True:
    a=float(input("Kérem adja meg a telek szélességét: "))
    if a==-1:
        break
    b=float(input("Kérem adja meg a telek hosszúságát: "))
    if b==-1:
        break
    try:
        print(f"Telek területe: {terulet(a,b)}m2")
    except ValueError as hiba:
        print(hiba)