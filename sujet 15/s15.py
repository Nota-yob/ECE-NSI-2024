# Exercice 1 : moyenne

def moyenne(tab:list) -> float :
    somme = 0
    for val in tab :
        somme += val
    return somme / len(tab)

assert moyenne([1.0]) == 1.0, "Test 1 failed"
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335, "Test 2 failed"
print("Ex1 : Tests passed")

# Exercice 2 : binaire

def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ""
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

assert binaire(83) == '1010011', "Test 1 failed"
assert binaire(6) == '110', "Test 2 failed"
assert binaire(127) == "1111111", "Test 3 failed"
assert binaire(0) == "0", "Test 4 failed"
print("Ex2 : Tests passed")