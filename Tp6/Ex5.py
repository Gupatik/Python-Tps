def process_input(user_input):
    try:
        return 10 / int(user_input)
    except ValueError:
        raise ValueError(f"Impossible de convertir {user_input} en entier.")
    except ZeroDivisionError:
        return ("Impossible de divisez par 0.")
    

input_value = input("Entrez un nombre : ")
print(process_input(input_value))
    