import time
import csv

# calcul du profit
def calculate_profit (cost:float, percentage_profit:float) -> float:
    return cost * percentage_profit

# Ouvrir un fichier CSV d'action et lire son contenu
def read_actions_csv_file(path:str,field_1:str, field_2:str, field_3:str) -> list[tuple[str,float,float]]:
    action_dict={}
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Utiliser la ligne 'Actions #' comme clé
            action_name = row[field_1]
            cost = round((float(row[field_2])))
            percentage_profit = float(row[field_3].replace('%', '')) / 100
            benefice_en_euros = round((calculate_profit(cost, percentage_profit)))
            
            # Ajouter chaque ligne au dictionnaire avec le bénéfice
            action_dict[action_name] = {
                "Coût": cost,  
                "Bénéfice (%)": percentage_profit,
                "Bénéfice (euros)": benefice_en_euros
            }

    # convertir le dict en une liste de tuple 
    actions =[(name, details["Coût"], details["Bénéfice (euros)"]) for name, details in action_dict.items()]
    return actions

# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, actions):
    # création de la matrice
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(actions) + 1)]

    # remplissage de la matrice
    for i in range(1, len(actions) + 1):
        for w in range(1, capacite + 1):
            if actions[i-1][1] <= w:
                matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-actions[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]


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
    return profit_max, actions_selection

def display_results(profit_max, actions_selection):
    # affichage des resultats
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
    field_1 = 'Actions #'
    field_2 = 'Coût par action (en euros)'
    field_3 = 'Bénéfice (après 2 ans)'
    path="Action folder/OC_p7_1er_tableau_actions.csv"
    actions = read_actions_csv_file(path, field_1, field_2, field_3)
    capacite = 500
    profit_max, actions_selection = sacADos_dynamique(capacite, actions)
    display_results(profit_max, actions_selection)



if __name__ =="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"durée d'execution: {end_time - start_time} s")