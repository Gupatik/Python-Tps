import os

def renomer_ficher(old_name, new_name):
    os.rename(old_name, new_name)
    print(f'Renamed {old_name} to {new_name}')

def deleter_ficher(file_name):
    os.remove(file_name)
    print(f'Deleted {file_name}')


#renomer_ficher("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex6/phrases.txt", "C:/Users/sebba/Desktop/S1/Python/Tp5/Ex6/anciennes_phrases.txt")
deleter_ficher("C:/Users/sebba/Desktop/S1/Python/Tp5/Ex6/anciennes_phrases.txt")

