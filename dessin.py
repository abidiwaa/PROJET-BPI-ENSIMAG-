"""liste_imagedule contenant les fonctions de dessin des chiffres"""


def ligne(vert,horiz,liste_image):
    """Fonction pour dessiner une ligne"""
    for i in range(vert[0],vert[1]):
        for j in range(horiz[0],horiz[1]):
            liste_image[i][j]="0 0 0\n"


def dessiner_point(taille,liste_image):
    """Fonction pour dessiner un point"""
    milieu=int(taille/2)
    mouvement=int(taille/9)+int(taille/6)
    pas=int(taille/15)
    ligne((milieu+pas+10,milieu+pas+20),(mouvement+pas+7,mouvement+pas+18),liste_image)

def dessiner(i,taille,liste_image,pos):
    """Fonction pour dessiner chaque chiffre selon les cas"""
    milieu=int(taille/2)
    if pos in (1,2):
        mouvement=int(pos*(taille/9))+int(taille/6)
    if pos>2:
        mouvement=int(int(taille/6)+pos*(taille/9))-int(taille/9)+int((taille/85))
    pas=int(taille/15)
    if i==3:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas+10,milieu),(mouvement+pas-10,mouvement+pas),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+10,milieu+pas+10),(mouvement+pas-10,mouvement+pas),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
    if i==1:
        ligne((milieu-pas,milieu+pas+20),(mouvement,mouvement+int((pas/8))),liste_image)
    if i==2:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas+10,milieu),(mouvement+pas-10,mouvement+pas),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+10,milieu+10+pas),(mouvement,mouvement+10),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
    if i==0:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement,mouvement+10),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement+pas,mouvement+pas+10),liste_image)
    if i==4:
        ligne((milieu-pas,milieu),(mouvement,mouvement+10),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement+pas,mouvement+pas+10),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas+10),liste_image)
    if i==5:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas,milieu),(mouvement,mouvement+10),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+10,milieu+pas+10),(mouvement+pas-10,mouvement+pas),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
    if i==6:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas,milieu),(mouvement,mouvement+10),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+10,milieu+pas+10),(mouvement+pas-10,mouvement+pas),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+10,milieu+10+pas),(mouvement,mouvement+10),liste_image)
    if i==7:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement+pas,mouvement+pas+10),liste_image)
    if i==8:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement+pas,mouvement+pas+10),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement,mouvement+10),liste_image)
    if i==9:
        ligne((milieu-pas,milieu-pas+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu,milieu+10),(mouvement,mouvement+pas),liste_image)
        ligne((milieu+pas+10,milieu+pas+20),(mouvement,mouvement+pas),liste_image)
        ligne((milieu-pas,milieu+pas+20),(mouvement+pas,mouvement+pas+10),liste_image)
        ligne((milieu-pas,milieu+pas+10),(mouvement,mouvement+10),liste_image)
