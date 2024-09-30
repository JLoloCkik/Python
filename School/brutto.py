import random
import math

num1 = int(input("Add meg a kisebb számot:"))
num2 = int(input("Add meg a nagyobb számot:"))

brutto = random.randint(num1, num2)

print(f"A bruttó: {brutto} Ft")
print(f"A Nettó: {math.floor(brutto * 0.65)} Ft")
print(f"A asdcas: {math.floor(brutto * 0.25)} Ft")
print(f"A adfasdfa: {math.floor(brutto * 0.05)} Ft")
print(f"A fasdrfas: {math.floor(brutto * 0.15)} Ft")
print(f"A asdasd: {math.floor(brutto * 0.10)} Ft")
