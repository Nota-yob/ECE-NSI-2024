# Exercice 1 : moyenne

def moyenne(tab) : 
    s = 0
    for val in tab :
        s += val
    return s/len(tab)
assert moyenne([1]) == 1.0
assert moyenne([1,2,3,4,5,6,7]) == 4.0
assert moyenne([1,2]) == 1.5
print("Ex 1 : Tests passed")

# Exercice 2 : dichotomie

def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut + fin) // 2 
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m -1 
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27) == False
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1) == False
assert dichotomie([], 28) == False
print("Ex 2 : Tests passed")