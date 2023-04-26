import streamlit as st
import pandas as pd
import warnings 

import accueil.acceuil as acceuil
import dashboard.dashboard as dashboard
import gallerie.gallerie as gallerie


st.set_option('deprecation.showPyplotGlobalUse', False)
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")


# importer et mettre en cache le df
@st.cache_data
def load_data():
    return pd.read_csv("discord_streamlit.csv",)

df = load_data()




# Menu
st.sidebar.title("Navigation")
options = st.sidebar.selectbox(" ", options=['Présentation', 'Dashboard', 'Galerie',])

# Navigation avec boutons radios

# Première partie : page d'accueil 
if options == 'Présentation':
    acceuil.choix_acceuil(df)

elif options == 'Dashboard':
    dashboard.dashboard_show(df)
    

elif options == 'Galerie':
    gallerie.gallerie_show(df)
    

