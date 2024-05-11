# Exercice 1 : recherche

def recherche(tab:list, n:int) :
    found_i = None
    for i in range(len(tab)) :
        if tab[i] == n : found_i = i
    return found_i

assert recherche([5, 3],1) == None, "Test 1 failed"
assert recherche([2,4],2) == 0, "Test 2 failed"
assert recherche([2,3,5,2,4],2) == 3, "Test 3 failed"

print("Ex1 : Tests passed")


# Exercice 2 : point le plus proche

def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre
    deux points."""
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = distance_carre(min_point, depart)
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < min_dist:
            min_point = tab[i]
            min_dist = distance_carre(tab[i], depart)
    return min_point

assert distance_carre((1, 0), (5, 3)) == 25, "Test 1 failed"
assert distance_carre((1, 0), (0, 1)) == 2, "Test 2 failed"
assert point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)]) == (2,5), "Test 3 failed"
assert point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)]) == (5,2), "Test 4 failed"

print("Ex2 : Tests passed")