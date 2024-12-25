import Ex4

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_prix_total(self):
        return self.produit.get_prix() * self.quantite

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total_panier(self):
        total = 0
        for commande in self.commandes:
            total += commande.calculer_prix_total()
        return total


produit1 = Ex4.Produit(nom="goo", prix=40)
commande1 = Commande(produit=produit1, quantite=2)

produit2 = Ex4.Produit(nom="bar", prix=30)
commande2 = Commande(produit=produit2, quantite=3)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

total_panier = panier.calculer_total_panier()
print(f'Total du panier: {total_panier}')
