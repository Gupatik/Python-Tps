
with open("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex2/phrases.txt", 'w') as file:
    for i in range(1, 4):
        phrase = input(f"Entrer la phrase {i}: ")
        file.write(phrase + '\n')

print("Success!")
