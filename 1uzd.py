# ievadi skaitli
skaitlis = int(input("Ievadiet skaitli: "))

# ievada ka skaitlis ir lielāks par 0 jeb ir pozitivs
if skaitlis <= 0:
    print("Lūdzu ievadiet pozitīvu skaitli.")
else:
    # ieraksti summu
    summa = 0

    # lieto for cikls, lai saskaitītu skaitļus no 1 līdz lietotāja ievadītajam skaitlim
    for skaitlis in range(1, skaitlis + 1):
        summa += skaitlis

    # Izvadīt rezultātu
    print("Summa no 1 līdz", skaitlis, "ir:", summa)
