# Dictionnaire du code Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'  # "/" représente les espaces
}

# Fonction pour convertir une phrase en code Morse
def texte_vers_morse(texte):
    morse = []
    for lettre in texte.upper():  # Convertir en majuscules pour correspondre aux clés du dictionnaire
        if lettre in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[lettre])
        else:
            morse.append('?')  # Utiliser "?" pour les caractères non supportés
    return ' '.join(morse)

# Demander à l'utilisateur de saisir une phrase
texte = input("Entrez une phrase à convertir en code Morse : ")

# Convertir la phrase et afficher le résultat
morse = texte_vers_morse(texte)
print("Code Morse :", morse)
