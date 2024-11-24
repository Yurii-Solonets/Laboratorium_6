import time

czas = int(input("Podaj czas w sekundach: "))

while czas > 0:
    print(f"Pozostało: {czas} sekund")
    czas -= 1
    time.sleep(1)

print("\nCzas minął!")