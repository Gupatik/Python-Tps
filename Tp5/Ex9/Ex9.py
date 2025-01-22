def file_statistics(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        total_lines = len(lines)

        total_words = 0
        total_characters = 0
        for line in lines:
            words = line.split()
            total_words += len(words)
            total_characters += len(line)

        return total_lines, total_words, total_characters

filename = "C:/Users/sebba/Desktop/S1/Python/Tp5/Ex9/sample.txt"

lines, words, characters = file_statistics(filename)

print(f"Nombre total de lignes : {lines}")
print(f"Nombre total de mots : {words}")
print(f"Nombre total de caractères : {characters}")
