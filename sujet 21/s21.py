# Exercice 1 : recherche motifs

def recherche_motif(motif:str, texte:str) -> list :
    liste = []
    for i in range(len(texte) - len(motif) + 1) :
        j = 0
        while j < len(motif) and texte[i+j] == motif[j] :
            j += 1
        if j == len(motif) :
            liste.append(i)
    return liste

assert recherche_motif("ab", "abracadabra") == [0, 7], "Test 1 failed"
assert recherche_motif("ab", "") == [], "Test 2 failed"
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11], "Test 3 failed"
print("Ex1 : Tests passed")
        
# Exercice 2 : graphe parcours

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc

assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0) == [0, 1, 2, 3], "Test 1 passed"
assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4) == [4, 5], "Test 2 passed"
print("Ex2 : Tests passed")