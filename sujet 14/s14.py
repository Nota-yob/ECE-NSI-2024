# Exercice 1 : min max

def min_et_max(tab:list) -> dict :
    dico = {
        "min": tab[0],
        "max": tab[0]
    }
    for ele in tab :
        if ele < dico["min"] :
            dico["min"] = ele
        if ele > dico["max"] :
            dico["max"] = ele
    return dico

assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}, "Test 1 failed"
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}, "Test 2 failed"
assert min_et_max([3]) == {'min': 3, 'max': 3}, "Test 3 failed"
assert min_et_max([1, 3, 2, 1, 3]) == {'min': 1, 'max': 3}, "Test 4 failed"
assert min_et_max([-1, -1, -1, -1, -1]) == {'min': -1, 'max': -1}, "Test 5 failed"
print("Ex1 : Tests passed")

# Exercice 2 : 

class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4),
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v
    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte :
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]
    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        self.contenu = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.contenu.append(Carte(i, j))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos
        (entier compris entre 0 et 51). """
        assert 0 <= pos <= 51, "La position de la carte est incorrecte"
        return self.contenu[pos]

jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)
carte2 = jeu.recuperer_carte(0)
assert carte1.recuperer_valeur() == "8", "Test 1 failed"
assert carte1.recuperer_couleur() == "coeur", "Test 2 failed"
assert carte2.recuperer_valeur() == "As", "Test 3 failed"
assert carte2.recuperer_couleur() == "pique", "Test 4 failed"
try:
    carte3 = jeu.recuperer_carte(52)
except:
    pass
    print("Ex2 : Tests passed")
