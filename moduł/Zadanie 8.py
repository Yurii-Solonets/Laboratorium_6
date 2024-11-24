import keyword

słowa = {"for", "print", "break", "done", "bad"}

for słowo in słowa:
    if keyword.iskeyword(słowo):
        print(f"'{słowo}' jest słowem kluczowym")
    else:
        print(f"'{słowo}' nie jest słowem kluczowym")