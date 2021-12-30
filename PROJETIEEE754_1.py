#code développé par Quentin, Cédric et Milan (cf : équipe HMD) // Commentaire Milan

def signe(nb_decimal:float)->int: #fonction pour obtenir le signe //PAR QUENTIN
    """
    Fonction pour determiner le signe

    entrée
        nb_decimal float nombre qui doit être traduit avec la norme IEE754
    sortie
        valeur numérique int retourne le signe en binaire 1 ou 0
    """
    if nb_decimal<0: #regarde si le nombre est inférieur à 0
        return 1 #signe en binaire
    return 0

def puissance_de_deux(nb_decimal:float)->int: #fonction puissance 2 //PAR QUENTIN
    """
    Fonction puissance de deux

    entrée 
        nb_decimal float nombre traduit avec la norme IEE754
    sortie
        valeur numérique int retourne l'exposant
    """
    if nb_decimal == 0: #regarde si le nombre est égal à 0
        return -127 #ok
    for i in range(-128,128): #pour i compris entre -128 et 128
        if 2**(i-1) <= nb_decimal < 2**i: #vérifie l'exposant
            return i-1 #return l'exposant

def base10_2_entier(nb_decimal:float)->str: # /PAR MILAN
    """
    Fonction de conversion en binaire de la partie entière

    entrée
        nb_decimal float nombre traduit avec la norme IEE754
    sortie
        s str partie entière convertie en binaire
    """
    s = ""
    if nb_decimal==0: #si le nombre estégal à 0
        return s #retourner "rien"
    i = puissance_de_deux(nb_decimal) #i prend la valeur de l'exposany
    while i >= 0: #tant que l'eposant est supérieur/égal à 0
        r = nb_decimal - 2**i #on a le nombre décimal -2 à l'exposant i
        if r >= 0: #on vérifie si le nombre est positif
            s += "1" #s prend valeur 1#test
            nb_decimal = r
        else:
            s += "0" #s prend la valeur 0
        i -= 1
    return s

def calibre_gauche(s:str,nb_decimal:float)->str: #fonction pour remplir avec des 0 à gauche //PAR MILAN
    """
    Calibre gauche

    entrée
        s str chaine à calibrer
        nb_decimal float nombre à traduire avec la norme IEE754
    sortie 
        s str calibre avec des 0
    """
    assert len(s)<=nb_decimal #si la taille de s n'est pas inférieur/égal au nombre décimal
    while len(s) < nb_decimal: #tant que la taille de la chaine s est inférieur au nombre décimal
        s = "0" + s #on a s égal 0
    return s

def calibre_droite(s:str,nb_decimal:float)->str: #fonction pour remplir avec des 0 à droite //PAR MILAN
    """
    Calibre droit

    entrée
        s str chaine à calibrer
        nb_decimal float nombre à traduire avec la norme IEE754
    sortie 
        s str calibre avec des 0
    """
    assert len(s)<=nb_decimal #si la taille de s n'est pas inférieur/égal au nombre décimal
    while len(s) < nb_decimal: #tant que la taille de la chaine s est inférieur au nombre décimal
        s += "0" #on a s égal 0
    return s

def base10_to_2_decimal(nb_decimal:float,m:int)->str: #fonction de conversion #PAR MILAN
    """
    Fonction conversion partie decimal en binaire
    
    entrée
        nb_decimal float nombre à traduire avec la norme IEE754
        m int permet d'avoir la taille de la chaine
    sortie
        s str chainee traduite en binaire
    """
    assert 0<=nb_decimal<1 
    s = ""
    i = -1
    while len(s)<m and nb_decimal != 0: #tant que la longeur de la chaine s est ifnférieur à m et le nombre décimal n'est pas égal à 0
        r = nb_decimal - 2**i #r prend la valeur de 2 à l'exposant i soustrait au nombre décimal
        if r>=0: #donc on a si r est supérieur ou égal à 0
            s += "1" #s prend la 1
            nb_decimal = r
        else:
            s += "0" #s prend la 0
            if s[0]=="0" and "1" not in s: #on a la première valeur prélévé de la chaine s égal à 0 et 1 
                m += 1 #m prend la valeur 1
        i -= 1 
    return s
 
def base2_16(nb_decimal:float)->str: #fonction traduction en hexadecimal // PAR CEDRIC
    """
    Fonction conversion hexadécimale

    entrée
        nb_decimal float nombre à traduire avec la norme IEE754
    sortie
        r str conversion en hexadecimal du nombre
    """
    h = [nb_decimal[i*4:i*4+4] for i in range(0,8)] #h prend la valeur de type 
    c = "0123456789ABCDEF" #valeur chaine hexadécimal
    r = ""
    for y in range(len(h)): #pour y sur la longueur de h occurences
        s = 0
        l = len(h[y]) # tous identiques en theorie, l prend la valeur de la longueur de la chaine h 
        for i in range(l):
            s += int(h[y][i])*2**(l-i-1) #on a les valeurs extraites fois 2 à l'exposant l moins i moins 1
        r += c[s]  #r coresspond à la valeur de la chaine c extraites avec l'id de s
    return r

def translate_127(nb_decimal:float,s:str="+")->float: #pas besoin d'expliquer la fonction car juste un clacul simple // PAR QUENTIN
    """
    fonction translate_127

    entrée
        nb_decimal float nombre à traduire avec la norme IEE754
        s str signe 
    sortie
        r float exposant
    """
    if s == "-":
        r = nb_decimal-127
    else:
        r = nb_decimal+127
    assert 0 <= r <= 255
    return r

def donner_apres_virgule(nb_decimal:float)->float:
    """
    Fonction donner_apres_virgule
    
    entrée
        nb_decimal float nombre à traduire avec la norme IEE754
    sortie
        valeur numérique float modulo de nb_decimal
    """
    return nb_decimal%1 #nombre decimal modulo de 1

def donner_avant_virgule(nb_decimal:float)->float:
    """
    Fonction donner_avant_virgule
    
    entrée
        nb_decimal float nombre à traduire avec la norme IEE754
    sortie
        valeur numérique float modulo de nb_decimal
    """
    return (nb_decimal-nb_decimal%1) #nombre decimal moins nombre décimal modulo de 1

def presentation_resultat_base_2(s): #fonction présentation fonction
    print("[R] résultat :", s[0]+" "+s[1:9]+" "+s[9:])

def main():   
 """ 
 Fonction d'affichage du résultat.
 """
 while True:
    
    # question
    nb_decimal = float(input("Entrez le nombre décimal à convertir en norme IEEE 754? "))
    assert -2**128 <= nb_decimal <= 2**128-1

    # signe
    signe_s = str(signe(nb_decimal))
    nb_decimal= abs(nb_decimal)

    # exp
    exp = puissance_de_deux(nb_decimal)
    exp_s = calibre_gauche(base10_2_entier(translate_127(exp)),8)
    #print("[I] La valeur absolue du nombre appartient à [", 2**exp, ";", 2**(exp+1), "[")

    # mantisse
    if exp_s == "00000000":
        print("[I] notation underflow")
        print("[R] non codé : on prend 0")
        mantisse = calibre_droite(base10_2_entier(0),23)
        presentation_resultat_base_2(signe_s+exp_s+mantisse)
        print("[R] héxadécimal :", base2_16(signe_s+exp_s+mantisse))
    else:
        print("[I] notation normale")
        partie_entiere = base10_2_entier(donner_avant_virgule(nb_decimal))
        print("[I] partie entière :", partie_entiere) 
        partie_decimale = base10_to_2_decimal(donner_apres_virgule(nb_decimal),23)
        print("[I] partie décimale brute :", partie_decimale)
        mantisse = partie_entiere + partie_decimale
        while mantisse[0] == "0":
            mantisse = mantisse[1:]
        mantisse = mantisse[1:]
        print("[I] mantisse brute :", mantisse)
        if len(mantisse)>23:
            mantisse = mantisse[:23]
        mantisse = calibre_droite(mantisse,23)
        presentation_resultat_base_2(signe_s+exp_s+mantisse)
        print("[R] héxadécimal :", base2_16(signe_s+exp_s+mantisse))
    print()
main()
#fin :D Cédric, Quentin, Milan