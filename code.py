x = input('Rentrer le nombre en base 10: ')
def base10_2_entier(x):
    if x>0:
      x = str(x)
      y = x.find('.')
      partie_décimal = x[0:y]
    return partie_décimal
print(base10_2_entier)