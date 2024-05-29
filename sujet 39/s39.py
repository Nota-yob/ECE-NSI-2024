# Exercice 1 : recherche élément in liste

def recherche(elt, tab) :
    i_val = None
    for i in range(len(tab)) :
        if tab[i] == elt :
            i_val = i
    return i_val

