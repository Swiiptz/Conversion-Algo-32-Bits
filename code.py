x = input('Rentrer le nombre en base 10: ') #entrée
def mantisse(x): #fonction mantisse
    
    def entier_base10(x):   #fonction qui extrait la partie entière
        a = str(x)
        y = a.find('.')
        partie_entière = a[0:y]
        return partie_entière

    def decimal_base10(x):  #fonction qui extrait la partie décimal
        a = str(x)
        y = a.find('.')
        long = len(a)
        partie_décimal = a[(y+1):long]
        partie_décimal = '0.' + str(partie_décimal)
        return partie_décimal #sortie str du décimal après la virugule de la forme 0.'decimal'

    entier = int(entier_base10(x)) 
    decimal = float(decimal_base10(x)) 

    def base10_2_entier(entier): #conversion de la partie entière en base 2
        a = bin(entier)       
        long = len(a)
        b = a[2:long]
        if int(b) == 0:
            b = ''
            return b
        else:
            lenght = len(b) #variable de la taille de la chaien
            return b

    f_conv_entier = base10_2_entier(entier) #permet de savoir si la partie entièr est égal à 0
    if f_conv_entier == None:
        lenght = 0 
    else:
        lenght = len(f_conv_entier)

    def base10_2_decimal(decimal): ##conversion de la partie décimal en base 2
        b = float(decimal)
        l = 0
        y = str(0)
        z = str(1)
        a = 0
        listeA = str() 
        long = 23 - lenght #taille de la chaine, soustraire la taille de la sortie totale de la mantisse
        while l < long: #tant que la chaine est en dessous de la valeur max on continue
            b = b*2
            if b > 1:
                listeA = listeA + z #permet de rajouter une valeur à la chaine "1"
                b = b-1
                l = l+1 #pour que la boucle while puisse etre validée
                a = a+1
                continue
            if b < 1:
                listeA = listeA + y #permet de rajouter une valeur à la chaine "0"
                l = l+1 #pour que la boucle while puisse etre validée
                a = a+1 
                continue
            if b==1:
                listeA = listeA + z #permet de rajouter une valeur à la chaine "1"
                l = long #pour sortir de la boucle while
                a = a+1
                break
        x = listeA
        return x #conversion partie décimal base 10 en base 2


    addition_mantisse = str(base10_2_entier(entier)) + '.' + str(base10_2_decimal(decimal)) #mise en forme de la mantisse
    return addition_mantisse
mantisse = mantisse(x)
c1 = mantisse[0]
if c1 == '.':
    c = 8 #0
else:
    c = 7 #1
def mantisse_vf(mantisse): #fonction mantisse version finale
 loca_point = mantisse.find('.') #localisation point dans la mantisse
 long_m = len(mantisse) #taille mantisse
 m_p1 = mantisse[0:loca_point]#partie gauche mantisse avant le point
 if m_p1=='':
    m_p2 = mantisse[(loca_point + 1):long_m] #partie droite de la mantisse après le point
    m_wpoint = m_p1 + m_p2 #mantisse sans point
    long_m_wpoint = len(m_wpoint) 
    m_c1 = '1' #caractère 1de la mantisse sans point
    m_c2 = m_wpoint[1:long_m_wpoint] #partie 2 de la mantisse sans point
    m_deca = m_c1 +'.'+m_c2 #mantisse avec le point décalé
    loca_point2 = m_deca.find('.') #localisation du 2eme point
    expo = loca_point - loca_point2 #différence des positions des deux point = exposant
    m_vf = m_c1 + m_c2
 else:
    m_p2 = mantisse[(loca_point + 1):long_m] #partie droite de la mantisse après le point
    m_wpoint = m_p1 + m_p2 #mantisse sans point
    long_m_wpoint = len(m_wpoint) 
    m_c1 = m_wpoint[0:1] #caractère 1de la mantisse sans point
    m_c2 = m_wpoint[1:long_m_wpoint] #partie 2 de la mantisse sans point
    m_deca = m_c1 +'.'+m_c2 #mantisse avec le point décalé
    loca_point2 = m_deca.find('.') #localisation du 2eme point
    expo = loca_point - loca_point2 #différence des positions des deux point = exposant
    m_vf = m_c2
 return m_vf

def exposant_ent(mantisse):
 loca_point = mantisse.find('.') #localisation point dans la mantisse
 long_m = len(mantisse) #taille mantisse
 m_p1 = mantisse[0:loca_point]#partie gauche mantisse avant le point
 if m_p1=='':
    loca_point = mantisse.find('.') #localisation point dans la mantisse
    long_m = len(mantisse) #taille mantisse
    m_p1 = mantisse[0:loca_point]#partie gauche mantisse avant le point
    m_p1 = '0'
    m_p2 = mantisse[(loca_point + 1):long_m] #partie droite de la mantisse après le point
    m_wpoint = m_p1 + m_p2 #mantisse sans point
    long_m_wpoint = len(m_wpoint) 
    m_c1 = '1' #caractère 1de la mantisse sans point
    m_c2 = m_wpoint[1:long_m_wpoint] #partie 2 de la mantisse sans point
    m_deca = m_c1 +'.'+m_c2 #mantisse avec le point décalé
    loca_point2 = m_deca.find('.') #localisation du 2eme point
    expo = loca_point - loca_point2 #différence des positions des deux point = exposant
    m_vf = m_c1 + m_c2
    l = 0
    a = str
    while a != '1':
        l = l+1
        a = m_vf[l]
    return l
 else:
    m_p2 = mantisse[(loca_point + 1):long_m] #partie droite de la mantisse après le point
    m_wpoint = m_p1 + m_p2 #mantisse sans point
    long_m_wpoint = len(m_wpoint) 
    m_c1 = m_wpoint[0:1] #caractère 1de la mantisse sans point
    m_c2 = m_wpoint[1:long_m_wpoint] #partie 2 de la mantisse sans point
    m_deca = m_c1 +'.'+m_c2 #mantisse avec le point décalé
    loca_point2 = m_deca.find('.') #localisation du 2eme point
    expo = loca_point - loca_point2 #différence des positions des deux point = exposant
    m_vf = m_c2
    return expo
expos = exposant_ent(mantisse)
def exposant(exposant_ent): #fonction exposant
 if c == 8:
     expos = exposant_ent(mantisse) 
     expos = 127 - int(expos)
 if c == 7:
     expos = exposant_ent(mantisse)
     expos = 127 + int(expos)
 bin_expos = bin(expos)
 long_expos = len(bin_expos)
 bin_exposant = bin_expos[2:long_expos]
 return bin_exposant

mantisse_t = str(mantisse_vf(mantisse))
exposant_t = str(exposant(exposant_ent))
print(exposant_t+' ' + mantisse_t)
#print(expos)
#test
#100000.11
#1.0000011 
#1010101.001
#1.010101001
