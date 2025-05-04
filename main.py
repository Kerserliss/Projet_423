import streamlit as st
import Profil_hydrophobicite as ph
import Partie1 as p
from io import StringIO, BytesIO

scale_dic = {'Kyte -Doolitle' : 7, 'Hopp-Woods' : 9}

st.title("Hydrophobicity profil ")

with st.sidebar:
    st.title(" Choose your inputs : ")
    scale = st.selectbox(" Scale : ", list(scale_dic.keys()))
    size = st.slider(" Windows lenght : ", min_value= 0, max_value= 50, value= scale_dic[scale])

    file = st.file_uploader("Put your protein.pdb in this : ",type ='pdb')
    if file :
        file_name = StringIO(file.getvalue().decode('utf-8'))
        dico_seq = p.profil_hydro(file_name)
    ready = st.button('Load')

if ready:
    fig = ph.profil_hydrophobicite(dico_seq, size)
    st.pyplot(fig)