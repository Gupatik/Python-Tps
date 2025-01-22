def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        raise ValueError(f"Impossible de convertir {value} en entier.") from e
    
try:
    convert_to_int("abc")
except ValueError as e:
    print(f"Erreur : {e}")