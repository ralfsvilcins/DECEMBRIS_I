# Ievadiet skaitli no lietotāja
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

# Pārbaude, vai skaitlis ir nepāra
if ievaditais_skaitlis % 2 != 0:
    print(ievaditais_skaitlis, "ir nepāra skaitlis.")
else:
    print(ievaditais_skaitlis, "nav nepāra skaitlis.")
