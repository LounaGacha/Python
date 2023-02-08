def saisirChiffre() -> int:
    code_Zero = 48
    code_Neuf = 59
    affiche = "Saisir un chiffre : "
    car = input(affiche)
    if len(car) == 1:
        code_ascii = ord(car)
    else:
        code_ascii = -1
    while (code_ascii < code_Zero) or (code_ascii > code_Neuf):
        print("Ce n'est pas un chriffre !")
        car = input("Saisir un chiffre : ")
        if len(car) == 1:
            code_ascii = ord(car)
        else:
            code_ascii = -1
    return int(car)

chiffre = saisirChiffre()
print("Chiffre saisi : ",chiffre)