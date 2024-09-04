import csv
import time
import math

# Calcul du profit (fonction simplifiée car le profit est directement donné en euros dans le CSV)
def calculate_profit(cost: float, profit: float) -> float:
    return profit

# Lire le contenu d'un fichier CSV d'action
def read_actions_csv_file(path: str, field_1: str, field_2: str, field_3: str) -> list[tuple[str, float, float]]:
    action_dict = {}
    try:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    action_name = row[field_1]
                    cost = float(row[field_2])
                    profit = float(row[field_3])
                    
                    # Filtrer les actions avec un prix de 0.0 si nécessaire
                    if cost == 0.0:
                        print(f"Action ignorée en raison du coût de 0.0: {action_name}")
                        continue

                    benefice_en_euros = calculate_profit(cost, profit)

                    action_dict[action_name] = {
                        "Coût": cost,
                        "Bénéfice (euros)": benefice_en_euros
                    }
                except ValueError as ve:
                    print(f"Erreur de conversion des données pour l'action {row}: {ve}")
                except KeyError as ke:
                    print(f"Champ manquant dans le CSV: {ke}")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{path}' n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
        return []

    actions = [(name, details["Coût"], details["Bénéfice (euros)"]) for name, details in action_dict.items()]
    return actions

# Optimisation avec la Programmation Dynamique
def optimize_actions_with_dp(actions: list[tuple[str, float, float]], budget_max: int):
    n = len(actions)
    dp = [[0] * (budget_max + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        action_name, cost, profit = actions[i - 1]
        adjusted_cost = math.floor(cost)
        for w in range(budget_max + 1):
            if adjusted_cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - adjusted_cost] + profit)
            else:
                dp[i][w] = dp[i-1][w]

    # Reconstruire la meilleure combinaison
    w = budget_max
    best_combination = []
    for i in range(n, 0, -1):
        action_name, cost, profit = actions[i - 1]
        adjusted_cost = math.floor(cost)
        
        # Utiliser les valeurs de la table dp pour vérifier la validité de l'inclusion de l'action
        if dp[i][w] != dp[i-1][w] and adjusted_cost <= w:
            best_combination.append((action_name, cost, profit))
            w -= adjusted_cost
            if w < 0:
                break

    best_combination.reverse()
    total_cost = sum(action[1] for action in best_combination)
    total_profit = sum(action[2] for action in best_combination)

    return best_combination, total_cost, total_profit

# Afficher les résultats
def display_results(best_combination, total_cost, total_profit):
    print("\nLa meilleure combinaison d'achat d'action pour un montant de 500€ générant le maximum de profit est :\n")
    for action in best_combination:
        print(f"{action[0]} - Coût: {action[1]}€ - Bénéfice: {action[2]}€")
    
    print(f"\nLe coût total est de: {total_cost} €")
    print(f"Le profit total est de: {total_profit} €")

# Point d'entrée principal
def main():
    field_1 = 'name'
    field_2 = 'price'
    field_3 = 'profit'
    path = "Action folder/dataset1_Python+P7.csv"
    actions = read_actions_csv_file(path, field_1, field_2, field_3)
    if not actions:
        print("Aucune action valide trouvée.")
        return
    
    budget_max = 500
    best_combination, total_cost, total_profit = optimize_actions_with_dp(actions, budget_max)
    display_results(best_combination, total_cost, total_profit)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Durée d'exécution: {end_time - start_time} s")
