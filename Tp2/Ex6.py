class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def calculer_surface(self):
        return self.largeur * self.hauteur
    
    def calculer_perimetre(self):
        return (2 * self.largeur) + (2 * self.hauteur)
    

rectangle = Rectangle(largeur = 4, hauteur = 6)

print(rectangle.calculer_surface())
print(rectangle.calculer_perimetre())
    
        