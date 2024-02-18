# 1. Feladat: A program kérjen be két pozitív egész  
# számot, majd írja ki azok összegét, különbségét, 
# szorzatát és hányadosát.

# 1. Lépés: Globális változók létrehozása 
# (Data Structure)
bekertElsoSzam = 0
bekertMasodikSzam = 0
osszeg = 0
kulonbseg = 0
szorzat = 0
hanyados = 0
kiiratas = ""

# 2. Lépés: Globális változók feltöltése 
# (User Interface I.)
bekertElsoSzam = int(input("Kérek egy egész pozitív számot: "))
bekertMasodikSzam = int(input("Kérek egy másik pozitív egész számot: "))

# 3. Lépés: Üzleti logika 
# (Business Logic)
osszeg = bekertElsoSzam + bekertMasodikSzam
kulonbseg = bekertElsoSzam - bekertMasodikSzam
szorzat = bekertElsoSzam * bekertMasodikSzam
hanyados = bekertElsoSzam / bekertMasodikSzam
kiiratas = f"A két szám: {bekertElsoSzam}, {bekertMasodikSzam}."
kiiratas += f"\nÖsszegük: {osszeg}."
kiiratas += f"\nKülönbségük: {kulonbseg}."
kiiratas += f"\nSzorzatuk: {szorzat}."
kiiratas += f"\nHányadosuk: {hanyados}."

# 4. Lépés: Eredmények kiíratása 
# (User Interface II.)
print(kiiratas)

