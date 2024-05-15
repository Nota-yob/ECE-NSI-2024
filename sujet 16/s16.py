# Exercice 1 : binaire

def ecriture_binaire_entier_positif(n:int) -> str :
    if n == 0 : return '0'
    binaire = ""
    while n != 0 :
        binaire = str(n % 2) + binaire
        n = n // 2
    return binaire

assert ecriture_binaire_entier_positif(0) == '0', "Test 1 failed"
assert ecriture_binaire_entier_positif(2) == '10', "Test 2 failed"
assert ecriture_binaire_entier_positif(105) == "1101001", "Test 3 failed"
print("Ex1 : Tests passed")

# Exercice 2 : tri bulle

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1]:
                echange(tab, j, j+1)

tab = []
tri_bulles(tab)
assert tab == [], "Test 1 failed"

tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
assert tab2 == [1, 2, 3, 3, 6, 7, 9], "Test 2 failed"

tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
assert tab3 == [3, 4, 7, 9], "Test 3 failed"

print("Ex2 : Tests passed")