class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} {self.prenom} et j'ai {self.age} ans.")

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule): 
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"etudiant {self.matricule}")

    

personne = Personne(nom="Mohamed", prenom="Sebbar", age=21)

personne.se_presenter()

etudiant = Etudiant(nom="Youssef", prenom="Khalid", age=22, matricule="12345")  
etudiant.se_presenter()
etudiant.etudier()





