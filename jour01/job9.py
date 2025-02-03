class Produit:
    def __init__(self, nom, prixHT, TVA):
        # Initialisation des attributs du produit
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    # Méthode pour calculer le prix TTC (prix HT + TVA)
    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    # Méthode pour afficher toutes les informations du produit
    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%, Prix TTC: {self.calculerPrixTTC()}"
    
    # Méthodes pour modifier le nom et le prix du produit
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifierPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
    
    # Méthodes pour obtenir les informations du produit
    def getNom(self):
        return self.nom
    
    def getPrixHT(self):
        return self.prixHT
    
    def getTVA(self):
        return self.TVA
    
    def getPrixTTC(self):
        return self.calculerPrixTTC()

# Création de plusieurs produits
produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 200, 10)

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())

# Modification du nom et du prix des produits
produit1.modifierNom("Produit A - Modifié")
produit1.modifierPrix(120)

produit2.modifierNom("Produit B - Modifié")
produit2.modifierPrix(220)

# Affichage des nouvelles informations après modification
print(produit1.afficher())
print(produit2.afficher())