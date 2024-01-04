#Algorytm Gaussa do wyznaczania daty Wielkanocy w zadanym roku
#wersja v2 z wykorzystaniem listy krotek oraz pętli zamiast ciągu operacji "if"
#The Gauss's Easter algorithm
#v2 version using a list of tuples and a loop insted of a long set of "if" clauses
#implementacja: (implemented by: ) Adrian Skowronski
#GitHub: https://github.com/adrian-skowronski

import sys
from datetime import datetime, timedelta

year = int(input("Wprowadz rok: (Enter the year: ) "))

year_range = [
    (1583, 1700, 22, 2), #początek zakresu włącznie, koniec zakresu z wyłączeniem, wartość_A, wartość_B
    (1700, 1800, 23, 3), #start of the range including, end of the range excluding, A_value, B_value
    (1800, 1900, 23, 4),
    (1900, 2100, 24, 5),
    (2100, 2200, 24, 6),
    (2200, 2300, 25, 0),
    (2300, 2400, 26, 1),
    (2400, 2500, 25, 1),
]

for start, end, A_value, B_value in year_range:
    if start <= year < end:
        A = A_value
        B = B_value
        break

if 1583 > year or year > 2499:
    print("brak danych dla tego roku (no data for this year)")
    sys.exit()

a = int(year % 19)
b = int(year % 4)
c = int(year % 7)
d = int((a*19+A) % 30)
e = int((2*b+4*c+6*d+B) % 7)

difference = int(d+e)
date = datetime(year,3,22)
Easter = (date + timedelta(difference)).date()

print("Wielkanoc w roku "+str(year)+" wypada w dniu: "+str(Easter))
print("Easter in "+str(year)+" falls on: "+str(Easter))