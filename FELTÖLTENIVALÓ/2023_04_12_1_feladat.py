print('1. feladat: Számok sorozata')
print('Kérem az alsó és a felső határt!')
also = int(input('a = '))
felso = int(input('b = '))
x = 1
while also > felso:
    print('Az alsó határ kisebb legyen mint a felső!')
    also = int(input('a = '))
    felso = int(input('b = '))

for i in range(also,felso+1):
    x = x*i
print(f'A számok sorozata: {x}')