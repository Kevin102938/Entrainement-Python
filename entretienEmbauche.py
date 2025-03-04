################## Exercices d'entretien d'embauche ##################
# Problème de paranthèses valides :
def isValid(s: str) -> bool:
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in mapping:
            top_elmement = stack.pop() if stack else '#'
            if mapping[char] != top_elmement:
                return False
        else:
            stack.append(char)
    return not stack

    # Exemples de tests
print(isValid("()[]{}"))  # Devrait renvoyer True
print(isValid("(]"))      # Devrait renvoyer False
print(isValid("([{}])"))  # Devrait renvoyer True
print(isValid("{[]}"))    # Devrait renvoyer True
print("####################################\n")


# Somme de deux :

# Inversion d’une chaîne :
def inverse_string(word):
    return word[::-1]

print(inverse_string("Hello"))
print("####################################\n")

# Recherche de nombre manquant :
def missing_number(liste):
    n = len(liste) + 1
    total = n * (n + 1) // 2
    return total - sum(liste)

print(f"le nombre manquant est : ",missing_number([3, 7, 1, 2, 8, 4, 5]))
print("####################################\n")

# Anagrammes :
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# Exemples de tests
print(isAnagram("listen", "silent"))  # Devrait renvoyer True
print(isAnagram("hello", "billion"))  # Devrait renvoyer False
print(isAnagram("anagram", "nagaram"))  # Devrait renvoyer True
print(isAnagram("rat", "car"))  # Devrait renvoyer False
print("####################################\n")


# Renversement de liste chaînée :

# Fusion de deux listes triées :


# Sous-séquence croissante la plus longue :

# Recherche binaire :

# Maximum de sous-tableau (Problème de Kadane) :


# MaxListe: Trouver le maximum dans une liste.
def maxList(lst):
    return max(lst)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(list))

print("####################################\n")
# Factorial: Calculer la factorielle d'un nombre.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) #120

print("####################################\n")
# VerifierParite: Vérifier si un nombre est pair.
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(isEven(4)) #True

print("####################################\n")
# CompterLesVoyelles: Compter le nombre de voyelles dans une chaîne.
def countVowels(s):
    voyelles = "aeiouy"
    count = 0
    for char in s:
        if char in voyelles:
            count += 1
    return count

print(countVowels("hello")) #2
    

print("####################################\n")
# SommeNombres: Calculer la somme des nombres de 1 à n.
def sumToN(n):
    return n * (n + 1) // 2 # formule de la somme des n premiers entiers
    

print(sumToN(5)) #15

print("####################################\n")
# InverserListe: Inverser une liste.
def reverseList(lst):
    return lst[::-1]

print(reverseList([1, 2, 3, 4, 5])) #[5, 4, 3, 2, 1]

print("####################################\n")
# Fibonacci: Retourner le n-ième nombre dans la séquence de Fibonacci.
def fibonacci(n):
    if n <= 1:
       return n
    print("étapes intermédiaires : ",n)
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7)) #13

print("####################################\n")
# TrouverDoublons: Identifier les éléments dupliqués dans une liste.
def findDuplicates(lst):
    duplicates = []
    seen = set() # pour stocker les éléments déjà vus
    for elm in lst:
        if lst.count(elm) > 1 and elm not in seen:
            duplicates.append(elm)
            seen.add(elm)
    return duplicates

print(findDuplicates([1, 2, 3, 4, 5, 5, 6, 6, 7])) #[5, 6]

print("####################################\n")
# CreerPalindrome: Créer un palindrome à partir d'une chaîne donnée.
def createPalindrome(s):
    pass



print("####################################\n")
# SommeChiffres: Calculer la somme des chiffres d'un nombre.
def sumDigits(number):
    separates = []
    for i in str(number):
        separates.append(int(i))
        print(separates)
    return sum(separates)

print(sumDigits(123)) #6

print("####################################\n")