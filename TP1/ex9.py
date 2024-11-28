def analyse_texte(texte):
    nombre_mots = len(texte.rsplit())
    nombre_caracteres = len(texte)
    return {"nombre_de_mots": nombre_mots, "nombre de caracteres": nombre_caracteres}


mon_texte = "Bonjour tout le monde!"
resultat = analyse_texte(mon_texte)
print(resultat) 
