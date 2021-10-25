x = input('Rentrer le nombre en base 10: ')

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