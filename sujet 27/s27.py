# Exercice 1 : couples consécutifs

def couples_consecutifs (tab:list) -> list :
    couples = []
    for i in range(len(tab) -1) :
        if tab[i] == tab[i+1] - 1 :
            couples.append((tab[i], tab[i+1]))
        i = i+1
    return couples
assert couples_consecutifs([1, 4, 3, 5]) == [], "Test 1 failed"
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)], "Test 2 failed"
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)], "Test 3 failed"
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)], "Test 4 failed"
assert couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)], "Test 5 failed"
print("Ex 1 : Tests passed")

# Exercice 2 : composante de pixels
"""
Part d'un pixel 1 et va donner la même valeurs à tous les pixels voisins
Si pixel n'est pas 1, return
Quand toutes les récursions ont return, on a visité tous les pixels 1 voisins
"""
def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return
    M[i][j] = val
    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage à droite
        colore_comp1(M, i+1, j, val)
    if j-1 >= 0: # propage en haut
        colore_comp1(M, i, j-1, val)
    if j+1 < len(M[i]): # propage en bas
        colore_comp1(M, i, j+1, val)

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]

print("Ex 2 : Tests passed")