#Algorytm Gaussa do wyznaczania daty Wielkanocy w zadanym roku
#The Gauss's Easter algorithm
#implementacja: (implemented by: ) Adrian Skowronski
#GitHub: https://github.com/adrian-skowronski

import sys
from datetime import datetime, timedelta

year = int(input("Wprowadz rok: (Enter the year: ) "))
if year <= 1582:
     A = 15 #wartosci A i B do algorytmu Gaussa (A and B values are needed for the Gauss's Easter algorithm)
     B = 6
elif year > 1582 and year < 1700:
     A = 22
     B = 2
elif year >= 1700 and year < 1800:
     A = 23
     B = 3
elif year >= 1800 and year < 1900:
     A = 23
     B = 4
elif year >= 1900 and year < 2100:
     A = 24
     B = 5
elif year >= 2100 and year < 2200:
     A = 24
     B = 6
elif year >= 2200 and year < 2300:
     A = 25
     B = 0
elif year >= 2300 and year < 2400:
     A = 26
     B = 1
elif year > 2400 and year < 2500:
     A = 25
     B = 1
elif year > 2499:
    print("brak danych dla tego roku (no data for this year)")
    sys.exit()

a = int(year % 19)
b = int(year % 4)
c = int(year % 7)
d = int((a*19+A) % 30)
e = int((2*b+4*c+6*d+B) % 7)

difference = int(d+e)
date = datetime(rok,3,22)
Easter = (date + timedelta(difference)).date()

print("Wielkanoc w roku "+str(year)+" wypada w dniu: "+str(Easter))
print("Easter in "+str(year)+" falls on: "+str(Easter))
