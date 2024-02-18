# 1. Feladat: Rajzoljuk meg az adott ábrát. 
# A szakaszok egyforma hosszúak, 100 képpontosak.
# A középső háromszög szabályos

# 1. Lépés: Globális változók létrehozása 
# (Data Structure)
kezdoFok = 0
fok = 60
elore = 100

# 2. Lépés: Globális változók feltöltése 
# (User Interface I.)

# 3. Lépés: Üzleti logika 
# (Business Logic)
from turtle import *

forward(elore)
left(fok)
forward(elore)
setheading(kezdoFok)
right(fok)
forward(elore)
left(fok)
forward(elore)

done()

# 4. Lépés: Eredmények kiíratása 
# (User Interface II.)
