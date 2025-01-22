import Vehicule

class Voiture(Vehicule.Vehicule):
    def __init__(self, marque, model, annee, nmbr_places):
        super().__init__(marque, model, annee)
        self.nmbr_places = nmbr_places

    def afficher_info(self):
        return (f'{super().afficher_info()}, nombre de places: {self.nmbr_places}')

