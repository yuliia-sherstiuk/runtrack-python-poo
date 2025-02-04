class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            self.__nombre_de_pages = 0
            print("Erreur : Le nombre de pages doit être un entier positif.")
        self.__disponible = True  # Par défaut, le livre est disponible

    # Getters et Setters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.c

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Vérification de la disponibilité
    def verification(self):
        return self.__disponible

    # Emprunter le livre
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour emprunt.")

    # Rendre le livre
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

    # Affichage des informations du livre
    def afficher(self):
        dispo = "disponible" if self.__disponible else "indisponible"
        print(f"Livre: Titre = {self.__titre}, Auteur = {self.__auteur}, Pages = {self.__nombre_de_pages}, État = {dispo}")


# Création d'un livre
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
livre.afficher()

# Emprunter le livre
livre.emprunter()
livre.afficher()

# Essayer de rendre le livre
livre.rendre()
livre.afficher()