# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

# # Afficher le résultat
# print(fibo(10))  # Affichera le 10e terme de la suite de Fibonacci


def fiboRec(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Afficher la suite complète
print(fiboRec(10))  # Affichera [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
