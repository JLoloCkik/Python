import random

x=random.randint(0,100)

while(True):
    a = int(input("Adj meg egy számot: "))

    if a > x:
        print(f"Ez a szám túl magas {a}")
    if a < x:
        print(f"Ez a szám túl alacsony {a}")
    if a == x:
        print(f"Erre gondoltam {a}" )
        break
        