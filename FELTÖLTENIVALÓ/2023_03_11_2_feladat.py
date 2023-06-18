import math
print('2. feladat: Derékszögű háromszög átfogójának kiszámítása')
print('kérem a két befogó méretét!')
l = 0

def atfogo(a,b):
    x = a*a+b*b
    y = math.sqrt(x)
    if y < 5:
        raise ValueError('Hiba! Túl kicsi a derékszögű háromszög!')
    else:
        return(y)
while l == 0:
        a = float(input('Egyik befogó mérete:   '))
        if a == 0:
            break
        b = float(input('Másik befogó mérete:   '))
        if b == 0:
            break
        try:
            print(f'Az átfogó mérete: {atfogo(a,b):.2f}')
        except ValueError as hiba:
            print(hiba)
        