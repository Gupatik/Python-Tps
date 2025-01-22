import logging

logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        error_message = f"Le fichier {file_name} n'existe pas."
        logging.error(error_message)
        raise FileNotFoundError(f"Le fichier {file_name} n'existe pas.") from e
    
try:
    content = read_file("file.txt")
    print(f"Contenu : {content}")
except FileNotFoundError as e:
    print(f"Erreur : {e}")