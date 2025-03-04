import tkinter as tk
from tkinter import messagebox

def calculer_pourboires():
    try:
        # Récupérer les valeurs des champs d'entrée
        addition = float(entry_addition.get())
        pourcentage = float(entry_pourcentage.get())
        personnes = int(entry_personnes.get())

        if addition <= 0 or pourcentage <= 0 or personnes <= 0:
            raise ValueError("Toutes les valeurs doivent être positives.")

        # Calculs
        pourboire = (addition * pourcentage) / 100
        total = addition + pourboire
        total_par_personne = total / personnes

        # Afficher les résultats
        result_pourboire.config(text=f"Pourboire : {pourboire:.2f} €")
        result_total.config(text=f"Total à payer : {total:.2f} €")
        result_par_personne.config(text=f"Par personne : {total_par_personne:.2f} €")
    except ValueError as e:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")
    except ZeroDivisionError:
        messagebox.showerror("Erreur", "Le nombre de personnes doit être supérieur à 0.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculateur de pourboires")

# Widgets pour les entrées utilisateur
tk.Label(root, text="Montant de l'addition (€) :").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_addition = tk.Entry(root)
entry_addition.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Pourcentage du pourboire (%) :").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pourcentage = tk.Entry(root)
entry_pourcentage.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Nombre de personnes :").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_personnes = tk.Entry(root)
entry_personnes.grid(row=2, column=1, padx=10, pady=5)

# Bouton pour effectuer le calcul
btn_calculer = tk.Button(root, text="Calculer", command=calculer_pourboires)
btn_calculer.grid(row=3, column=0, columnspan=2, pady=10)

# Widgets pour afficher les résultats
result_pourboire = tk.Label(root, text="", fg="green")
result_pourboire.grid(row=4, column=0, columnspan=2, pady=5)

result_total = tk.Label(root, text="", fg="green")
result_total.grid(row=5, column=0, columnspan=2, pady=5)

result_par_personne = tk.Label(root, text="", fg="green")
result_par_personne.grid(row=6, column=0, columnspan=2, pady=5)

# Lancer la boucle principale de la fenêtre
root.mainloop()
