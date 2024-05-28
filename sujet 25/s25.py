# Exercice 1 : recherche min

def recherche_min(tab:list) -> int :
    i_min = 0 
    for i in range(len(tab)) :
        if tab[i] < tab[i_min] :
            i_min = i
    return i_min

assert recherche_min([5]) == 0, "Test 1 failed"
assert recherche_min([2, 4, 1]) == 2, "Test 2 failed"
assert recherche_min([5, 3, 2, 2, 4]) == 2, "Test 3 failed"
assert recherche_min([-1, -2, -3, -3]) == 2, "Test 4 failed"
print("Ex 1 : Tests passed")

# Exercice 2 : sépare 0 et 1

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche] = tab[droite]
            tab[droite] = 1
            droite = droite - 1
    return tab

assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1], "Test 1 failed"
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], "Test 2 failed"
print("Ex 2 : Tests passed")