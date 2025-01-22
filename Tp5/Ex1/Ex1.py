
with open("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex1/exemple.txt", 'r') as file:
    lines = file.readlines()
    
    for index, line in enumerate(lines, start=1):
        print(f"{index}: {line.strip()}")
