# Exercice 1 : multiplication (idem sujet 18)

def multiplication(n1:int, n2:int) -> int :
    result = 0
    for i in range(abs(n1)) :
        if n1 < 0 :
            result -= n2
        else : 
            result += n2
    return result

assert multiplication(3, 5) == 15, "Test 1 failed"
assert multiplication(-4, -8) == 32, "Test 2 failed"
assert multiplication(-2, 6) == -12, "Test 3 failed"
assert multiplication(-2, 0) == 0, "Test 4 failed"
print("Ex 1 : Tests passed")


# Exercice 2 : dichotomie

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = fin - 1
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False
print("Ex 2 : Tests passed")