# Exercice 1 : voisins entrants graphes orientes

def voisins_entrants(adj:list, x) -> list :
    voisins = []
    for i in range(len(adj)) : # i = indice du sommet
        for v in adj[i] : # v = voisins du sommet i
            if v == x :
                voisins.append(i)
    return voisins

assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1) == [0]
print("Ex 1 : Tests passed")

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat

assert nombre_suivant('1211') == '111221'
assert nombre_suivant('311') == '1321'
print("Ex 2 : Tests passed")