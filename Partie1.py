#Projet BI423
#Extraction des données du fichier PDB
from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa

def extraction(file, filename):
    parser = PDBParser(QUIET=True)#on évite d'afficher les anomalies du fichier 
    structure = parser.get_structure(file, filename)#on récupère la structure de la protéine avec toute les informations

    return structure 


def acide_amine():
    data = extraction()#on obtien la structure

    liste_aa = {}#on initialise un dictionnaire pour stocker les données des acides aminés

    for model in data:#on regarde pour chaque etat 3D de la protéine
        for chain in model:#on regarde chaque chaine d'aa dans l'etat 3D
            c_id = chain.get_id()

            if c_id not in liste_aa:#si la chaine n'est pas déjà dans le dico on l'ajoute
                liste_aa[c_id] = []

                for residue in chain :#on regarde chaque acide aminé de la chaine 
                    if is_aa(residue, standard = True):
                        res_nom = residue.get_resname()#on récupère le nom de l'aa
                        res_id = residue.get_id()[1]#on récupère sa position
                        liste_aa[c_id].append((res_nom, res_id))#on ajoute les données dans le dico
    
    return liste_aa





