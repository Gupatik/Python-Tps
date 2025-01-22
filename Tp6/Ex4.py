class NegativeAgeError(Exception):
    def __init__(self, message ="L'âge ne peut pas être négatif."):
        super().__init__(message)


def set_age(age):

    if age<0:
        raise NegativeAgeError ("L'age négative n'est pas autorisée.")
    print(f"L'âge défini est : {age}")

try:
    set_age(-10)
except NegativeAgeError as e:
    print(f"Erreur : {e}")