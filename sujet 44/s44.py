# Exercice 1 : énumère

def enumere(tab:list) :
    d = {}
    for i in range(len(tab)) :
        if not tab[i] in d :
            d[tab[i]] = []
        d[tab[i]].append(i)
    return d

assert enumere([]) == {}
assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}
print("Ex 1 : Tests passed")

# Exercice 2 : arbre binaire, parcours, insertion

class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if arbre.etiquette > cle:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
        return arbre
    
arbre = Noeud(5, Noeud(2, None, Noeud(3, None, None)), Noeud(7, None, None))
liste = []
parcours(arbre, liste)
assert liste == [2,3,5,7]
insere(arbre, 1)
liste = []
parcours(arbre, liste)
assert liste == [1,2,3,5,7]
insere(arbre, 4)
liste = []
parcours(arbre, liste)
assert liste == [1,2,3,4,5,7]
insere(arbre, 6)
liste = []
parcours(arbre, liste)
assert liste == [1,2,3,4,5,6,7]
insere(arbre, 8)
liste = []
parcours(arbre, liste)
assert liste == [1,2,3,4,5,6,7,8]
print("Ex 2 : Tests passed")