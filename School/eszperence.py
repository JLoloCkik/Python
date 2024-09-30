import math

m = int(input("Adja meg az m értékét: "))
n = int(input("Adja meg az n értékét: "))
k = int(input("Adja meg a csempe oldalhosszát: "))

cs_m = math.ceil(m / k)
cs_n = math.ceil(n / k)

cs = cs_m * cs_n

print(f"Szükséges csempék száma: {cs}")
