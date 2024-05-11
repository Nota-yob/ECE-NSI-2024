# Exercice 1 : delta encoding

def delta(liste:list) -> list :
    encoded = []
    previous = None

    for ele in liste :
        if previous is None :
            encoded.append(ele)
        else :
            encoded.append(ele-previous)

        previous = ele
    return encoded

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3], "Test 1 failed"
assert delta([42]) == [42], "Test 2 failed"

print("Ex1 : Tests passed")

# Exercice 2 : expression arithmétique

class Expr:
    """Classe implémentant un arbre d'expression."""
    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None
    
    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = ""
        if self.gauche is not None:
            s = '(' + s + self.gauche.infixe()
        s = s + str(self.valeur)
        if self.droite is not None:
            s = s + self.droite.infixe() + ')'
        return s

a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
assert a.infixe() == '(1+2)', "Test 1 failed"
b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)),
        '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None))
        )
assert b.infixe() == '((1+2)*(3+4))', "Test 2 failed"
e = Expr(
Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None),
'+', Expr(None, 7, None))),
'-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
assert e.infixe() == '((3*(8+7))-(2+1))', "Test 3 failed"

print("Ex2 : Tests passed")