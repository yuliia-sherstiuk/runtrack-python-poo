import random

# Classe Carte représentant une carte avec sa valeur et couleur
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

# Classe Jeu représentant le paquet de cartes et gérant les opérations du jeu
class Jeu:
    couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in Jeu.valeurs for couleur in Jeu.couleurs]
        random.shuffle(self.paquet)

    def distribuer(self):
        return self.paquet.pop()

# Fonction pour calculer la valeur totale d'une main
def calculer_main(main):
    total = 0
    nombre_as = 0

    # Calcul initial, les As sont considérés comme 11 pour l'instant
    for carte in main:
        if carte.valeur in ['Valet', 'Dame', 'Roi']:
            total += 10
        elif carte.valeur == 'As':
            total += 11
            nombre_as += 1
        else:
            total += int(carte.valeur)

    # Si le total dépasse 21 et qu'il y a des As, on les compte comme 1
    while total > 21 and nombre_as > 0:
        total -= 10
        nombre_as -= 1

    return total

# Fonction principale pour jouer une partie
def jouer_blackjack():
    jeu = Jeu()
    main_joueur = [jeu.distribuer(), jeu.distribuer()]
    main_croupier = [jeu.distribuer(), jeu.distribuer()]

    print(f"Main du joueur : {main_joueur}, total = {calculer_main(main_joueur)}")
    print(f"Main du croupier : {main_croupier[0]}, ?")

    # Tour du joueur
    while True:
        action = input("Voulez-vous 'prendre' une carte ou 'passer' ? (prendre/passer) : ")
        if action == 'prendre':
            main_joueur.append(jeu.distribuer())
            total_joueur = calculer_main(main_joueur)
            print(f"Vous avez pris : {main_joueur[-1]}, total = {total_joueur}")

            if total_joueur > 21:
                print("Vous avez dépassé 21, vous avez perdu !")
                return
        else:
            break

    # Tour du croupier
    print(f"Main du croupier : {main_croupier}, total = {calculer_main(main_croupier)}")
    while calculer_main(main_croupier) < 17:
        main_croupier.append(jeu.distribuer())
        print(f"Le croupier tire : {main_croupier[-1]}, total = {calculer_main(main_croupier)}")

    # Résultat final
    total_joueur = calculer_main(main_joueur)
    total_croupier = calculer_main(main_croupier)

    print(f"Main finale du joueur : {main_joueur}, total = {total_joueur}")
    print(f"Main finale du croupier : {main_croupier}, total = {total_croupier}")

    if total_croupier > 21 or total_joueur > total_croupier:
        print("Félicitations, vous avez gagné !")
    elif total_joueur == total_croupier:
        print("Égalité !")
    else:
        print("Le croupier a gagné !")

# Lancer une partie
if __name__ == "__main__":
    jouer_blackjack()