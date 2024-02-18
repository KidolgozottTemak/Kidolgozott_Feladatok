# 1. Feladat: Rajzoljuk meg a mellékelt házikót 
# egyetlen vonallal. Nem emelhetjük fel az ecsetet, 
# és nem mehetünk kétszer végig egy vonalon. 
# A tető szabályos háromszög. A szakaszok egyforma 
# hosszúak, 100 képpontosak. Az átlók hossza 141 képpont.

# 1. Lépés: Globális változók létrehozása 
# (Data Structure)
kezdoFok = 0
fok1 = 60
fok2 = 75
fok3 = 90
fok4 = 135
elore = 100
atlo = 141

# 2. Lépés: Globális változók feltöltése 
# (User Interface I.)

# 3. Lépés: Üzleti logika 
# (Business Logic)
from turtle import *

left(fok3)
forward(elore)
left(fok3)
forward(elore)
left(fok3)
forward(elore)
left(fok3)
forward(elore)
left(fok4)
forward(atlo)
right(fok2)
forward(elore)
setheading(kezdoFok)
right(fok1)
forward(elore)
setheading(0)
right(fok4)
forward(atlo)
setheading(kezdoFok)

done()

# 4. Lépés: Eredmények kiíratása 
# (User Interface II.)
