import csv
import os


def ajouter_contact(fichier, nom, prenom, telephone):
    with open(fichier, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nom, prenom, telephone])


def afficher_contacts(fichier):
    with open(fichier, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            nom, prenom, telephone = row
            print(f"Nom : {nom}, Prénom : {prenom}, Téléphone : {telephone}")

def rechercher_contact(fichier, nom, prenom, telephone):
    with open(fichier, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == nom and row[1] == prenom and row[2] == telephone:
                print(f"Nom : {row[0]}, Prénom : {row[1]}, Téléphone : {row[2]}")
                return	row
            
def supprimer_contact(fichier, nom, prenom): 
    contact = rechercher_contact(fichier, nom, prenom) 
    if contact is None: 
        return 
    temp_file = "C:/Users/sebba/Desktop/S1/Python/Tp5/Ex10/temp.csv"
    with open(fichier, 'r', newline='') as f, open(temp_file, 'w', newline='') as temp: 
        reader = csv.reader(f) 
        writer = csv.writer(temp) 
        deleted = False 
        for row in reader: 
            if row[0] == nom and row[1] == prenom: 
                deleted = True 
            else: 
                writer.writerow(row) 
        os.replace(temp_file, fichier) 
        
        if deleted: 
            print(f"Contact {nom} {prenom} supprimé.") 
        else: 
            print(f"Aucun contact trouvé pour le nom : {nom} et prénom : {prenom}")

        

