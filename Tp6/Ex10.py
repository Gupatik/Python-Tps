file = input("Entrez le nom du fichier : ")
entier = input("Entrez un entier : ")


with open(file, 'w') as file:
    try:
        try:
            entier = int(entier)
            if entier < 0:
                raise ValueError("Le nombre doit être positif")
        except ValueError as e:
            print(f"Impossible de convertir {entier} en entier: {e}") 
        file.write(str(entier))
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Le fichier {file} n'existe pas.") from e
    except IOError as e:
        print(f"Erreur lors de l'accès au fichier : {e}")
    
