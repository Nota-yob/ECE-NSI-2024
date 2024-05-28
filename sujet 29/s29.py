# Exercice 1 : moyenne

def moyenne(notes:list) -> float :
    somme = 0
    effectifs = 0
    for note, coef in notes :
        somme += note*coef
        effectifs += coef
    return somme / effectifs

assert moyenne([(15.0,2),(9.0,1),(12.0,3)]) == 12.5, "Test 1 failed"
print("Ex 1 : Tests passed")

# Exercice 2 : triangle de Pascal

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1]
    for i in range(len(ligne) - 1):
        ligne_suiv.append(ligne[i]+ligne[i+1])
    ligne_suiv.append(1)
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle

assert ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1], "Test 1 failed"
assert pascal(2) == [[1], [1, 1], [1, 2, 1]], "Test 2 failed"
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]], "Test 3 failed"