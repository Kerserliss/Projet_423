#Module pour gérer la creation du profil d'hydrophobicité 
import matplotlib.pyplot as plt 
#import scale as sc

def calcul_bidon(fenetre,scale):  # Pour gerer les calculs 
    fenetre = fenetre.upper()  # On met tout en maj dans le doute
    # Chaque acide amné, on lui attripue son score 
    # Math ici
    calcul = 10
    calcul = calcul / 7 # Size a changé selon échelle
    return calcul

def profil_hydrophobcité(name,seq_prot,scale):
    plt.title(name)
    plt.xlabel(name + ' taille = ' + str(len(seq_prot)))
    plt.ylabel(' Value ')

    size = 7  # Need a odd value
    middle = size //2
    values = []
    for i in range(len(seq_prot)):
        if i < middle:
            fenetre = seq_prot[(i-middle)%middle:i+(size-middle)]  # A changer
        else:
            fenetre = seq_prot[i-middle:i+(size+middle)]  # A changer
        val = calcul_bidon(fenetre)
        values.append(val)

    limy = max(values)
    plt.xlim(0, len(seq_prot))
    plt.ylim(0, limy + 2)

    plt.plot(values)



    
    
