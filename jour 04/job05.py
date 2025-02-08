class Forme:
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        pi = 3.14159
        return pi * self.radius ** 2
    
cercle = Cercle (10)

cercle = Cercle (7)

print("L'aire du cercle est :", cercle.aire())  