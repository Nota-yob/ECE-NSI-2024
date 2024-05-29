# Exercice 1 : Nombre d'occurences

def nbr_occurrences(chaine:str) -> dict :
    dico = {}
    for lettre in chaine :
        if not lettre in dico :
            dico[lettre] = 1
        else :
            dico[lettre] += 1
    return dico

assert nbr_occurrences("Hello world !") == \
    {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1},\
        "Test 1 failed"
print("Ex 1 : Tests passed")

# Exercice 2 : Fusion tableaux

def fusion(tab1,tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 = i1 + 1
        else:
            tab12[i] = tab2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1]
        i1 = i1 + 1
        i = i+1
    while i2 < n2:
        tab12[i] = tab2[i2]
        i2 = i2 + 1
        i = i+1
    return tab12

assert fusion([1,2,3],[]) == [1,2,3], "Test 1 failed"
assert fusion([], []) == [], "Test 2 failed"
assert fusion([1, 6, 10],[0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10], "Test 3 failed"
print("Ex 2 : Tests passed")