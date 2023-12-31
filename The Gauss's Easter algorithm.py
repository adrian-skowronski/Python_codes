#Algorytm Gaussa do wyznaczania daty Wielkanocy w zadanym roku
#The Gauss's Easter algorithm
#implementacja: (implemented by: ) Adrian Skowronski
#GitHub: https://github.com/adrian-skowronski

import sys
from datetime import datetime, timedelta

rok = int(input("Wprowadz rok: (Enter the year: ) "))
if rok <= 1582:
     A = 15 #wartosci A i B do algorytmu Gaussa (A and B values are needed for the Gauss's Easter algorithm)
     B = 6
elif rok > 1582 and rok < 1700:
     A = 22
     B = 2
elif rok >= 1700 and rok < 1800:
     A = 23
     B = 3
elif rok >= 1800 and rok < 1900:
     A = 23
     B = 4
elif rok >= 1900 and rok < 2100:
     A = 24
     B = 5
elif rok >= 2100 and rok < 2200:
     A= 24
     B= 6
elif rok >= 2200 and rok < 2300:
     A = 25
     B= 0
elif rok >= 2300 and rok < 2400:
     A = 26
     B = 1
elif rok > 2400 and rok < 2500:
     A = 25
     B = 1
elif rok > 2499:
    print("brak danych dla tego roku (no data for this year)")
    sys.exit()

a = int(rok % 19)
b = int(rok % 4)
c = int(rok % 7)
d = int((a*19+A) % 30)
e = int((2*b+4*c+6*d+B) % 7)

roznica = int(d+e)
data = datetime(rok,3,22)
Wielkanoc = (data + timedelta(roznica)).date()

print("Wielkanoc w roku "+str(rok)+" wypada w dniu: "+str(Wielkanoc))
print("Easter in "+str(rok)+" falls on: "+str(Wielkanoc))