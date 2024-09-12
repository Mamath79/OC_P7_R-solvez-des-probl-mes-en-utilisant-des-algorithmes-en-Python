import itertools
import csv
import time
from tqdm import tqdm

# calcul du profit
def calculate_profit (price:float, percentage_profit:float) -> float:
    return price * percentage_profit / 100

# Ouvrir un fichier CSV d'action et lire son contenu et calculer le profit reel pour chaque action
def read_actions_csv_file(path:str,field_1:str, field_2:str, field_3:str) -> list[tuple[str,float,float]]:
    action_dict={}
    try:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                action_name = row[field_1]
                price = float(row[field_2].replace(",","."))
                profit_percentage = float(row[field_3].replace(",",".").replace("%",""))
                profit = calculate_profit(price, profit_percentage)
                
                # Ajouter chaque ligne au dictionnaire avec le profit réel
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
    
    # convertir le dict en une liste de tuple 
    actions =[(name, details["price"], details["profit"]) for name, details in action_dict.items()]
    return actions

# creation d'une liste de combinaisons possible d'achat d'action pour un cout total ne depassant pas les 500€
def generate_valid_combinations(actions:list[tuple[str,float,float]], budget_max:int):
    valid_combinations = []
    for n in tqdm(range( 1, len(actions)+1)):
        for combination in itertools.combinations(actions, n):
            total_cost = sum(action[1] for action in combination)
            total_profit = sum(action[2] for action in combination)
            if total_cost <= budget_max:
                valid_combinations.append((combination,total_cost,total_profit))
    
    # nombre total de combinaison
    total_combinations = len(valid_combinations)

    # trier les combinaisons par profit decroissant pour etablir un classement des meilleurs combinaison
    sorted_combinations = sorted(valid_combinations, key=lambda x :x[2], reverse=True)

    # ne garder que la meilleur combinaison
    top_1_combination = sorted_combinations[0]

    return valid_combinations, total_combinations, sorted_combinations, top_1_combination


def display_results(total_combinations:int, top_1_combination:list[tuple[str,float,float]]):
    # Affichage nombre de combinaison et de la meilleur combinaison
    print(f"\nle nombre de combinaisons possibles est de : {total_combinations} ")
    top_1_combinations_names =[action[0] for action in top_1_combination[0]]

    print("\nLa meilleur combinaison d'achat d'action pour un montant de 500€ generant le maximum de profit sur deux ans est : \n")
    for action in top_1_combinations_names:
        print(action)
    print(f"\nle cout total est de: {top_1_combination[1]} €")
    print(f"\nle profit est de: {top_1_combination[2]} €")

def main():
    # parametrage des champs pour les fichiers d'actions à analyser
    field_1 = 'name'
    field_2 = 'price'
    field_3 = 'profit'

    # choix du fichier à analyser par l'utilisateur ( doit etre un csv bien formater present dan sle dossier Action folder)
    user_input = input("entrer le nom du fichier à analyser pour un budget max de 500 €: ")
    path=f"data/{user_input}.csv"
    
    # choix du budget max à implementer :
    budget_max = 500

    # mesure du temps d'execution du programme 
    start_time = time.time()
    actions = read_actions_csv_file(path,field_1, field_2, field_3)
    valid_combinations, total_combinations, sorted_combinations, top_1_combinations = generate_valid_combinations(actions,budget_max)
    display_results(total_combinations, top_1_combinations)
    end_time = time.time()
    print(f"\ndurée d'execution: {end_time - start_time} s")

if __name__ == "__main__":
    main()
