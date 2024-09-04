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