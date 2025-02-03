class Personne: 
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return f"Je suis {self.nom} {self.prenom}"
p1 = Personne("Sherstiuk", "Yuliia")
p2 = Personne("Sherstiuk", "Diana")
print(p1)
print(p2)