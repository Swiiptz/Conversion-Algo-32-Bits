x = input('Rentrer le nombre en base 10: ')
def entier_base10(x):  
        a = str(x)
        y = a.find('.')
        partie_entière = a[0:y]
        return partie_entière

def decimal_base10(x):  
        a = str(x)
        y = a.find('.')
        long = len(a)
        partie_décimal = a[(y+1):long]
        partie_décimal = '0.' + str(partie_décimal)
        return partie_décimal #sortie str du décimal après la virugule de la forme 0.'decimal'

entier = int(entier_base10(x))
decimal = float(decimal_base10(x))

def base10_2_entier(entier):
 a = bin(entier)       
 long = len(a)
 b = a[2:long]
 if int(b) == 0:
    b = '0'
    return b
 else:
    lenght = len(b)
    return b

f_conv_entier = base10_2_entier(entier)
if f_conv_entier == None:
    lenght = 0
else:
    lenght = len(f_conv_entier)

def base10_2_decimal(decimal):
   b = float(decimal)
   l = 0
   y = str(0)
   z = str(1)
   a = 0
   listeA = str()
   long = 23 - lenght
   while l < long:
      b = b*2
      if b > 1:
         listeA = listeA + z
         b = b-1
         l = l+1
         a = a+1
         continue
      if b < 1:
         listeA = listeA + y
         l = l+1
         a = a+1
         continue
      if b==1:
         listeA = listeA + z
         l = long
         a = a+1
         break
   x = listeA
   return x #conversion partie décimal base 10 en base 2


addition_mantisse = str(base10_2_entier(entier)) + '.' + str(base10_2_decimal(decimal))
print(addition_mantisse)


