# suivre la methode du sac a dos https://www.youtube.com/watch?v=wDsZhd1wEuk


# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection

# Nom
# poids
# Valeur

elements = [('Montre à gousset', 2, 6),
        ('Boule de bowling', 3, 10),
        ('Portrait de tata Germaine', 4, 12)]
print('Algo dynamique', sacADos_dynamique(5, elements))
