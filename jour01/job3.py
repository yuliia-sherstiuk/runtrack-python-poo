class Operation:
    def __init__(self,  nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"La somme de {self.nombre1} et {self.nombre2} est {resultat}")

Operation1=Operation(12, 3)
Operation1.addition()
