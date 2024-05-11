# Exercice 1 : moyenne pondérée

def moyenne(notes:list) -> float :
    somme = 0
    effectif = 0
    for note in notes :
        somme += note[0]*note[1]
        effectif += note[1]
        
    if effectif == 0 : return None

    return somme/effectif

assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142, "Test 1 failed"
assert moyenne([(3, 0), (5, 0)]) == None, "Test 2 failed"

print("Ex1 : Tests passed")

# Exercice 2 : dessins pixels

def  affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
    des "*" , les 0 par un espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)

def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
    liste_depart'''
    liste_zoomee = []
    for elt in liste_depart :
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
    ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee

coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

#affiche(coeur)
#print('\n')
#affiche(dessin_zoom(coeur,2))
assert liste_zoom([1,2,3],3) == [1, 1, 1, 2, 2, 2, 3, 3, 3], "Test 1 failed"
print("Ex2 : Tests passed")