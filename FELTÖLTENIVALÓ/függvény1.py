def lánchossz(lánc,karakter):
    z=0
    for i in lánc:
        if i==karakter:
            z+=1
    return z

x=input("Kérem a karakterláncot: ")
y=input("Kérem a keresett karaktert: ")
print(f"A szövegben {lánchossz(x,y)} alkalommal szerepel a keresett karakter.")