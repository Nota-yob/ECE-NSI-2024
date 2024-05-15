# Exercice 1 : multiplication

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
print("Ex1 : Tests passed")

# Exercice 2 : recherche dichotomie

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab,
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m+1 , j)
    elif tab[m] > x:
        return chercher(tab, x, i , m-1)
    else:
        return m

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None, "Test 1 failed"
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None, "Test 2 failed"
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4, "Test 3 failed"
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2, "Test 4 failed"
print("Ex2 : Tests passed")