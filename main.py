import streamlit as st
import Profil_hydrophobicite as ph
import extraction_echelle as exc
from io import StringIO, BytesIO

scale_dic = {'Kyte - Doolittle' : [7,exc.dico_echelle_K_D()], 'Hopp-Woods' : [9,exc.dico_HW()],'Cornette' : [5,exc.dico_C()]}  # Pour definir les échelles

st.title("Hydrophobicity profil ")  # Titre de la page principale


with st.sidebar:  # Pour definir le menu sur la gauche
    st.title(" Choose your inputs : ")  # Titre de la page
    scale = st.selectbox(" Scale : ", list(scale_dic.keys()),index=0)  # On crée un endroit pour selectionner l'échelle
    size = st.slider(" Windows lenght : ", min_value= 0, max_value= 50, value= scale_dic[scale][0])  # Même chose pour la taille

    file = st.file_uploader("Put your protein.pdb in this : ",type ='pdb')  # Endroit pour déposer le fichier
    if file :  # Si on a le fichier, on récupère son nom
        file_n = StringIO(file.getvalue().decode('utf-8'))
        if st.button('Load') :  # Le bouton pour lancer l'opération
            st.session_state['ready'] = True  # On met notre variable ready a True dans notre session

if st.session_state.get('ready',False):  # Si on a le bouton cliqué, on lance sinon on met False pour initiliaser la valeur

    # On donne l'échelle en fonction du choix de l'utilisateur
    dico_seq = exc.profil_hydro(file_n,scale_dic[scale][1])
    fig = ph.profil_hydrophobicite(dico_seq, size)  # On récupère la figure
    st.pyplot(fig)  # On affiche le plot

    # On affiche un bouton pour save le fichier 
    save_name = st.text_input(label = "File save name without the extension: ")

    # Ici on couvertit le fichier en Bytes pour que streamlit accepte le fichier .
    save_data = BytesIO()  # On ouvreun fichier de type Bytes
    fig.savefig(save_data, format ='svg', dpi = 400)  # On sauvegarde notre figure dedans en svg
    save_data.seek(0)  # On remet a la position 0

    # Si on a le nom, on affiche le bouton
    if save_name :
        if st.download_button(label = 'Save Button ', data = save_data, file_name= save_name +'.svg') : # Si le bouton est cliqué, alors on save
            st.session_state['ready'] = False  # Et on met a False l'état de la variable ready
    


