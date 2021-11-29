"""Code du Projet BPI pour générer une image gif
 de simulations de pi par la méthode de Monte Carlo
"""
import random
import sys
from subprocess import call
from time import time
import dessin
import simulator
taille = sys.argv[1]
pts_simu = sys.argv[2]
pts_virg = sys.argv[3]


def entiers_de_sim(simu, virg):
    """retourne une liste contenant
     les entiers à dessiner dans le bon ordre de gauche à droite"""
    liste=[]
    chaine_chiffres= str(int(simulator.simulator_pi(int(simu))*(10**int(virg))))
    for i in range(len(chaine_chiffres)):
        liste.append(int(chaine_chiffres[i]))
    return liste


def generate_ppm_file(taille_, simu, virg):
    """génère image ppm"""
    image_blanche=[["255 255 255\n" for i in range(int(taille_))] for j in range(int(taille_))]
    cpt = 0
    while cpt<(int(simu)):
        i = int(random.uniform(0, int(taille_)-1))
        j = int(random.uniform(0, int(taille_)-1))
        if (((int(taille_)/2)-i)**2 + ((int(taille_)/2)-j)**2) <= (int(taille_)/2)**2:
            image_blanche[i][j] = "255 0 0\n"
            cpt+=1
        else:
            image_blanche[i][j] = "0 0 255\n"
            cpt+=1
    nom = f'img{int((10/(int(sys.argv[1])))*int(simu))}.ppm'
    dessin.dessiner_point(int(taille_), image_blanche)
    for i in range(len(entiers_de_sim(int(simu), int(virg)))):
        dessin.dessiner(entiers_de_sim(int(simu), int(virg))[i], int(taille_), image_blanche, i+1)
    fichier = open(nom, 'w')
    fichier.write('P3\n')
    fichier.write(f'{int(taille_)} {int(taille_)}\n255\n')
    for j in range(int(taille_)):
        fichier.writelines(image_blanche[j])
    fichier.close()
    return nom


def generate_gif():
    """génère le gif demandé"""
    gif_list= []
    for i in range(1, 11):
        gif_list.append(generate_ppm_file(taille, (i*int(pts_simu))/10, int(pts_virg)))
    call(['convert', '-delay', '100']+gif_list+['Projet.gif'])



def err(liste):
    """génère gif si tout fonctionne bien et lance des exceptions
    dans le cas de valeurs négatives ou type non entier ou trop de
     nombres demandés après la virgule"""
    for j in liste:
        if j[1:].isdigit() and int(j)<=0:
            raise ValueError("Valeur négative ou nulle")
        if not j.isdigit():
            raise ValueError("Type non entier")
    if liste[2].isdigit() and int(liste[2]) >6:
        raise ValueError ("Trop de nombres après la virgule")
    return generate_gif()




t1=time()
err([taille,pts_simu,pts_virg])
t2=time()
print(t2-t1)
