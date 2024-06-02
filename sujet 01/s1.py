# Exercice 1 

a = {
        'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],
        'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']
    }

def taille(arbre, sommet) :
    if sommet == '' :
        return 0
    return 1 + taille(arbre, arbre[sommet][0]) + taille(arbre, arbre[sommet][1])

assert taille(a, 'F') == 9
assert taille(a, 'B') == 5
assert taille(a, 'I') == 2
print("Ex 1 : Tests passed")

# Exercice 2

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N):
        imin = k #Si aucun est inférieur, on va échanger k avec k soit aucun changement
        for i in range(k, N): # on va parcourir les éléments restants
            if tab[i] < tab[imin]: # on boucle et on cherche le plus petit élément
                imin = i # l'indice du plus petit élément est stocké dans imin
        echange(tab, k, imin) # on échange le premier élément des restants (k) avec le plus petit(imin)

tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
assert tab == [6, 12, 18, 21, 25, 41, 55]
print("Ex 2 : Tests passed")