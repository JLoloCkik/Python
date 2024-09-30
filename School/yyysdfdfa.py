import random

q=random.randint(0,1100)

while(True):
    x=int(input("Adj meg egy számot: "))
    if x > q :
        print(f"Túl big {x}")
    if x < q :
        print(f"Túl kicsi {x}")
    if x == q :
        print(f"Ezígyjo {x}")
        break