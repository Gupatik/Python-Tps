def fusionner_dicts(dict1, dict2):
    fusionne = dict1.copy() 
    for cle, valeur in dict2.items():
        if cle in fusionne:
            fusionne[cle] += valeur
        else:
            fusionne[cle] = valeur
    return fusionne


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

resultat = fusionner_dicts(dict1, dict2)
print(resultat)  
