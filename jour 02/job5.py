class Voiture :
    def __init__(self, marque, modèle, année, kilométrage, en_marche = False, reservoir = 50):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Assesseurs (getters) pour obtenir les valeurs des attributs
    def get_marque(self):         
        return self.__marque
    def get_modele(self) :
        return self.__modèle
    def get_année(self) :
        return self.__année
    def get_kilomètrage(self) :
        return self.__kilométrage
    def get_status(self) :
        return self.__en_marche

    # Mutateurs (setters) pour modifier les valeurs des attributs
    def set_marque(self, new_marque):         
        self.__marque = new_marque
        return self.__marque
    def set_modele(self, new_modele) :
        self.__modèle = new_modele
        return self.__modèle
    def set_année(self, new_année) :
        self.__année = new_année
        return self.__année
    def set_kilomètrage(self, new_kilo) :
        self.__kilométrage =new_kilo
        return self.__kilométrage
    def set_status(self, new_status) :
        if self.__en_marche :
            new_status = True
        else :
            new_status = self.__en_marche
        return new_status

  
   

    # Méthode pour démarrer la voiture
    def démarrer(self) :
        if self.__verifier_plein() > 5 :
            self.__en_marche = True
        return self.__en_marche

    def arrêter(self) :
        self.__en_marche = False    
        return self.__en_marche
    
    def __verifier_plein(self) :
        return self.__reservoir
    
    def set_reservoir(self, new_value) :
        self.__reservoir = new_value
        return self.__reservoir
    #add a method that prints the car's information

    def afficher(self) :
        return f"Les info de la voiture :\nmarque = {self.get_marque()}\nmodel = {self.get_modele()}\nKM = {self.get_kilomètrage()} km\nstatus = {self.get_status()}"
    
voiture1 = Voiture("Opel", "AAA", 2021, 40)
voiture1.set_reservoir(40)
print(voiture1.démarrer())
print(voiture1.afficher())