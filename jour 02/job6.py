class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire des plats (nom : prix)
        self.__statut = "en cours"  # Statut initial

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut == "en cours":
            self.__plats_commandes[nom_plat] = prix_plat
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self.__statut = "annulée"
        print("Commande annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        return sum(self.__plats_commandes.values())

    # Méthode pour afficher la commande avec le total
    def afficher_commande(self):
        if self.__plats_commandes:
            print(f"Commande #{self.__numero_commande}:")
            for nom_plat, prix_plat in self.__plats_commandes.items():
                print(f"- {nom_plat}: {prix_plat:.2f} €")
            total = self.__calculer_total()
            print(f"Total à payer: {total:.2f} €")
        else:
            print("Aucun plat dans la commande.")

    # Méthode pour calculer la TVA
    def calculer_TVA(self, taux_tva=0.2):
        total_ht = self.__calculer_total()
        tva = total_ht * taux_tva
        print(f"TVA ({taux_tva * 100}%): {tva:.2f} €")
        return tva

    # Méthode pour terminer la commande
    def terminer_commande(self):
        self.__statut = "terminée"
        print("Commande terminée.")