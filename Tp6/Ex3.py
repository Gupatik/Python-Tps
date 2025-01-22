def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Le fichier {file_name} n'existe pas.") from e
    
try:
    content = read_file("file.txt")
    print(f"Contenu : {content}")
except FileNotFoundError as e:
    print(f"Erreur : {e}")