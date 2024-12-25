class Forme:
    def calculer_surface():
        pass

class Rectangle(Forme):
    def __init__(self, hauteur, largeur):
        self.hauteur = hauteur
        self.largeur = largeur

    def calculer_surface(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):  
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return (self.rayon ** 2) * 3.14
    

cercle = Cercle(rayon=3)
surface = cercle.calculer_surface()
print(surface)

rectangle = Rectangle(hauteur=3, largeur= 3)
surface = rectangle.calculer_surface()
print(surface)
