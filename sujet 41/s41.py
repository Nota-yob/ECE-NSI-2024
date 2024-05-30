# Exercice 1 : taille noeud binaire

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

def taille(arbre:Noeud) :
    if arbre is None :
        return 0
    return 1 + taille(arbre.gauche) + taille(arbre.droit)

def hauteur(arbre:Noeud) :
    if arbre is None : 
        return -1
    if hauteur(arbre.droit) > hauteur(arbre.gauche) :
        return 1 + hauteur(arbre.droit)
    else :
        return 1 + hauteur(arbre.gauche)

a = Noeud(1, Noeud(4, None, None),
Noeud(0, None,
Noeud(7, None, None)))

assert hauteur(a) == 2
assert taille(a) == 4
assert hauteur(None) == -1
assert taille(None) == 0
assert hauteur(Noeud(1, None, None)) == 0
assert taille(Noeud(1, None, None)) == 1
print("Ex 1 : Tests passed")

# Exercice 2 : ajoute valeur in tableau

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i]
    tab_ins[indice] = element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1]
    return tab_ins

assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(0, 4, [7, 8, 9]) == [4, 7, 8, 9]
print("Ex 2 : Tests passed")