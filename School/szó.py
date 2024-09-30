import random

while True:
    kugi=int(input(" Mit akarsz nigger? "))
    abc = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I',

        'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 
        's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

    length = len(abc)

    i = 0
    a=""
    while (i  < kugi) :
        fasz = random.randint(0, length - 1)
        asd= abc[fasz]
        a=a+asd
        i += 1

    print(a)