import random

listy = list(range(1, 49))

wylosowane = random.sample(listy, 6)

wylosowane.sort()

print(f"Wylosowane liczby w Dużym Lotku: ", wylosowane)