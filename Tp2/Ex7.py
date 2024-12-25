class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        
    def afficher_livres(self):
        for livre in self.livres: 
            print(livre.titre)


# Création de la bibliothèque 
bibliotheque = Bibliotheque() 

# Ajout de livres 
livre1 = Livre(titre="1984", auteur="George Orwell", annee_publication=1949) 
livre2 = Livre(titre="Le Petit Prince", auteur="Antoine de Saint-Exupéry", annee_publication=1943) 

bibliotheque.ajouter_livre(livre1) 
bibliotheque.ajouter_livre(livre2) 

# Affichage des livres 
bibliotheque.afficher_livres()