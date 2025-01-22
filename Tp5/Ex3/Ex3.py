


with open("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex3/phrases.txt", 'w') as file:
    for i in range(1, 4):
        phrase = input(f"Entrer la phrase {i}: ")
        file.write(phrase + '\n')

print("Success!")

answer = input("Voulez-vous ajouter au contenu du fichier? (o/n) ")

if answer == 'o' or answer == 'oui':
    with open("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex3/phrases.txt", 'a') as file:
        phrase = input("Entrer la phrase: ")
        file.write(phrase + '\n')
    print("Success a ajouter!")

