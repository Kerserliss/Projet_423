#Module pour gérer la creation du profil d'hydrophobicité 
import matplotlib.pyplot as plt 
import extraction_echelle as exc
#import scale as sc

def calcul_hydro(fenetre):
    """
    Fonction qui prends en entrée une liste de float et qui renvoie la moyenne de la fenêtre qu'on a donné.
    Paramètres : 
        fenetre : Liste de float.
    """
    sums = sum(fenetre)
    calcul = sums / len(fenetre) # Taille qui correspond anotre echelle.
    return calcul  

def conv_into_list(dico):
    """
    Récupère les floats du dico crée dans le module Partie 1 et retourne une liste
    Paramètre :
        dico : Dictionnaire qui a pour clef la position de l'acide aminée et en valeur
        un tuple contenant l'acide aminé, et l'hydrophobicité associé. 
    """
    return [float(value[1]) for value in dico.values()]

def get_aa(dico):
    liste = [value[0] for value in dico.values()]
    seq =''
    i = 0
    while i < len(liste):
        seq += liste[i]
        i+= 1
    return seq

def profil_hydrophobicite(dic_prot_values,size):
    """
    Fonction qui avec le nom de la protéine, le dictionnaire de la protéine et la taille de fenêtre renvoie un 
    graphe correspondant au profil d'hydrophobicité.
    Paramètres :
        name : Nom de la protéine.
        dic_prot_values : Dictionnaire crée a l'issue de la partie 1.
        size : La taille de la fenêtre.
    """
    list_prot = conv_into_list(dic_prot_values)
    # On calcule le millieu de la fenêtre et on initialize le tableau de valeur
    middle = size //2
    values = []

    # On fait notre boucle pour parcourir tout le long de la liste et de faire la moyenne
    # a chaque fois des acides aminés qui sont avant et après notre position i = middle.
    for i in range(middle,len(list_prot)-middle):  # Pour ne pas calculer les 3 premiers et poiuvoir calculer une moyenne correcte.
        fenetre = list_prot[i-middle:i+middle+1]  # On récupère les valeurs.
        val = calcul_hydro(fenetre)  # On récupère la moyenne.
        values.append(val)  # On ajoute a notre tableau de valeurs
    
    # On trace le graphe.
    fig,axs = plt.subplots()
    axs.plot(values)

    # On nomme le graphe et ses différents axes
    axs.set_title(' Hydrophobicity profil ( Windows size = ' + str(size) +  ' ) ') 
    axs.set_xlabel(' lenght = ' + str(len(list_prot)))
    axs.set_ylabel(' Value ')

    # On retourne la figure
    return fig