class CompteBancaire:
    def __init__ (self, numero_compte, nom, prenom, solde=0, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = float (solde)
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte N : {self.__numero_compte}") 
        print(f"Titulaire: {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde} € ")

    def afficherSolde(self):
        print(f"Le sold du compte est de {self.__solde}€") 

    def versement(self, montant):
        self.__solde += montant
        print(f"versement de {montant} €. Nouveau solde: {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Solde insuffisant pour effectuer ce retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€. Nouveau solde: {self.__solde}€")  


    def agios(self):
        if self.__solde < 0 :
            self.__solde -= 10
            print(f"Agios appliques. Nouveau solde: {self.__solde} €") 
 
    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.retrait(montant)
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ effectué vers {compte_destinataire.__prenom} {compte_destinataire.__nom}")
        else:
            print("Solde insuffisant pour le virement.")

compte1 = CompteBancaire("17111979", "Sherstiuk", "Yuliia", 1000000)
compte2 = CompteBancaire("22021969", "Droummeng", "Laurent",-500000, decouvert=True )

compte1.afficher()
print(f"Overdraft permission for compte1: {compte1._CompteBancaire__decouvert}")
compte1.versement(50000)
compte1.retrait(1000)  
compte1.virement(compte2, 1000)
compte1.afficherSolde()

compte2.afficher()
print(f"Overdraft permission for compte2: {compte2._CompteBancaire__decouvert}")
compte2.versement(5000)
compte2.retrait(2000)  

compte2.afficherSolde()