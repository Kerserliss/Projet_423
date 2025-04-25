#Projet BI423
#Extraction des données du fichier PDB
from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa

def extraction(file, filename):
    parser = PDBParser(QUIET=True)#on évite d'afficher les anomalies du fichier 
    structure = parser.get_structure(file, filename)#on récupère la structure de la protéine avec toute les informations

    return structure 

#il faut convertir chaque acide amine en 1 caractère pour pouvoir correspondre au valeur de l'echelle choisit 
#je créé un dico pour pouvoir ensuite comparé les aa de la prot au dico et ainsi convertir les 3 caractères en 1 seul
#sans avoir le besoin de faire pleins de if 
def dico_aa():
    file = open('aa.txt', 'r')
    aa = {}

    line = list(file.readline().strip().upper().split(' '))

    cle = line[0]
    valeur = line[1]
    if cle not in aa:
        aa[cle] = valeur

    for line in file:
        line = list(line.strip().upper().split(' '))

        if len(line) < 2 :
            continue 
        cle = line[0]
        valeur = line[1]
        
        if cle not in aa:
            aa[cle] = valeur

    file.close()
    print(aa)   
    return aa



def acide_amine(file, filename):
    data = extraction(file,filename)#on obtien la structure
    aa = dico_aa()
    liste_aa = {}#on initialise un dictionnaire pour stocker les données des acides aminés

    for model in data:#on regarde pour chaque etat 3D de la protéine
        for chain in model:#on regarde chaque chaine d'aa dans l'etat 3D
            c_id = chain.get_id()

            if c_id not in liste_aa:#si la chaine n'est pas déjà dans le dico on l'ajoute
                liste_aa[c_id] = []

            for residue in chain :#on regarde chaque acide aminé de la chaine 
                 if is_aa(residue, standard = True):
                    res_nom = residue.get_resname()#on récupère le nom de l'aa
                    print(res_nom)
                    if res_nom in aa:
                        nom = aa[res_nom]
                        res_id = residue.get_id()[1]#on récupère sa position
                        liste_aa[c_id].append((nom, res_id))#on ajoute les données dans le dico
    print(liste_aa)
    return liste_aa

acide_amine('proteine', 'prot.pdb')#verification de la fonction 








