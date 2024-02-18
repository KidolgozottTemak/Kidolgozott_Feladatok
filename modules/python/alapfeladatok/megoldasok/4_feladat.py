# 1. Feladat: A program kérjen be egy vezetéknevet 
# és egy keresztnevet. Üdvözölje a felhasználót
# Vezetéknév-keresztnév sorrendben
# Keresztnév-vezetéknév sorrendben.

# 1. Lépés: Globális változók létrehozása 
# (Data Structure)
vezeteknev = ""
keresztnev = ""
udvozlet1 = ""
udvozlet2 = ""

# 2. Lépés: Globális változók feltöltése 
# (User Interface I.)
vezeteknev = input("Kérek egy vezetéknevet: ")
keresztnev = input("Kérek egy keresztnevet: ")

# 3. Lépés: Üzleti logika 
# (Business Logic)
udvozlet1 = f"Hello {vezeteknev} {keresztnev}!"
udvozlet2 = f"Hello {keresztnev} {vezeteknev}!"

# 4. Lépés: Eredmények kiíratása 
# (User Interface II.)
print(udvozlet1)
print(udvozlet2)

