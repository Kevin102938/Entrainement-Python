s = "Python permet de manipuler facilement les chaînes de caractères"
print(s)
print(s[0])
print(s[1])

s2 = s.replace("Python", "Java")
print(s2)

s3 = s.split(" ")  
print(s3)

s4 = " ".join(s3)
print(s4)

# Trie d'une chaîne de caractères 
liste = ["Python", "Java", "C++", "JavaScript", "Ruby"]
listeN = [5, 3, 8, 1, 2]
liste.sort()
listeN.sort()
print(liste, listeN)


# Liste position

position = [1,2,3,4,5,6,7,8,9,10]
print(position.index(3))
print(position[0])
print(position[-1])

positionReverse = position[::-1]
print(position)
print(positionReverse)

