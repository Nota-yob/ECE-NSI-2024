# Exercice 1 : parcours largeur

def parcours_largeur(arbre:tuple) -> list :
    parcours = []
    file = [arbre]
    while file :
        a = file.pop(0)
        parcours.append(a[1])
        if a[0] is not None :
            file.append(a[0])
        if a[2] is not None :
            file.append(a[2])
    return parcours

arbre = ( ( (None, 1, None), 2, (None, 3, None) ),
4,
( (None, 5, None), 6, (None, 7, None) ) )
assert parcours_largeur(arbre) == [4, 2, 6, 1, 3, 5, 7], "Test 1 failed"
print("Ex1 : Tests passed")

# Exercice 2 : plus grande somme consécutive

def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if tab[i] + sommes_max[i-1] > tab[i] :
            sommes_max[i] = tab[i] + sommes_max[i-1]
        else:
            sommes_max[i] = tab[i]
    # on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum] :
            maximum = i
    return sommes_max[maximum]

assert somme_max([1, 2, 3, 4, 5]) == 15, "Test 1 failed"
assert somme_max([1, 2, -3, 4, 5]) == 9, "Test 2 failed"
assert somme_max([1, 2, -2, 4, 5]) == 10, "Test 3 failed"
assert somme_max([1, -2, 3, 10, -4, 7, 2, -5]) == 18, "Test 4 failed"
print("Ex2 : Tests passed")