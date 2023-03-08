def ligne_pleine(car:str, nb:int) -> str:
    res = ""
    if nb >= 1:
        for i in range(nb):
            res = res + car
    else:
        print("Nombre choisi trop petit")
    return res


def ligne_creuse(car:str, nb:int) -> str:
    res = ""
    if nb >= 1:
        for i in range(nb):
            if i == 0 or i == nb-1:
                res = res + car
            else:
                res = res + " "
    return res


def rectangle_plein(car:str, longeur:int, largeur:int) -> None:
        for i in range(longeur):
            ligne_pleine(car,i)





'''def rectangle_creux(car:str, longeur:int, largeur:int) -> None:



def triangle_plein(car:str, longeur:int, largeur:int) -> None:



def triangle_creux(car:str, longeur:int, largeur:int) -> None:'''




rectangle_plein('B', 1, 5)

print("------------")

#Tests
assert ligne_pleine('M', 1) == "M"
assert ligne_pleine('#', 5) == "#####"
assert ligne_creuse('Y', 1) == "Y"
assert ligne_creuse('X', 5) == "X   X"