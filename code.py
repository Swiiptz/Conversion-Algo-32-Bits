x = input('Rentrer le nombre en base 2:')
def entier_base10(x):  
    if float(x) > 0:
        a = str(x)
        y = a.find('.')
        partie_décimal = a[0:y]
        return partie_décimal
    else:
        return "Le nombre est inférieur à 0"
print(entier_base10(x))