class Vehicule:
    def __init__(self, marque, model, annee):
        self.marque = marque
        self.model = model
        self.annee = annee
    
    def afficher_info(self):
        print(f'la marque: {self.marque}, le modele: {self.model}, annee: {self.annee}')
        