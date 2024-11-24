import math
import random
from traceback import print_tb

dolna_granica = int(input("Podaj dolną granicę przedziału: "))
gorna_granica = int(input("Podaj górną granicę przedziału: "))

krotka = tuple(random.randint(dolna_granica, gorna_granica) for _ in range(10))

iloczyń = math.prod(krotka)
n = len(krotka)
średnia_geometryczna = iloczyń**(1/n)

print(f"Wylosowana krotka: {krotka}")
print(f"Średnia geometryczna krotki: {średnia_geometryczna:.2f}")
