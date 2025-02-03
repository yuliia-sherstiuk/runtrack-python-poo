
class Animal:
    def __init__(self):
        self.prenom = ""
        self.age = 0
    def vieiller(self):
        self.age += 1
    def nommer (self, prenom):
        self.prenom = prenom

mon_animal = Animal() 
print("l'age de animal :" , mon_animal.age)     
mon_animal.vieiller()
print("l'age de l'animal :",  mon_animal.age )  
mon_animal.nommer("lain")
print("l'animal se nomme :", mon_animal.prenom)
