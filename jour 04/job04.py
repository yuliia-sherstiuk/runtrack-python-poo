class Forme:
    def aire(self):
        return 0

class Rectangle (Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
  
rectangle = Rectangle(15, 10)
print ("l'aire du rectangle est:", rectangle.aire())  

