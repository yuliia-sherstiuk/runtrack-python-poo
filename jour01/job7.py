class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def gauche(self):
        self.x -= 1
    def droite(self):
        self.x += 1
    def bas(self):
        self.y += 1
    def haut(self):
        self.y -= 1
    
    def position(self):
        return (self.x, self.y)

personnage = Personnage(5, 4)
print("Position initiale:", personnage.position())

personnage.gauche()  
personnage.haut()    
print("Nouvelle position:", personnage.position())

personnage.droite()  
personnage.bas()    
print("Position après déplacements:", personnage.position())