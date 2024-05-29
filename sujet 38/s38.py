# Exercice 1 : indices maxi

def indices_maxi(tab) :
    maxi = tab[0]
    indices = [] # va être append car 1e val = maxi
    for i in range(len(tab)) : 
        if tab[i] > maxi :
            maxi = tab[i]
            indices = [i]
        elif tab[i] == maxi :
            indices.append(i)
    return (maxi, indices)

assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])
print("Ex 1 : Tests passed")

# Exercice 2 : pile entiers

def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse
def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        entier = pile.pop()
        if entier >= 0:
            pile_positifs.append(entier)
    return renverse(pile_positifs)

assert  renverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "Test 1 failed"
assert positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9], "Test 2 failed"
print("Ex 2 : Tests passed")