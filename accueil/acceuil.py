import streamlit as st
import Fonction_wordcloud.wordcloud as wc

### Partie Présentation

def choix_acceuil(dataframe):

    st.header("Accueil")
    st.write(" ")
    st.write("Cette application a pour but de réaliser une rapide étude de texte sur des conversations Discord sur les années 2019, 2020 et 2022.")
    st.write("L'année 2021 n'est pas présente dans le corpus.")
    st.write("Elle permettra de visualiser les thèmes les plus réccurents sur les conversations via des wordclouds pour les illustrer.")
    st.write("Une page est dédiée pour voir la répartitions des conversations en fonction des années, et une gallerie est disponible pour voir les différents wordclouds.")
    st.write('De nombreux terme employés font références à un contexte gaming, comme les pseudonymes, des expressions gamers, ou encore des angliscismes.')

    st.write(" ")
    st.write("Le texte d'origine a été nettoyé en amont grâce à _Python_, et lemmatisé pour obtenir ce résultat.")
    st.write(" ")
    st.write(" ")

    vide_1, graph, vide2 = st.columns([1, 5, 1])
    with graph:
        st.divider()
        wc.wordcloud_all_df(dataframe)
        st.divider()
    
    st.write(" ")
    st.write(" ")
    st.write("Pour réaliser cette application les outils suivants ont été utilisé :")
    st.write("_Pandas_, _Wordcloud_, _NLTK_, _Spacy_, _MatplotLib_, _Seaborn_, _Plotly_ _Express_, _Numpy_, _Bloxs_, _Pil_ et _Streamlit_")
    st.write(" ")
    st.write("Les images proviennent de _[Flaticon](https://www.flaticon.com/)_, et ont été crée par _Freepik_ et _Aldo Cervantes_.")




