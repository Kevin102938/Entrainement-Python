entrée = [1, 2, 3, 4, 5, 6]
sortie = [4, 8, 12]  # car seuls les nombres pairs (2, 4, 6) sont doublés
print(entrée)
exclure = [x*2 for x in entrée if x % 2 == 0]
print (exclure)