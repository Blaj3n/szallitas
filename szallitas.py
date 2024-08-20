tomegek = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

print("2. feladat")

osszesen = 0
for tomeg in tomegek:
    osszesen += tomeg
print(f"A tárgyak tömegének összege: {osszesen} kg ")

print("3. feladat")
dobozok = []
aktualis_doboz = 0
max_suly = 20

for tomeg in tomegek:
    if aktualis_doboz + tomeg <= max_suly:
        aktualis_doboz += tomeg
    else:
        dobozok.append(aktualis_doboz)  # Jelenlegi doboz lezárása
        aktualis_doboz = tomeg  # Új doboz kezdése az aktuális tárggyal

# Utolsó doboz hozzáadása a listához (ciklus után)
if aktualis_doboz > 0:
    dobozok.append(aktualis_doboz)

print(f"A dobozok tartalmának tömege (kg): {dobozok} ")
print(f"A szükséges dobozok száma: {len(dobozok)}")

# for ciklus magyarázat

# Részletes lépések:
#
# Iteráció: Minden egyes tárgy (azaz a tomeg változó) sorra kerül a tomegek listából.
#
# Feltétel ellenőrzése: Az if feltétel ellenőrzi, hogy az aktuális doboz súlya (aktualis_doboz) és az
# új tárgy súlya (tomeg) együtt még belefér-e a doboz maximális súlyába (max_suly).
# Ha igen, akkor az új tárgyat hozzáadjuk az aktualis_doboz-hoz.
#   Belsejében: Ha a tárgy belefér, akkor a doboz súlyához hozzáadjuk a tárgy súlyát.
# Doboz lezárása: Ha az új tárgy hozzáadásával a doboz túllépné a maximális súlyt, akkor lezárjuk az aktuális dobozt:
# Belsejében: Az aktuális doboz súlyát elmentjük a dobozok listába. Ezután az új tárgyat az új doboz kezdésére használjuk, tehát az aktualis_doboz változót az új tárgy súlyával inicializáljuk.
# Utolsó doboz hozzáadása:
# A ciklus végén lehet, hogy maradt még egy doboz, amely nem került hozzáadásra a dobozok listához, ezért ezt hozzáadjuk,
# ha az aktualis_doboz súlya nagyobb mint 0.

# Teljesen részletes lépések:
# 1. Ciklus kezdete: Minden egyes tárgy súlya sorra kerül.
# 2. Tömegek összehasonlítása: Az aktualis_doboz súlyához hozzáadjuk a következő tárgy súlyát, és megnézzük, hogy az
# össz súly nem haladja-e meg a maximális 20 kg-ot.
# 3. Doboz lezárása és új kezdése: Ha a következő tárgy hozzáadásával a doboz túllépné a 20 kg-ot,
# lezárjuk a jelenlegi dobozt (mentjük a listába) és elkezdünk egy új dobozt, amiben az új tárgy már benne van.
# 4. Utolsó doboz: Miután a ciklus végéhez érünk, az utolsó doboz súlyát is hozzáadjuk a listához,
# ha van még bennetartalom.
# Ez a logika biztosítja, hogy a tárgyakat a lehető legjobban csomagoljuk, és minden doboz súlya ne haladja meg
# a 20 kg-ot.
