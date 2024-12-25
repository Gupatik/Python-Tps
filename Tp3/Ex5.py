class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def afficher_employes(self):
        for employe in self.employes:
            print(f'Manager: {self.nom}, Nom: {employe.nom}, Prénom: {employe.prenom}, Salaire: {employe.salaire}')


manager1 = Manager(nom="boo", prenom="mooo", salaire=50000)
employe1 = Employe(nom="koo", prenom="jooo", salaire=30000)
employe2 = Employe(nom="soo", prenom="vooo", salaire=32000)

manager1.ajouter_employe(employe1)
manager1.ajouter_employe(employe2)

manager2 = Manager(nom="poo", prenom="zooo", salaire=80000)
employe3 = Employe(nom="roo", prenom="uooo", salaire=70000)
employe4 = Employe(nom="too", prenom="yooo", salaire=62000)

manager2.ajouter_employe(employe3)
manager2.ajouter_employe(employe4)

manager1.afficher_employes()
manager2.afficher_employes()
