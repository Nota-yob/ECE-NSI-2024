# Exercice 1 : ajoute dictionnaire

def ajoute_dictionnaires(d1:dict, d2:dict) -> dict :
    d = d1
    for kd2 in d2 :
        if not kd2 in d :
            d[kd2] = d2[kd2]
        else :
            d[kd2] += d2[kd2]
    return d

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}, "Test 1 failed"
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}, "Test 2 failed"
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}, "Test 3 failed"
print("Ex 1 : Tests passed")

# Exercice 2 : jeu pion

from random import randint

def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0
    while nombre_cases_vues < nombre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if not cases_vues[case_en_cours] :
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues + 1
        n = n + 1
    assert check_cases_vues(cases_vues), "Test 1 failed"
    assert nombre_cases_vues == nombre_cases, "Test 2 failed"
    assert n >= nombre_cases, "Test 3 failed"
    return n

def check_cases_vues(cases_vues) :
    for case in cases_vues :
        if case is False :
            return False
    return True

nombre_coups()
print("Ex 2 : Tests passed")