# Exercice 1 : mot dans phrase

def nombre_de_mots(phrase:str) -> int :
    mots = 0
    for lettre in phrase :
        if lettre == " " :
            mots += 1
        elif lettre == "." :
            # on ajoute un mot pcq pas d'espace
            mots += 1
            break
        elif lettre in ["!", "?"] :
            # on enlève ni ajoute de mot pcq déjà fait par l'espace
            break
    return mots

assert nombre_de_mots('Cet exercice est simple.') == 4, "Test 1 failed"
assert nombre_de_mots('Le point d exclamation est séparé !') == 6, "Test 2 failed"
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10, "Test 3 failed"
assert nombre_de_mots('Fin.') == 1, "Test 4 failed"
print("Ex1 : Tests passed")

# Exercice 2 : ABR

class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None :
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
assert arbre.gauche.etiquette == 3, "Test 1 failed"
assert arbre.droit.etiquette == 9, "Test 2 failed"
assert arbre.gauche.gauche.etiquette == 1, "Test 3 failed"
assert arbre.gauche.droit.etiquette == 6, "Test 4 failed"
print("Ex2 : Tests passed")