class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom 
        self.__prenom = prenom 
        self.__age = age


    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        if isinstance(nom, str) and nom.strip():
            self.__nom = nom 
        else:
            print("erreur")


    def get_prenom(self):
        return self.__prenom
    
    def set_prenom(self, prenom):
        if isinstance(prenom, str) and prenom.strip():
            self.__prenom = prenom 
        else:
            print("erreur")


    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age 
        else:
            print("erreur")


personne = Personne("koo", "pooo", 33)

print(personne.get_nom())
print(personne.get_prenom())  
print(personne.get_age()) 


personne.set_nom("foo") 
personne.set_prenom("mooo") 
personne.set_age(28)

print(personne.get_nom())
print(personne.get_prenom())  
print(personne.get_age()) 