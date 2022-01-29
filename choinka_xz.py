clear_launchpad()
licznik_gorny = 0
licznik_dolny = 0
for wiersz in range(8):
    if wiersz < 3:
        licznik_gorny = licznik_gorny + 1
        for i in range(licznik_gorny):
            light_up(wiersz * 16 + 4 + i, COLOR_GREEN_FULL)

        for i in range(licznik_gorny):
            light_up(wiersz * 16 + 4 - i, COLOR_GREEN_FULL)
    elif wiersz < 6:
        licznik_dolny = licznik_dolny + 1
        for j in range(0, licznik_dolny+1):
            light_up(wiersz * 16 + 4 + j, COLOR_GREEN_FULL)

        for j in range(0, licznik_dolny+1):
            light_up(wiersz * 16 + 4 - j, COLOR_GREEN_FULL)
    elif wiersz >= 6:
        light_up(wiersz * 16 + 4, COLOR_AMBER_LOW)
