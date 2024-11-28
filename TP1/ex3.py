def intersection(ensemble1, ensemble2):
    return list(set(ensemble1) & set(ensemble2))

ensemble1 = [0, 22, 33, 43, 5] 
ensemble2 = [1, 2, 33, 4, 5] 
print(intersection(ensemble1, ensemble2))