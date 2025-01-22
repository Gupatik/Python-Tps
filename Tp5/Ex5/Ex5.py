import json

with open("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex5/etudiants.json", 'r') as json_file:
    data = json.load(json_file)
    
    for student in data['students']:
        nom, age, note = student
        print(f"Nom : {nom}, Âge : {age}, Note : {note}")
