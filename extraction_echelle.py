#Projet BI423 Ellyna Soumelis , Percevault Lysa, LDDI

#Extraction des données du fichier PDB

from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa

def extraction(file, filename):
    """On extrait les données du fichier pdb
        Paramètre :
            file : type de structure
            filename: nom du fichier """
    
    parser = PDBParser(QUIET=True)#on évite d'afficher les anomalies du fichier 
    structure = parser.get_structure(file, filename)#on récupère la structure de la protéine avec toute les informations
    return structure 

extraction('pdb','prot.pdb')


def dico_aa():
    """On convertit chaque acide aminé en 1 seul caractère 
    correspondant pour pouvoir les faire correspondre aux échelles d'hydrophobicité """
    
    file = open('aa.txt', 'r')#on ouvre le fichier texte 
    aa = {}#on créé un dictionnaire vide 

    line = list(file.readline().strip().upper().split(' '))#chaque ligne du fichier texte est transformé en liste 

    cle = line[0]#le premier élément correspondant aux 3 caractères est définis comme la clé 
    valeur = line[1]#le deuxième élément correspondant à 1 seul caractère est définis comme la valeur 
    if cle not in aa:
        aa[cle] = valeur

    for line in file:#on parcours toute les lignes du fichier 

        line = list(line.strip().upper().split(' '))

        if len(line) < 2 :
            continue 
        cle = line[0]
        valeur = line[1]
        
        if cle not in aa:#on ajoute les valeurs dans le dictionnaire 
            aa[cle] = valeur

    file.close()   
    return aa

def dico_echelle_K_D():
    """On transforme le fichier des valeurs de l'echelle de Kyte et Doolittle en dictionnaire"""
    
    file = open("echelle_K_D.txt", "r")
    echelle = {}

    line = list(file.readline().strip().split(' '))

    cle = line[0]#la clé est l'acide aminé 
    valeur = line[1]#la valeur correspond à son hydrophobicité 
    if cle not in echelle:
        echelle[cle] = valeur
    
    for line in file :
        line = list(line.strip().upper().split(' '))

        if len(line) < 2 :
            continue 
        cle = line[0]
        valeur = line[1]
        
        if cle not in echelle:
            echelle[cle] = valeur
    
    file.close()
    
    return echelle 

def dico_HW():
    """On convertit le fichier texte de l'échelle Hop et Woods en un dictionnaire"""
    file = open("echelle_HW.txt", "r")
    echelle = {}

    line = list(file.readline().strip().split(' '))

    cle = line[0]
    valeur = line[1]
    if cle not in echelle:
        echelle[cle] = valeur
    
    for line in file :
        line = list(line.strip().upper().split(' '))

        if len(line) < 2 :
            continue 
        cle = line[0]
        valeur = line[1]
        
        if cle not in echelle:
            echelle[cle] = valeur
    
    file.close()
    
    return echelle 

def dico_C():
    """On transforme le fichier texte de l'echelle de Cornette en dictionnaire """
    file = open("echelle_C.txt", "r")
    echelle = {}

    line = list(file.readline().strip().split(' '))

    cle = line[0]
    valeur = line[1]
    if cle not in echelle:
        echelle[cle] = valeur
    
    for line in file :
        line = list(line.strip().upper().split(' '))

        if len(line) < 2 :
            continue 
        cle = line[0]
        valeur = line[1]
        
        if cle not in echelle:
            echelle[cle] = valeur
    
    file.close()
    
    return echelle 


def acide_amine(file, filename):
    """On récupère les acides aminés du fichier et on les convertit 
    en 1 seul caractère car dans le fichier c'est 1 seul caractère
    Paramètre : 
        file : type de donnée
        filename : nom du fichier à analyser"""
    
    data = extraction(file,filename)#on obtien la structure
    aa = dico_aa()
    liste_aa = {}#on initialise un dictionnaire pour stocker les données des acides aminés
    liste_id =[]#on initialise une liste pour stocker les id des chaines des acides aminés
    for model in data:#on regarde pour chaque etat 3D de la protéine
        for chain in model:#on regarde chaque chaine d'aa dans l'etat 3D
            c_id = chain.get_id()
            if c_id not in liste_id:
                liste_id.append(c_id)
                for residue in chain :#on regarde chaque acide aminé de la chaine 
                    if is_aa(residue, standard = True):#on vérifie que c'est un acide aminé correspondant aux acides aminés standard 
                        res_nom = residue.get_resname()#on récupère le nom de l'aa
                        if res_nom in aa:
                            nom = aa[res_nom]
                            res_id = residue.get_id()[1]#on récupère sa position
                            if res_id not in liste_aa:#si la chaine n'est pas déjà dans le dico on l'ajoute
                                liste_aa[res_id] = nom#la clé du dictionnaire est la position de l'aa et la valeure est l'aa

    return liste_aa


def profil_hydro(file, echelle):
    """On construit le dictionnaire de l'hydrophobicité des aa de la protéine 
    la clé est la position de l'aa dans la chaine de la prot, et la valeur est une liste qui contient l'aa et son hydrophobicité
    Paramètre : 
        file : fichier pdb de la protéine
        echelle : fonction dictionnaire de l'echelle que l'on souhaite utiliser """

    aa = acide_amine('proteine', file)#on récupère le dictionnaire des aa de la prot avec leur position comme clé et l'aa en valeur
    hydro = echelle#on récupère le dictionnaire de l'echelle avec comme clé l'aa et la valeur son hydrophobicité

    profil = {}#on intialise le dicitonnaire qui contient tout 

    for key in aa :#on parcours le dico des aa en fonction des clés donc des positions de l'aa
        for cle in hydro :#on parcours le dico de l'echelle en fonction des clés donc de l'aa
            if aa[key] == cle:

                if key not in profil:
                    profil[key] = []#on intialise pour chaque position comme valeur une liste
                    valeur1 = aa[key] #acide aminé
                    valeur2 = hydro[cle]#hydophobicité
                    profil[key].append(valeur1)#on ajoute l'aa
                    profil[key].append(valeur2)#on ajoute l'hydophobicité

    return profil










