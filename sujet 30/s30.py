# Exercice 1 : fusion

def fusion(tab1:list, tab2:list) -> list :
    tab = tab1 + tab2
    for k in range(len(tab)) :
        i_min = k
        for i in range(k, len(tab)) :
            if tab[i] < tab[i_min] :
                i_min = i
        tmp = tab[k]
        tab[k] = tab[i_min]
        tab[i_min] = tmp
    return tab
assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]
assert fusion([], []) == []
assert fusion([1, 2, 3], []) == [1, 2, 3]
print("Ex 1 : Tests passed")

# Exercice 2 : Traduire chiffres romains to base 10
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """

    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]

assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIV") == 2024
print("Ex 2 : Tests passed")