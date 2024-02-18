# 1. Feladat: A program kérjen be egy számot, 
# majd írja ki a megelőző és a rákövetkező értéket.

# 1. Lépés: Globális változók létrehozása 
# (Data Structure)
bekertSzam = 0
elozo = 0
rakovetkezo = 0
kiiratas = ""

# 2. Lépés: Globális változók feltöltése 
# (User Interface I.)
bekertSzam = int(input("Kérek egy egész számot: "))

# 3. Lépés: Üzleti logika 
# (Business Logic)
elozo = bekertSzam - 1
rakovetkezo = bekertSzam + 1
kiiratas = f"A szám: {bekertSzam}."
kiiratas += f"\nAz előző szám: {elozo}."
kiiratas += f"\nA rákövetkező szám: {rakovetkezo}."

# 4. Lépés: Eredmények kiíratása 
# (User Interface II.)
print(kiiratas)

