class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  
        self.__largeur = largeur 

    #Assesseurs (get)
    def get_longueur(self):  
        return self.__longueur
    
    def get_largeur(self):   
        return self.__largeur
    
    #Mutateurs(set)

    def set_longueur(self, longueur):
        if longueur > 0:
            self.__longueur = longueur
        else:
            raise ValueError("La longueur doit être un nombre positif")
    
    def set_largeur(self, largeur):
        if largeur > 0:
            self.__largeur = largeur
        else:
            raise ValueError("La largeur doit être un nombre positif")
    
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)


    def surface (self): 
         return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longeuer, largeur, hauteur):
        super().__init__(longeuer, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        if hauteur > 0:
            self.__hauteur = hauteur
        else:
            raise ValueError("La valleur doit etre un nombre positif")
        
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.get_hauteur()
   #test

rectangle = Rectangle(5, 7) 
print("perimetr du rectangle:", rectangle.perimetre())
print("surface du rectangle:", rectangle.surface())   

parallelepipede = Parallelepipede(2, 3, 4)
print("Volume du parallélépipède:", parallelepipede.volume())
        
               



       
    
