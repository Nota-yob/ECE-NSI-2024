# Exercice 1 : Température minimale

def annee_temperature_minimale(temp, annees) : 
    n = len(temp)
    i_min = 0
    for i in range(n) : 
        if temp[i] < temp[i_min] :
            i_min = i
    return (temp[i_min], annees[i_min])

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016), "Test 1 failed"
print("Ex 1 : Tests passed")

# Exercice 2 : palindromes


def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat
def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine
def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)

assert inverse_chaine('bac') == "cab"
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True

print("Ex 2 : Tests passed")