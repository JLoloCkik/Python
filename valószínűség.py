import random


n = int(input())


dobas_1 = random.randint(1, n)
dobas_2 = random.randint(1, n)


max_dobas = max(dobas_1, dobas_2)

if max_dobas < n:

    nyeresi_valoszinuseg = (n - max_dobas) / n
else:

    nyeresi_valoszinuseg = 0

print(f"1-es játékos dobása: {dobas_1}")
print(f"2-es játékos dobása: {dobas_2}")
print(f"A legnagyobb dobott szám: {max_dobas}")
print(f"A valószínűsége annak, hogy a 3-as játékos nyer: {nyeresi_valoszinuseg:.4f}")
