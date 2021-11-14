nb = input("Choisir un nombre en base 10: ")
#---------------------------------------------------------------------
#signe
signe = int
if float(nb) < 0 :
        signe = 1 # Nombre Négatif
        
if float(nb) >= 0 :
        signe = 0 # Nombre Positif
if float(nb) < 0:
 locate_neg = nb.find("-")
 long_negate = len(nb)
 nb = nb[locate_neg +1:long_negate]

# -----------------------------------------------------------------
# partie entière
def entier_base10(nb):
    entier = str
    nb = float(nb)
    ent_nb = int(nb)
    float_nb = float(nb)
    if float_nb == ent_nb:
        nb = int(nb)
        entier = str(nb)
    if float_nb != ent_nb:
        nb_str = str(nb)
        loca_point = nb_str.find(".")
        entier = nb_str[0:loca_point]
    return entier
#print(entier_base10(nb)) VALIDE

# -------------------------------------------------------------------
# partie décimal
def decimal_base10(nb):
    décimal = str
    nb = float(nb)
    ent_nb = int(nb)
    float_nb = float(nb)
    if float_nb == ent_nb:
        décimal = ''
    if float_nb != ent_nb:
        nb_str = str(nb)
        loca_point = nb_str.find(".")
        nb_long = len(nb_str)
        décimal = nb_str[loca_point+1:nb_long]
        décimal = "0."+ str(décimal)
    return décimal
#print(decimal_base10(nb)) VALIDE

# -------------------------------------------------------------------
entier = int(entier_base10(nb))
# conversion entier VALIDE
def base10_2_entier(entier):
        a = bin(entier)       
        long = len(a)
        b = a[2:long]
        return b
#print(base10_2_entier(entier))

#---------------------------------------------------------------------
if decimal_base10(nb)=='':
    decimal = ''
else:
    decimal = float(decimal_base10(nb))
f_conv_entier = base10_2_entier(entier)
if f_conv_entier == 0:
        lenght = 0
else:
        lenght = len(f_conv_entier)
# conversion decimal VALIDE
def base10_2_decimal(decimal):
       if decimal == '':
        x = 0 
       else:
        b = float(decimal)
        l = 0
        y = str(0)
        z = str(1)
        a = 0
        listeA = str()
        long = 23 - lenght
        while l <= long:
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
        premier_car = listeA[0:1]
        if premier_car == '0':
            long_listeA = len(listeA)
            sans_premier_car = listeA[1:long_listeA]
            listeA = listeA

        x = listeA
       return x #conversion partie décimal base 10 en base 2
#print(base10_2_decimal(decimal))
# mantisse
#--------------------------------------------------------------------
## I- mantisse :addition VALIDE
def mantisse_addition_point(nb):
     mantisse_addition = str(base10_2_entier(entier))+ '.' + str(base10_2_decimal(decimal))
     return mantisse_addition
def mantisse_addition(nb):
     mantisse_addition = str(base10_2_entier(entier)) + str(base10_2_decimal(decimal))
     return mantisse_addition
#print(mantisse_addition(nb))
#print(mantisse_addition_point(nb))
#--------------------------------------------------------------------
mant_add_point = mantisse_addition_point(nb) #avec point
mant_add = mantisse_addition(nb)#sans point
car1 = '0'
## II- mantisse :decal mantisse VALIDE
def decal_mantisse(mant_add):
    a = 0
    b = 1
    l = 0
    car1 = mant_add_point[a:b]
    nb_float = float(nb)
    if nb_float >= 1: 
        loca_point = mant_add_point.find('.') #localisation point dans la mantisse
        long_m = len(mant_add)
        long_m_point = len(mant_add_point)
        mant_p1 = mant_add_point[0:loca_point]#partie gauche mantisse avant le point
        mant_p2 = mant_add_point[(loca_point + 1):long_m_point] #partie droite de la mantisse après le point
        mant_car1 = mant_add[0:1]
        mant_sans_car1 = mant_add[1:long_m]
        mant_deca_point = mant_car1 +'.' + mant_sans_car1
    if nb_float < 1 and nb_float > 0:
        while car1 != '1':
            car1 = mant_add_point[a:b]
            l = l+1
            a = a+1
            b= b+1
        long_m = len(mant_add_point)
        mant_car1 = mant_add_point[l:l+1]
        mant_sans_car1 = mant_add_point[l:long_m]
        mant_deca_point = mant_car1 +'.' + mant_sans_car1
    if nb_float == 0:
        mant_deca_point = '0.0'
    return mant_deca_point
#print(mant_add_point) #0.00011001100110011001100
#print(decal_mantisse(mant_add)) #0.011001100110011001100
mant_deca_point = decal_mantisse(mant_add)
def mantisse_vf(mant_deca_point):
    loca_point = mant_deca_point.find(".")
    long_mant_p = len(mant_deca_point)
    mantisse = mant_deca_point[loca_point+1:long_mant_p]
    return mantisse
#print(mantisse_vf(mant_deca_point))
#--------------------------------------------------------------------
new_mant_add_point = decal_mantisse(mant_add) #avec point
mant_add = mantisse_addition(nb) #sans point
old_mant_point = mantisse_addition_point(nb)
mant_p = mantisse_addition_point(nb)
mant_add_point = mantisse_addition_point(nb)
## I - exposant
def exposant_ent(mant_add_point):
    a = 0
    b = 1
    l = 0
    car1 = mant_add_point[a:b]
    nb_float = float(nb)
    if nb_float >= 1:
        loca_point_new_mant = new_mant_add_point.find(".")
        loca_point_old_mant = old_mant_point.find(".")
        exposant_entier = loca_point_old_mant - loca_point_new_mant
    if nb_float <1 and nb_float > 0 :
         while car1 != '1':
            car1 = mant_p[a:b]
            l = l+1
            a = a+1
            b= b+1
         exposant_entier = (l-2)
    if nb_float == 0:
            exposant_entier = 0
    return exposant_entier
#print(mant_add_point)  
#print(exposant_ent(mant_add_point))
#print(mant_p)
#--------------------------------------------------------------------
## II - exposant
def exposant(expo):
 nb_float = float(nb)
 expo_ent = exposant_ent(mant_add_point)
 if nb_float >= 1:
  expo = 127 + expo_ent
 if nb_float < 1 and nb_float > 0:
  expo = 127 - expo_ent
 if nb_float == 0:
  expo = 0
 bin_expos = bin(expo)
 long_expos = len(bin_expos)
 bin_exposant = bin_expos[2:long_expos]
 return bin_exposant
#print(exposant(exposant_ent(mant_add)))
# --------------------------------------------------------------------
# calibre
exposant_vf = str(exposant(exposant_ent(mant_add)))
mantisse_vf1 = str(mantisse_vf(mant_deca_point))
def calibre_droit(mantisse_vf1):
    nb0 = 23 - len(mantisse_vf1)
    mantisse = mantisse_vf1 + "0"*nb0
    return mantisse

def calibre_gauche(exposant_vf):
 nb0=8-len(exposant_vf)
 exposant = nb0*'0'+exposant_vf 
 return exposant
# --------------------------------------------------------------------
#hexadecimal 
iee_754 = str(signe)+calibre_gauche(exposant_vf)+calibre_droit(mantisse_vf1)
iee_ent = int(iee_754)
part1 = iee_754[0:4]
part2 = iee_754[4:8]
part3 = iee_754[8:12]
part4 = iee_754[12:16]
part5 = iee_754[16:20]
part6 = iee_754[20:24]
part7 = iee_754[24:28]
part8 = iee_754[28:32]


print(hex(int(part1)))
print('bit:',str(signe)+' '+ calibre_gauche(exposant_vf)+' ' + calibre_droit(mantisse_vf1))