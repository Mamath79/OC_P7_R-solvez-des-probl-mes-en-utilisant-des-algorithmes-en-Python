import itertools
import csv
import time



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
            cost = float(row[field_2])
            percentage_profit = float(row[field_3].replace('%', '')) / 100
            benefice_en_euros = calculate_profit(cost, percentage_profit)
            
            # Ajouter chaque ligne au dictionnaire avec le bénéfice
            action_dict[action_name] = {
                "Coût": cost,  
                "Bénéfice (%)": percentage_profit,
                "Bénéfice (euros)": benefice_en_euros
            }

    # convertir le dict en une liste de tuple 
    actions =[(name, details["Coût"], details["Bénéfice (euros)"]) for name, details in action_dict.items()]

    return actions

# creation d'une liste de combinaisons possible d'achat d'action pour un cout total ne depassant pas les 500€
def generate_valid_combinations(actions:list[tuple[str,float,float]]):
    valid_combinations = []
    budget_max = 500
    for n in range ( 1, len(actions)+1):
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


def display_results(total_combinations, top_1_combination):
    # Affichage nombre de combinaison et de la meilleur combinaison
    print(f"\nle nombre de combinaisons possibles est de : {total_combinations} ")
    top_1_combinations_names =[action[0] for action in top_1_combination[0]]


    print("\nLa meilleur combinaison d'achat d'action pour un montant de 500€ generant le maximum de profit sur deux ans est : \n")
    for action in top_1_combinations_names:
        print(action)
    print(f"\nle cout total est de: {top_1_combination[1]} €")
    print(f"\nle profit est de: {top_1_combination[2]} €")

def main():
    field_1 = 'Actions #'
    field_2 = 'Coût par action (en euros)'
    field_3 = 'Bénéfice (après 2 ans)'
    path="Action folder/OC_p7_1er_tableau_actions.csv"
    actions = read_actions_csv_file(path,field_1, field_2, field_3)
    valid_combinations, total_combinations, sorted_combinations, top_1_combinations = generate_valid_combinations(actions)
    display_results(total_combinations, top_1_combinations)

if __name__ =="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"durée d'execution: {end_time - start_time} s")
