import time
import csv
from tqdm import tqdm


# Ouvrir un fichier CSV d'action et lire son contenu
def read_actions_csv_file(path:str,field_1:str, field_2:str, field_3:str) -> list[tuple[str,float,float]]:
    action_dict={}
    ignored_actions =[]
    try:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Utiliser la ligne 'Actions #' comme clé
                action_name = row[field_1]

                # price et profit X100 pour pouvoir les convertir en entier car
                # ils deviendront des index de la matrice qui doivent etre des entiers
                price = int(100*float(row[field_2].replace(",",".")))
                profit = int(100*float(row[field_3].replace(",",".")))
                
                # Ignorer les actions avec un coût négatif ou nul
                if price <= 0:
                    ignored_actions.append(action_name)
                    continue

                # Ajouter chaque ligne au dictionnaire avec le bénéfice
                action_dict[action_name] = {
                    "price": price,  
                    "profit": profit
                }

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{path}' n'a pas été trouvé.")
        return []
    except csv.Error:
        print(f"Erreur : Le fichier '{path}' n'est pas un fichier CSV valide.")
        return []
    
    #afficher liste des actions ignorées car cout negatif ou gratuit
    print("Action ignorées en raison du coût négatif ou nul: ")
    for elements in  ignored_actions:
        print(elements)

    # convertir le dict en une liste de tuple 
    actions =[(name, details["price"], details["profit"]) for name, details in action_dict.items()]
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
    

    #remplissage de la matrice
    for i in tqdm(range(1, len(actions) + 1)):
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

    profit_max = matrice[-1][-1] / 100
    # print(profit_max, actions_selection)
    return profit_max, actions_selection

def display_results(profit_max, actions_selection):

    actions_selection_names =[action[0] for action in actions_selection]
    print("\nLa meilleur combinaison d'achat d'action pour un montant de 500€ generant le maximum de profit sur deux ans est : \n")
    for action in actions_selection_names:
        print(action)

    total_cost = sum(actions[1] for actions in actions_selection) / 100

    print(f"\nle cout total est de: {total_cost} €")
    print(f"\nle profit est de: {profit_max} €")

def main():
    # parametrage des champs pour les fichiers d'actions a analyser
    field_1 = 'name'
    field_2 = 'price'
    field_3 = 'profit'

    # choix du fichier à analyser par l'utilisateur ( doit etre un csv bien formater present dan sle dossier Action folder)
    user_input = input("entrer le nom du fichier à analyser pour un budget max de 500 €: ")
    path=f"Action folder/{user_input}.csv"
    
    # choix du budget max à implementer :
    start_time = time.time()
    actions = read_actions_csv_file(path,field_1, field_2, field_3)
    capacite = 500 * 100
    profit_max, actions_selection = sacADos_dynamique(capacite, actions)
    display_results(profit_max, actions_selection)
    end_time = time.time()
    print(f"\ndurée d'execution: {end_time - start_time} s")

if __name__ =="__main__":
    main()