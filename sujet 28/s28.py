# Exercice 1 : fibonacci

def fibonacci(n) :
      if n < 3 :
            return 1
      return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025
print("Ex 1 : Tests passed")

# Exercice 2 : élève du mois

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(notes)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h']), "Test 1 passed"
assert eleves_du_mois([],[]) == (0, []), "Test 2 passed"
print("Ex 2 : Tests passed")

