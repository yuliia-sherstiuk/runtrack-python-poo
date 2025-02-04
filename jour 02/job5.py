class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        # Attributs privés
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False  # La voiture est par défaut éteinte
        self.__reservoir = 50  # Le réservoir de carburant est initialisé à 50 litres par défaut

    # Assesseurs (getters) pour obtenir les valeurs des attributs
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    # Mutateurs (setters) pour modifier les valeurs des attributs
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Méthode privée pour vérifier le niveau de carburant
    def __verifier_plein(self):
        return self.__reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture est démarrée.")
        else:
            print("Pas assez de carburant pour démarrer la voiture.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")