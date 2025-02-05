class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut = "en cours"
    
    def ajouter_plat(self, nom_plat, prix):
        if self._statut != "en cours":
            print("Impossible d'ajouter un plat, la commande est terminée ou annulée.")
            return
        self._plats_commandes[nom_plat] = prix
        print(f"{nom_plat} ajouté pour {prix}€.")
    
    def annuler_commande(self):
        self._statut = "annulée"
        self._plats_commandes.clear()
        print("Commande annulée.")
    
    def terminer_commande(self):
        self._statut = "terminée"
        print("Commande terminée.")
    
    def calculer_total(self):
        return sum(self._plats_commandes.values())
    
    def calculer_TVA(self, taux=0.20):
        return self.calculer_total() * taux
    
    def afficher_commande(self):
        print(f"Commande #{self._numero_commande} - Statut: {self._statut}")
        if not self._plats_commandes:
            print("Aucun plat commandé.")
        else:
            for plat, prix in self._plats_commandes.items():
                print(f"- {plat}: {prix}€")
        total = self.calculer_total()
        tva = self.calculer_TVA()
        print(f"Total: {total}€ (TVA: {tva}€)")

# Création d'une commande
commande1 = Commande(101)

# Ajout de plats
commande1.ajouter_plat("Pâtes Carbonara", 12.5)
commande1.ajouter_plat("Pizza Margherita", 10.0)
commande1.ajouter_plat("Tiramisu", 5.5)

# Affichage du total et de la commande
commande1.afficher_commande()

# Terminer la commande
commande1.terminer_commande()

# Tentative d'ajouter un plat après la fin de la commande
commande1.ajouter_plat("Café", 2.0)

# Annulation d'une nouvelle commande
commande2 = Commande(55)
commande2.ajouter_plat("Salade César",15.50)
commande2.afficher_commande()
commande2.annuler_commande()
commande2.afficher_commande()
