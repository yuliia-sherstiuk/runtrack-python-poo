class Tache: 
    def __init__(self, titre, description, statut="faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "terminee"

    def __str__(self):
        return f"Titre: {self.titre}, description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tache '{tache.titre}' ajoutée")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tache '{titre}' supprimée")
                return
        print(f"Tache '{titre}' non trouvée")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()
                print(f"Tache '{titre}' marquée comme terminée")
                return
        print(f"Tache '{titre}' non trouvée")

    def afficherListe(self):
        if not self.taches:
            print("Aucune tache dans la liste.")
        else:
            print("Liste de taches:")
            for tache in self.taches:
                print(tache)

    def filterListe(self, statut):
        filtered = [tache for tache in self.taches if tache.statut == statut]
        if not filtered:
            print(f"Aucune tache avec le statut {statut}.")
        else:
            print(f"Liste des taches avec le statut '{statut}':")
            for tache in filtered:
                print(tache)

# Créer des taches
tache1 = Tache("Trouve une alternance", "Faites une liste d'entreprises. Soumettez votre CV. Réussissez l’entretien.")
tache2 = Tache("Terminer projet", "Finir le projet de programmation")
tache3 = Tache("Appeler le client", "Fixer un rendez-vous")
tache4 = Tache("Apprendre Python", "Algorithmie, développement d’une application avec Python, utilisation d’une interface graphique Tkinter / Pygame")
tache5 = Tache("C++", "Compréhension de l’intérêt des Design patterns, conception MVC, patrons de conception, UML, algorithmie, gestion de la mémoire, librairie SDL3, tests, pointeurs, entrées sorties")
tache6 = Tache("Apprendre java", "Algorithmique, culture informatique, chiffrage et déchiffrage d’une chaîne de caractères en utilisant un algorithme")

# Créer une liste de taches
liste_de_taches = ListeDeTaches()

# Ajouter les taches
liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)
liste_de_taches.ajouterTache(tache3)
liste_de_taches.ajouterTache(tache4)
liste_de_taches.ajouterTache(tache5)
liste_de_taches.ajouterTache(tache6)

# Afficher toutes les taches
liste_de_taches.afficherListe()

# Supprimer une tache
liste_de_taches.supprimerTache("Appeler le client")

# Afficher toutes les taches après suppression
liste_de_taches.afficherListe()

# Marquer une tâche comme terminée
liste_de_taches.marquerCommeFinie("Terminer projet")

# Afficher toutes les tâches
liste_de_taches.afficherListe()


liste_de_taches.filterListe("faire")


liste_de_taches.filterListe("terminee")