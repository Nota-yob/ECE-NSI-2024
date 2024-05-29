# Exercice 1 : occurence de caractères

def occurrences(caractere, chaine) :
    n = 0
    for lettre in chaine :
        if lettre == caractere :
            n += 1
    return n

assert occurrences('e', "sciences") == 2
assert occurrences('i', "mississippi") == 4
assert occurrences('a', "mississippi") == 0
print("Ex 1 : Tests passed")

# Exercice 2 : rendu de monnaie
valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang+1 )
    
assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291,1) == [50, 50, 50, 50, 50, 20, 20, 1]
print("Ex 2 : Tests passed")
