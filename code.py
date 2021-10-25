x = input('Rentrer le nombre en base 10: ')
def entier_base10(x):  
    if float(x) >= 1:
        a = str(x)
        y = a.find('.')
        partie_entière = a[0:y]
        return partie_entière
    else:
        nb_zero = '0'
        return nb_zero #sortie str de l'entier avant la virgule

def decimal_base10(x):  
        a = str(x)
        y = a.find('.')
        long = len(a)
        partie_décimal = a[(y+1):long]
        partie_décimal = '0.' + str(partie_décimal)
        return partie_décimal #sortie str du décimal après la virugule de la forme 0.'decimal'

entier = int(entier_base10(x))
decimal = float(decimal_base10(x))

def base10_2_decimal(decimal):
   b = float(decimal)
   l = 0
   y = str(0)
   z = str(1)
   a = 0
   listeA = str()
   while l < 8:
      b = b*2
      if b > 1:
         b = b-1
         listeA = listeA + z
         l = l+1
         a = a+1
      else:
         listeA = listeA + y
         l = l+1
         a = a+1
      if b==1:
         listeA = listeA + z
         l = 8
         a = a+1
         c = 8-len(listeA)
         listeA = listeA + ('0'*c)
   x = listeA
   return x #conversion partie décimal base 10 en base 2

def base10_2_entier(entier):

