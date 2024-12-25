class Vehicule:
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("vvvf")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("uuuf")

voiture = Voiture() 
bicyclette = Bicyclette() 

voiture.deplacer()
bicyclette.deplacer()