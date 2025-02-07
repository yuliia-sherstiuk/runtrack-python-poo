class Rectangle:
    def __init__ (self, langeuer, largeur):
        self.__langeuer = langeuer
        self.__largeur = largeur

    #Assesseurs (get)
    def get_langeuer(self):
        return self.__langeuer
    
    def get_largeur (self):
        return self.__largeur
    
    #Mutateurs(set)

    def set_longueur(self, longueur):
        if longueur > 0:
            self.__longueur = longueur

    def set_largeur(self, largeur): 
        if largeur > 0:
            self.__largeur = largeur 
    


    def perimetre (self)
        return  2 * (self.__largeur + self.__langeuer)


    def surface (self) 
        return self.__langeuer * self.__largeur

    
       
     class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale du {self.name}: {self.max_speed} nœuds.")
  