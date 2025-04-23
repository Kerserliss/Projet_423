import streamlit as st
import Profil_hydrophobicité as ph

st.title("Profil d'hydrophobicité")
st.write( "Choissisez l'echelle a utilisé parmi la liste ci-dessous ")
st.selectbox(" Echelle : ", ['Kyte','Colette','la 3 '])
