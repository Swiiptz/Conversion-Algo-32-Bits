x = input('Rentrer le nombre en base 10: ')
def mantisse(x):
    
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
            b = ''
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
    return addition_mantisse
mantisse = mantisse(x)
c1 = mantisse[0]
if c1 == '.':
    c = 8 #0
else:
    c = 7 #1
def mantisse_vf(mantisse):
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
def exposant(exposant_ent):
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
print(exposant(exposant_ent))

#print(expos)
#test
#100000.11
#1.0000011 
#1010101.001
#1.010101001
