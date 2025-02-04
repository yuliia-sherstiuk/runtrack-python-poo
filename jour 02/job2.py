class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            self.__nombre_de_pages = 0
            print("Erreur : Le nombre de pages doit être un entier positif.")
    # Getters
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # Setters
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")
    # Affichage du livre
    def afficher(self):
        print(f"Livre: Titre = {self.__titre}, Auteur = {self.__auteur}, Pages = {self.__nombre_de_pages}")


# Création d'un livre avec titre, auteur et nombre de pages
livre = Livre("Les Misérables", "Victor Hugo", 1232)
livre.afficher()

# Modification des attributs
livre.set_nombre_de_pages(500)
livre.afficher()

livre.set_nombre_de_pages(-200)  