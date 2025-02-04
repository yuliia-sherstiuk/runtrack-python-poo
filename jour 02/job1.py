class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Getters
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Setters
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    # Affichage du rectangle
    def afficher(self):
        print(f"Rectangle: Longueur = {self.__longueur}, Largeur = {self.__largeur}")


# Création d'un rectangle avec longueur = 10 et largeur = 5
rect = Rectangle(10, 5)
rect.afficher()

# Modification des attributs
rect.set_longueur(25)
rect.set_largeur(15)
rect.afficher()