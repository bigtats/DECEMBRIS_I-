

ievaditais_skaitlis = int(input("Ievadiet skaitli bez komatiem!: "))

if ievaditais_skaitlis < 0:
    print("Faktoriāls nav domāts negatīviem skaitļiem.")
else:
    faktorials = 1

    for skaitlis in range(1, ievaditais_skaitlis + 1):
        faktorials *= skaitlis

    print(f"Faktoriāls no {ievaditais_skaitlis} ir: {faktorials}")