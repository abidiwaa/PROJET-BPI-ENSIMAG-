""" Donne une simulation de pi par la méthode de Monte-Carlo"""
from random import uniform


def simulator_pi(nbr_sim):
    """Effectue la simulation"""
    compteur = 0
    for _ in range(1,nbr_sim):
        abscisse = uniform(-1,1)
        ordonnée = uniform(-1,1)
        rayon = abscisse**2+ordonnée**2
        if rayon<=1:
            compteur+=1
    return 4*(compteur/nbr_sim)
