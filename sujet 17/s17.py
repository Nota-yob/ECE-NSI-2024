# Exercice 1 : répétition

def nb_repetitions (elt, tab:list) -> int :
    counter = 0
    for element in tab :
        if element == elt :
            counter += 1
    return counter

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3, "Test 1 failed"
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2, "Test 2 failed"
assert nb_repetitions(12, [1, '!', 7, 21, 36, 44]) == 0, "Test 3 failed"
print("Ex1 : Tests passed")

# Exercice 2 : binaire

def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ""
    while a != 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

assert binaire(0) == '0', "Test 1 failed"
assert binaire(77) == '1001101', "Test 2 failed"
print("Ex2 : Tests passed")