class Part:
    def __init__(self, name , materiel):
        self.name = name
        self.materiel = materiel

    def change_materiel (self, new_materiel):
        self.materiel = new_materiel   

    def __str__(self):
        return f"{self.name} ({self.material})"
    
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {"Mat": Part("Mat", "Bois")}

    def display_state(self):
        print(f"\nEtat actuel du navire {self.name}:")
         
        for part in self.__parts.values():
            print(part)
    
    def replace_part(self, part_name, new_part):

        if part_name in self.__parts:
            self.__parts[part_name] = new_part #change detail
            print(f"\n remplace le detail {part_name}")
        else:
            print(f"\n Erreur : {part_name} introuvable") 

    def change_part(self, part_name, new_material):  
         if part_name in self.__parts:
             self.__parts[part_name].change_material(new_material)
             print(f"Materiau de {part_name} modifie en {new_material}.")
         else:
             print(f"Piece {part_name} introuvable.")

class RqcingShip(Ship):
     def __init__(self, name, max_speed):
         super().__init__(name)
         self.max_speed = max_speed

     def display_speed(self):
         print(f" vitesse max {self.name}: {self.max_speed}")    
    

def main():
    ship = Ship("Le navire Lain")   

    while True:
        print("\nMenu:")
        print("\n1. Afficher l'etat du bateau.\n2.Remplacer une piece.\n3.Modifier le materiau d'une piece\n4.Quitter")
        choix = int(input("Choississez une option:   "))
        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("nom de la pice a modifier:  ")
            new_material = input("Nouveau materiau:  ")
            ship.change_part(part_name, new_material)
        elif choix == "4":
            break
        else:
            print("option invalide")

if __name__ == "__main__":
    main()           

                