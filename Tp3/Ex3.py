import Ex1

cercle = Ex1.Cercle(rayon=3)
rectangle = Ex1.Rectangle(hauteur=3, largeur=3)
formes = [cercle, rectangle]

def afficher_surface(formes):
    for forme in formes:
        print(forme.calculer_surface())


#afficher_surface(formes)
