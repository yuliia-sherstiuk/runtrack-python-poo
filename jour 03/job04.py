class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Joueur {self.nom} | Buts: {self.buts} | Passes: {self.passes_decisives} | Jaunes: {self.cartons_jaunes} | Rouges: {self.cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 4, "Défenseur")
joueur3 = Joueur("Rodrigo", 7, "Attaquant")
joueur4 = Joueur("Poule", 11, "Attaquant")
joueur5 = Joueur("Garry", 1, "Gardien")
joueur6 = Joueur("Devid", 2, "Défenseur")
joueur7 = Joueur("Benjament", 6, "Milieu")

# Création de l'équipe
equipe = Equipe("PSG")

# Ajout des joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)
equipe.ajouterJoueur(joueur4)
equipe.ajouterJoueur(joueur5)
equipe.ajouterJoueur(joueur6)
equipe.ajouterJoueur(joueur7)

# Simulation du match
joueur1.marquerUnBut()                # Messi marque un but
joueur1.effectuerUnePasseDecisive()    # Messi fait une passe décisive
joueur2.recevoirUnCartonRouge()        # Ramos reçoit un carton rouge
joueur3.marquerUnBut()                # Mbappé marque un but
joueur3.marquerUnBut()                # Mbappé marque un autre but
joueur4.effectuerUnePasseDecisive()    # Neymar fait une passe décisive
joueur6.recevoirUnCartonJaune()        # Hakimi reçoit un carton jaune

# Affichage des statistiques de tous les joueurs
equipe.afficherStatistiquesJoueurs()