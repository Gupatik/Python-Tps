class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom 
        self.__prix = prix

    def get_nom(self):
        return self.__nom
    
    def get_prix(self): 
        return self.__prix

    def calcul_remise(self):
        if self.__prix > 30:
            return self.__prix - ((self.__prix * 15) / 100)
        else:
            return self.__prix
    
    
    
        

produit = Produit(nom = "goo", prix = 50)

print(f'votre final prix Mr {produit.get_nom()} est: {produit.calcul_remise()}')