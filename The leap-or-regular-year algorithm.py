#Algorytm sprawdzajacy czy zadany rok jest przestepny, czy nieprzestepny
#Algorithm to check whether a given year is a leap or regular one
#implementacja: (implemented by: ) Adrian Skowronski
#GitHub: https://github.com/adrian-skowronski

year = int(input("Wprowadz rok: (Enter the year: ) "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(str(year)+" to rok przestepny (is a leap year)")
else:
    print(str(year)+" to rok nieprzestepny (is a regular year)")
