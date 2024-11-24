import math
import keyword

def wypisz_funkcje(module):
    funkcje = [nazwa for nazwa in dir(module) if callable(getattr(module, nazwa))]
    return funkcje

print("funkcje w module math: ")
print(wypisz_funkcje(math))

print("\nFunkcje w module keyword: ")
print(wypisz_funkcje(keyword))

print("\nMetody typu tuple:")
print(wypisz_funkcje(tuple))