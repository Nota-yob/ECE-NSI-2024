# Exercice 1

def correspond(mot, mot_a_trous) :
    if len(mot) != len(mot_a_trous) :
        return False
    for i in range(len(mot_a_trous)) :
        if mot_a_trous[i] != "*" and mot_a_trous[i] != mot[i]:
            return False
    return True

assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False
assert correspond('AUTO', '*UT*') == True
print("Ex 1 : Tests passed")

# Exercice 2
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.'''

    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires = nb_destinataires + 1
    return nb_destinataires == len(plan)

assert est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'}) == False
assert est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}) == True
assert est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'}) == True
assert est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'}) == False
print("Ex 2 : Tests passed")