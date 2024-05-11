# Exercice 1 : vérifie trié

def verifie(tab:list) -> bool :
    for i in range(len(tab)-1) :
        if tab[i] > tab[i+1] :
            return False
    return True

assert verifie([0, 5, 8, 8, 9]) == True, "Test 1 failed"
assert verifie([8, 12, 4]) == False, "Test 2 failed"
assert verifie([-1, 4]) == True, "Test 3 failed"
assert verifie([]) == True, "Test 4 failed"
assert verifie([5]) == True, "Test 5 failed"

print("Ex1 : Tests passed")

# Exercice 2 : vote

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat


def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre
    de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
        liste_finale = [ nom for nom in election if election[nom] == nmax ]
    return liste_finale

assert depouille([ 'A', 'B', 'A' ]) == {'A': 2, 'B': 1}, "Test 1 failed"
assert depouille([]) == {}, "Test 2 failed"
election = depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B'])
assert election == {'A': 3, 'B': 4, 'C': 3}, "Test 3 failed"
assert vainqueurs(election) == ['B'], "Test 4 failed"
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) == ['A', 'B'], "Test 5 failed"

print("Ex2 : Tests passed")