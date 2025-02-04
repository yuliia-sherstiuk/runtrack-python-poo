class Student:
    def __init__(self, last_name, first_name, student_id):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__student_id = student_id
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()  # Mise à jour du niveau
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom = {self.__last_name} Prenom = {self.__first_name} id = {self.__student_id} Niveau = {self.__level}")

# Instanciation de l'étudiant John Doe
student = Student("Doe", "John", 145)

# Ajout des crédits
student.add_credits(15)
student.add_credits(10)
student.add_credits(10)
student.add_credits(10)
student.add_credits(10)
student.add_credits(10)
student.add_credits(10)


# Affichage du total de crédits
print(f"Le nombre de crédits de John Doe est de {student._Student__credits} points")

# Affichage des informations de l'étudiant
student.student_info()
