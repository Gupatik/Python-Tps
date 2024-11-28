def somme_varargs(*args):
    return sum(args)

args = {1, 2, 3}
print(somme_varargs(args))