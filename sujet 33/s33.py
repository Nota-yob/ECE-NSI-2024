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