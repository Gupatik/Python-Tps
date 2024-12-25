class Animal:
    def faire_du_bruit(self): 
        pass

class Chien(Animal):
    def faire_du_bruit(bruit):
        print("wa wa")

class Chat(Animal):
    def faire_du_bruit(bruit):
        print("maw maw")

chien = Chien() 
chien.faire_du_bruit() 

chat = Chat() 
chat.faire_du_bruit()


