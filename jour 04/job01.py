class Personne:
    def __init__(self, age=14):
        self.age = age  

    def afficherAge(self):
        print(f"Âge: {self.age}")  

    def bonjour(self):
        print("Hello")  

    def modifierAge(self, nouveau_age):
        self.age = nouveau_age  


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")  

    def afficherAge(self):
        print(f"J’ai {self.age} ans")  


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age) 
        self.__matiereEnseignee = matiereEnseignee  

    def enseigner(self):
        print("Le cours va commencer")  


# test
personne1 = Personne()
eleve1 = Eleve()  

eleve1.bonjour()
eleve1.afficherAge()  
eleve1.allerEnCours() 


professeur = Professeur(40, "Mathématiques")  
professeur.enseigner()  