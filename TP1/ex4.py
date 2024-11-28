def compte_occurences(liste):
    occs = {} 
    for mot in liste: 
        if mot in occs: occs[mot] += 1 
        else: occs[mot] = 1 
    return occs


ma_liste = ["pomme", "banane", "pomme", "orange", "pomme"] 

print(compte_occurences(ma_liste))