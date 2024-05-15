# Exercice : puissances

def liste_puissances(a:int, n:int) -> list :
    liste = [a]
    for i in range(n-1) :
        liste.append(liste[-1]*a)
    return liste

def liste_puissances_borne(a:int, borne:int) -> list :
    if not a < borne :
        return []
    
    liste = [a]
    while liste[-1]*a < borne:
        liste.append(liste[-1]*a)

    return liste

assert liste_puissances(3, 5) == [3, 9, 27, 81, 243], "Test 1 passed"
assert liste_puissances(-2, 4) == [-2, 4, -8, 16], "Test 2 passed"
assert liste_puissances_borne(2, 16) == [2,4,8], "Test 3 passed"
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16], "Test 4 passed"
assert liste_puissances_borne(5, 5) == [], "Test 5 passed"
print("Ex1 : Tests passed")

# Exercice 2 : mot parfait

# to be coded...