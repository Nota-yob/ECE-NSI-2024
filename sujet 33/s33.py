# Exercice 1 : renverse

def renverse(string:str) :
    inverse = ""
    for lettre in string :
        inverse = lettre + inverse
    return inverse

assert renverse("") == ""
assert renverse("abc") == "cba"
assert renverse("informatique") == "euqitamrofni"
print("Ex 1 : Tests passed")

# Exercice 2 : Crible 

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2*i
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], "Test 1 failed"
assert crible(5) == [2, 3], "Test 2 failed"
print("Ex 2 : Tests passed")