class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def affiche_info(self):
        print("marque: ", self.marque, "\n", "modele: ",self.modele, "\n","annee: ",self.annee)


voiture = Voiture(marque = "Merceedes", modele = "AMG GT 63 s", annee =  2023)

voiture.affiche_info()