import streamlit as st
import Profil_hydrophobicite as ph
import extraction_echelle as exc
from io import StringIO, BytesIO

scale_dic = {'Kyte - Doolittle' : 7, 'Hopp-Woods' : 9,'Cornette' : 5}  # Pour definir les échelles

st.title("Hydrophobicity profil ")  # Titre de la page principale

with st.sidebar:  # Pour definir le menu sur la gauche
    st.title(" Choose your inputs : ")  # Titre de la page
    scale = st.selectbox(" Scale : ", list(scale_dic.keys()),index=0)  # On crée un endroit pour selectionner l'échelle
    size = st.slider(" Windows lenght : ", min_value= 0, max_value= 50, value= scale_dic[scale])  # Même chose pour la taille

    file = st.file_uploader("Put your protein.pdb in this : ",type ='pdb')  # Endroit pour déposer le fichier
    if file :  # Si on a le fichier, on récupère son nom
        file_name = StringIO(file.getvalue().decode('utf-8'))
    ready = st.button('Load')  # Le bouton pour lancer l'opération

if ready and file :  # Si on a le bouton cliqué et le fichier on recupère le dico
    # On donne l'échelle en fonction du choix de l'utilisateur
    if scale =='Kyte - Doolittle':
        dico_seq = exc.profil_hydro(file_name,exc.dico_echelle_K_D())
    elif scale =='Hopp - Woods':
        dico_seq = exc.profil_hydro(file_name, exc.dico_HW())
    elif scale =='Cornette':
        dico_seq = exc.profil_hydro(file_name, exc.dico_C())

    fig = ph.profil_hydrophobicite(dico_seq, size)  # On récupère la figure
    st.pyplot(fig)  # On affiche le plot

    save_file = st.text_input(label = "File save name :")
    st.download_button()
