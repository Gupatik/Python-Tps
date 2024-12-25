class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print("woof")


chien = Chien(nom = "Max", race = "Labrador", age =  3)

chien.aboyer()