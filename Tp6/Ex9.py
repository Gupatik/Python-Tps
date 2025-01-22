def get_positive_integer():
    while True:
        try:
            num = int(input("Saisir un entier positif:"))
            if num <0:
                raise ValueError("Le nombre doit être positif")
            else:
                return num
        except ValueError as e:
            print(f"Impossible de convertir en entier: {e}")


get_positive_integer()