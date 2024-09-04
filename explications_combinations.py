import itertools

ls = ["a","b","c","d"]

all_combinations = []

for r in range ( 1, len(ls)+1):
    a = itertools.combinations(ls,r)
    all_combinations.append(list(a))

y=[i for i in all_combinations ]
    
for combinations in y:
    print(combinations)
