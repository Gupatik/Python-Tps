class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        return (f'la puissance: {self.puissance}, le tyoe moteur: {self.type_moteur}')