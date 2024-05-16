# Exercice : puissances

def liste_puissances(a:int, n:int) -> list :
    liste = [a]
    for i in range(n-1) :
        liste.append(liste[-1]*a)
    return liste

def liste_puissances_borne(a:int, borne:int) -> list :
    if not a < borne :
        return []
    
    liste = [a]
    while liste[-1]*a < borne:
        liste.append(liste[-1]*a)

    return liste

assert liste_puissances(3, 5) == [3, 9, 27, 81, 243], "Test 1 passed"
assert liste_puissances(-2, 4) == [-2, 4, -8, 16], "Test 2 passed"
assert liste_puissances_borne(2, 16) == [2,4,8], "Test 3 passed"
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16], "Test 4 passed"
assert liste_puissances_borne(5, 5) == [], "Test 5 passed"
print("Ex1 : Tests passed")

# Exercice 2 : mot parfait

dico = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
    "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
    "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
    "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
    "W": 23, "X": 24, "Y": 25, "Z": 26
    }

def codes_parfait(mot):
    """Renvoie un triplet
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est
    parfait."""
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    mot_est_parfait = code_concatene % code_additionne == 0
    return code_additionne, code_concatene, mot_est_parfait

assert codes_parfait("PAUL") == (50, 1612112, False), "Test 1 failed"
assert codes_parfait("ALAIN") == (37, 1121914, True), "Test 2 failed"
print("Ex2:  Tests passed")