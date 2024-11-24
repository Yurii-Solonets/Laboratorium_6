from datetime import datetime

data_lab = datetime(2024, 11, 19)
data_kolokwium = datetime(2024, 12, 17)

dziś = datetime.today()

dni_od_lab = (dziś - data_kolokwium).days
dni_do_kolokwium = (data_kolokwium - dziś).days

miesiące = {
    1:"stycznia", 2:"lutego", 3:"marca", 4:"kwietnia",
    5:"maja", 6:"czerwca", 7:"lipca", 8:"sierpnia",
    9:"wreśnia", 10:"pażdziernika", 11:"listopada", 12:"grudnia"
}

print(f"Dzisiaj jest {dziś.day} {miesiące[dziś.month]} {dziś.year}")
print(f"Od ostatnich laboratoriów ({data_lab.day} {miesiące[data_lab.month]} {data_lab.year}) upłynęło {dni_od_lab} dni.")
print(f"Do kolokwium ({data_kolokwium.day} {miesiące[data_kolokwium.month]} {data_kolokwium .year}) pozodtało {dni_do_kolokwium} dni.")