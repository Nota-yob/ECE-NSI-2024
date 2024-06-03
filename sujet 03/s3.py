# Exercice 1 : Max liste

def maximum_tableau(tab:list) -> list :
    max = tab[0]

    for val in tab :
        if val > max :
            max = val
    
    return max

assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131, "Test 1 failed"
assert maximum_tableau([-27, 24, -3, 15]) == 24, "Test 2 failed"
print("Ex 1 : Tests passed")


# Exercice 2 : Parenthésage

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []
    
    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def bon_parenthesage(ch):
    """Renvoie un booléen indiquant si la chaîne ch
    est bien parenthésée"""
    p = Pile()
    for c in ch:
        if c == "(" :
            p.empiler(c)
        elif c == ")":
            if p.est_vide():
                return False
            else:
                p.depiler()
    return p.est_vide()

assert bon_parenthesage("((()())(()))") == True, "Test 1 failed"
assert bon_parenthesage("())(()") == False, "Test 2 failed"
assert bon_parenthesage("(())(()") == False, "Test 3 failed"
print("EX 2 : tests passed")