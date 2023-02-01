
from random import randint

n_coup = 0
n_cherche = randint(1,1000)
n_choisi = int(input("Choisir le nombre à faire deviner entre 1 et 1000 : "))
print("Indiqué à la machine si le nombre est 'plus' ou 'moins'")

while n_cherche != n_choisi:
    print("Je choisi le nombre :", n_cherche)
    if n_cherche < n_choisi:
        plus = print(int(input("Le nombre est ")))
        n_cherche = randint(1,n_cherche)
        n_coup += 1
    if n_cherche > n_choisi:
        moins = print(int(input("Le nombre est ")))
        n_cherche = randint(n_cherche,1000)
        n_coup += 1
    if n_cherche == n_choisi:
        print("Le nombre est ", n_cherche, ", j'ai trouvé en ",n_coup, "coup")


