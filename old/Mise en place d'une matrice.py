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


#mise en place matrix etc...
def matrix_dp(actions):
    n = len(actions)
    matrix = []

    print(actions)
    pass


    # n = 3
    # dp = [[0] * (5) for _ in range(n + 1)]


    # for x in dp:
    #     print(x)

def main():
    field_1 = 'Actions #'
    field_2 = 'Coût par action (en euros)'
    field_3 = 'Bénéfice (après 2 ans)'
    path="Action folder/OC_p7_1er_tableau_actions.csv"
    budget_max= 500
    actions = read_actions_csv_file(path,field_1, field_2, field_3)
    matrix_dp(actions)


if __name__ =="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"durée d'execution: {end_time - start_time} s")