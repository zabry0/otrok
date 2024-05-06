import random

def generuj_nahodny_seznam():
    delka_seznamu = random.randint(3, 15)  
    rozsah_hodnot = (20, 1000)  
    cisla = []
    for _ in range(delka_seznamu):
        cisla.append(random.randint(rozsah_hodnot[0], rozsah_hodnot[1]))
    return cisla

prvni_seznam = generuj_nahodny_seznam()
druhy_seznam = generuj_nahodny_seznam()

print("První náhodně generovaný seznam:", prvni_seznam)
print("Druhý náhodně generovaný seznam:", druhy_seznam)
