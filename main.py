kvadratas = [7, 8, 9, 4, 5, 6, 1, 2, 3]
zaidejas = "X"

def atspausdinti_kvadrata():
    eile = 0
    for simbolis in kvadratas:
        print(str(simbolis) + "|", end="")
        eile += 1
        if eile == 3:
            print()
            eile = 0

laimejimai = [[True, False, False, True, False, False, True, False, False], [False, True, False, False, True, False, False, True, False], [False, False, True, False, False, True, False, False, True], [True, True, True, False, False, False, False, False, False], [False, False, False, True, True, True, False, False, False], [False, False, False, False, False, False, True, True, True], [True, False, False, False, True, False, False, False, True], [False, False, True, False, True, False, True, False, False]]


def tikrinti_laimejima():
    pakeistas = kvadratas.copy()
    for counter, x in enumerate(pakeistas):
        if x == zaidejas:
            pakeistas[counter] = True
        else:
            pakeistas[counter] = False
    for laimejimas in laimejimai:
        for nr, langelis in enumerate(laimejimas):
            if langelis == True:
                if pakeistas[nr] == langelis:
                    continue
                else:
                    break
        else:
            return True
    return False

atspausdinti_kvadrata()

while True:
    print()
    pasirinkimas = int(input(f"Žaidėjas {zaidejas}: pasirinkite veiksmą"))
    if pasirinkimas in kvadratas:
        kvadratas[kvadratas.index(pasirinkimas)] = zaidejas
        atspausdinti_kvadrata()
        if tikrinti_laimejima():
            print(f"Žaidėjas {zaidejas} laimėjo!")
            break
        if zaidejas == "X":
            zaidejas = "O"
        else:
            zaidejas = "X"
    else:
        print("Nėra tokio pasirinkimo, bandykite dar kartą")
