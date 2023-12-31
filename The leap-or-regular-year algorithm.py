#Algorytm sprawdzajacy czy zadany rok jest przestepny, czy nieprzestepny
#Algorithm to check whether a given year is a leap or regular one
#implementacja: (implemented by: ) Adrian Skowronski
#GitHub: https://github.com/adrian-skowronski

rok = int(input("Wprowadz rok: (Enter the year: ) "))
if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print(str(rok)+" to rok przestepny (is a leap year)")
else:
    print(str(rok)+" to rok nieprzestepny (is a regular year)")
