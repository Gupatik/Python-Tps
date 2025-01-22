import csv

def read_csv(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nom, age, ville = row 
            print(f"Nom : {nom}, Âge : {age}, Ville : {ville}")


read_csv("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex4/contacts.csv")