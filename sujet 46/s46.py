# Exercice 1 : recherche indice valeur

def recherche(tab:list, n:int) :
    g = 0
    d = len(tab) - 1
    while g < d :
        m = (d + g) // 2
        if n < tab[m] :
            d = m - 1
        elif n > tab[m] :
            g = m + 1
        else :
            return m

assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == None
print("Ex 1 : Tests passed")

# Exercice 2 : chiffrement césar

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
print("Ex 2 : Tests passed")