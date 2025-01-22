def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
    else:
        print("la division a été effectuée avec succès")
    return a / b



try:
    result = safe_division(10, 1)
    print(f"Résultat : {result}")
except ZeroDivisionError as e:
    print(f"Erreur : {e}")
finally:
    print("Fin du programme.")
