class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    def __init__(self, solde):
        self.solde = solde


    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        self.solde -= montant

    def afficher_solde(self):
        print("solde: ", self.solde)


compte = CompteBancaire(solde = 300)

compte.deposer(50)
compte.afficher_solde()
compte.retirer(10)
compte.afficher_solde()
