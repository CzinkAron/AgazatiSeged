class Class_cím:
    def __init__(self,sor:str):
        adatok = sor.strip().split(';')
        self.egy = adatok[0]
        self.kettő = int(adatok[1])
        self.három = adatok[2]
        self.négy = adatok[3]
        self.öt = int(adatok[4])
        self.hat = int(adatok[5])
        self.hét = float(adatok[6].replace(',','.'))
        self.négy = adatok[7]
        self.kilenc = adatok[8]
        self.tíz = int(adatok[9])
        self.tizenegy = adatok[10]


Lista_cím:list[Class_cím]=[]
file=open('adott beolvasandó file', 'r')
fejlec= file.readline()
for sor in file:
    Lista_cím.append(Class_cím(sor))
file.close()
