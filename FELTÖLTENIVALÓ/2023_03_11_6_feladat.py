def CamelCase(szoveg):
    #Sok almafa van a kertemben.
    szoveg=szoveg.replace(",","")
    szoveg=szoveg.replace(".","")
    szoveg=szoveg.replace(";","")
    #Sok almafa van a kertemben
    szavak=szoveg.split(" ")
    #szavak=['Sok','almafa','van','a','kertemben']
    konv_szoveg=""    
    for i in szavak:
        #almafa
        konv_szoveg+=i[0].upper()+i[1:]
        #Almafa
    #konv_szoveg=SokAlmafaVanAKertemben
    return konv_szoveg

i=input("Kérem a mondatot: ")
print(CamelCase(i))