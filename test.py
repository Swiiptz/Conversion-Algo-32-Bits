mantisse = '.010101001' #000011001100110011001100
loca_point = mantisse.find('.') #localisation point dans la mantisse
long_m = len(mantisse) #taille mantisse
m_p1 = mantisse[0:loca_point]#partie gauche mantisse avant le point
m_p1 = '0'
m_p2 = mantisse[(loca_point + 1):long_m] #partie droite de la mantisse après le point
m_wpoint = m_p1 + m_p2 #mantisse sans point
long_m_wpoint = len(m_wpoint) 
m_c1 = m_wpoint[0:1] #caractère 1de la mantisse sans point
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
print(l)
