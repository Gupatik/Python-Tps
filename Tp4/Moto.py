import Moteur

class Moto(Moteur.Moteur):
    def __init__(self, puissance, type_moteur, type_moto):
        super().__init__(puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        print(f'{super().afficher_moteur()}, le type moto: {self.type_moto}')