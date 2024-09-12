n = 3
budget_max = 5
# dp = [[0] * (5) for _ in range(n + 1)]

# initialiser la matrice en 2d à zero
dp =[]
for actions in range(n+1):
    dp.append([0]* budget_max)


for x in dp:
    print(x)


num = 10.123456

print(round(num, 2))


user_input = input("entrer le nom du fichier à analyser pour un budget max de 500 €: ")
print(user_input)

# Retrouver les éléments en fonction de la somme
w = capacite
n = len(actions)
actions_selection = []

while w >= 0 and n >= 0:
    e = actions[n-1]
    if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
        actions_selection.append(e)
        w -= e[1]

    n -= 1