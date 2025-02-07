class Part: 
    def __init__(self, name, materiel):
        self.name = name
        self.materiel = materiel

    def change_materiel(self, new_materiel):
        self.materiel = new_materiel   

    def __str__(self):
        return f"{self.name} ({self.materiel})"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mat": Part("Mat", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Voile": Part("Voile", "Tissu")
        }

    def display_state(self):
        print(f"\nÉtat actuel du navire {self.name}:")
        for part in self.__parts.values():
            print(part)

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            print(f"\nRemplacement de {part_name} effectué.")
        else:
            print(f"\nErreur : {part_name} introuvable.")

    def change_part(self, part_name, new_material):  
        if part_name in self.__parts:
            self.__parts[part_name].change_materiel(new_material)
            print(f"\n Matériau de {part_name} modifié en {new_material}.")
        else:
            print(f"\n Pièce {part_name} introuvable.")

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse max de {self.name}: {self.max_speed} km/h")    

def main():
    ship = Ship("Le Navire de LAIN")   

    while True:
        print("\nMenu:")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Quitter")

        choix = input("Choisissez une option: ")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("Nom de la pièce à remplacer: ")
            new_material = input("Matériau de la nouvelle pièce: ")
            ship.replace_part(part_name, Part(part_name, new_material))
        elif choix == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            ship.change_part(part_name, new_material)
        elif choix == "4":
            print("\n Au revoir !")
            break
        else:
            print("\n Option invalide.")

if __name__ == "__main__":
    main()