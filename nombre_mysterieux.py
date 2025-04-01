from random import *

maxi = int(input("Entrez la valeur maximale du nombre mystérieux : "))
nombre_mysterieux=randint(1,maxi)
n_saisie=input(f"Entrez un nombre entre 1 et {maxi} : ")
n=int(n_saisie)
i = 1

while(n!=nombre_mysterieux):
    if n>nombre_mysterieux:
            print("Le nombre mystérieux est inférieur à",n)
    if n<nombre_mysterieux:
            print("Le nombre mystérieux est supérieur à",n)
    n=int(input("Entrez un autre nombre entre 1 et 100 : "))
    i+=1

print("Bravo ! Vous avez trouvé le nombre mystérieux :",n)
print("Nombre de tentatives :",i)