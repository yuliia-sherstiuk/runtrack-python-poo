# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}")
        print(f"Model : {self.modele}")
        print(f"Anne: {self.annee}")
        print(f"Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")
# Classe Voiture   
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
         super().informationsVehicule()
         print(f"Nombre de porte: {self.portes}")

    def demarrer(self):
        print("La voiture démarre: Attention, je roule en voiture !")
        
# Classe Moto
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print(f"La moto démarre: Attention, je roule à moto !")

#objet Voiture
voiture = Voiture("Mersedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()
voiture.demarrer()

print()

#  objet Moto
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
moto.demarrer()       