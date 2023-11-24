# ievadi skaitli
skaitlis = int(input("Ievadiet skaitli: "))

# parbauda vai skaitlis ir pozitivs vai negativs
if skaitlis < 0:
    print("Faktoriāls nav definēts negatīviem skaitļiem.")
elif skaitlis == 0:
    print("Faktoriāls no 0 ir 1.")
else:
    faktorials = 1

    # Aprēķināt faktoriālu izmantojot for ciklu
    for i in range(1, skaitlis + 1):
        faktorials *= i

    # ievadit rezultātu
    print("Faktoriāls no", skaitlis, "ir:", faktorials)
