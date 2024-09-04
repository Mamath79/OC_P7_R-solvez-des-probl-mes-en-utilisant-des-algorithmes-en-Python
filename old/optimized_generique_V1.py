import time
import csv

# Ouvrir un fichier CSV d'action et lire son contenu
def read_actions_csv_file(path:str,field_1:str, field_2:str, field_3:str) -> list[tuple[str,float,float]]:
    action_dict={}
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Utiliser la ligne 'Actions #' comme clé
            action_name = row[field_1]
            cost = int(round((float(row[field_2]))))
            profit = int(round(float(row[field_3])))
            
            # Ignorer les actions avec un coût négatif
            if cost <= 0:
                print(f"Action ignorée en raison du coût négatif ou nul: {action_name}")
                continue
            
            action_dict[action_name] = {
                "Cost": cost,  
                "Profit": profit
            }

    # convertir le dict en une liste de tuple 
    actions =[(name, details["Cost"], details["Profit"]) for name, details in action_dict.items()]

    return actions

# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, actions):
    #creation de la matrice a deux dimensions initialiser à zero
    matrice = []
    for n in range(len(actions)+1):
        line = []
        for n in range(capacite +1):
            line.append(0)
        matrice.append(line)
    
    for n in matrice:
        print(n)

    #remplissage de la matrice
    for i in range(1, len(actions) + 1):
        for w in range(1, capacite + 1):
            if actions[i-1][1] <= w:
                matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-actions[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
    for n in matrice:
        print(n)

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

    profit_max = matrice[-1][-1]
    print(profit_max, actions_selection)
    return profit_max, actions_selection

def display_results(profit_max, actions_selection):

    actions_selection_names =[action[0] for action in actions_selection]
    print("\nLa meilleur combinaison d'achat d'action pour un montant de 500€ generant le maximum de profit sur deux ans est : \n")
    for action in actions_selection_names:
        print(action)

    total_cost = 0
    for actions in actions_selection:
        total_cost += actions[1]

    print(f"\nle cout total est de: {total_cost} €")
    print(f"\nle profit est de: {profit_max} €")

def main():
    field_1 = 'name'
    field_2 = 'price'
    field_3 = 'profit'
    path="Action folder/dataset2_Python+P7.csv"
    actions = read_actions_csv_file(path, field_1, field_2, field_3)
    capacite = 40
    profit_max, actions_selection = sacADos_dynamique(capacite, actions)
    display_results(profit_max, actions_selection)



if __name__ =="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"durée d'execution: {end_time - start_time} s")