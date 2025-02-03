class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont : ({self.x}, {self.y})")
    def afficherX(self):
        print(f"Coordonnée x : {self.x}")
    def afficherY(self):
        print(f"Coordonnée y : {self.y}")
    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur
        print(f"Nouvelle coordonnée x : {self.x}")
    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur
        print(f"Nouvelle coordonnée y : {self.y}")

point1 = Point(3, 4)
point1.afficherLesPoints()  

point1.afficherX()  
point1.afficherY()  
point1.changerX(5)  
point1.changerY(6)  
point1.afficherLesPoints()  
