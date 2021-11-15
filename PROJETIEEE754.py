
def signe(nb_decimal):
    if nb_decimal<0:
        return 1
    return 0

def puissance_de_deux(nb_decimal):
    if nb_decimal == 0:
        return -127
    for i in range(-128,128):
        if 2**(i-1) <= nb_decimal < 2**i:
            return i-1

def base10_2_entier(nb_decimal):
    s = ""
    if nb_decimal==0:
        return s
    i = puissance_de_deux(nb_decimal)
    while i >= 0:
        r = nb_decimal - 2**i
        if r >= 0:
            s += "1"
            nb_decimal = r
        else:
            s += "0"
        i -= 1
    return s

def calibre_gauche(s,nb_decimal):
    assert len(s)<=nb_decimal
    while len(s) < nb_decimal:
        s = "0" + s
    return s

def calibre_droite(s,nb_decimal):
    assert len(s)<=nb_decimal
    while len(s) < nb_decimal:
        s += "0"
    return s

def base10_to_2_decimal(nb_decimal,m):
    assert 0<=nb_decimal<1
    s = ""
    i = -1
    while len(s)<m and nb_decimal != 0:
        r = nb_decimal - 2**i
        if r>=0:
            s += "1"
            nb_decimal = r
        else:
            s += "0"
            if s[0]=="0" and "1" not in s:
                m += 1
        i -= 1
    return s

def base2_16(nb_decimal):
    h = [nb_decimal[i*4:i*4+4] for i in range(0,8)]
    c = "0123456789ABCDEF"
    r = ""
    for y in range(len(h)):
        s = 0
        l = len(h[y]) # tous identiques en theorie
        for i in range(l):
            s += int(h[y][i])*2**(l-i-1)
        r += c[s]
    return r

def translate_127(nb_decimal,s="+"):
    if s == "-":
        r = nb_decimal-127
    else:
        r = nb_decimal+127
    assert 0 <= r <= 255
    return r

def donner_apres_virgule(nb_decimal):
    return nb_decimal%1

def donner_avant_virgule(nb_decimal):
    return (nb_decimal-nb_decimal%1)

def presentation_resultat_base_2(s):
    print("[R] résultat :", s[0]+" "+s[1:9]+" "+s[9:])
    
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
        print("[R] non codé : on prend 0")
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

