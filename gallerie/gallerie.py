import streamlit as st
import Fonction_wordcloud.wordcloud as wc

### Partie Gallrie
# Fair un afficge de 3 x 4 wordclouds grace à une grille de colonnes/lignes
def gallerie_show(dataframe):

    #  number = st.number_input("l'année pour generer le Wordcloud")
    annee_df = dataframe["year"].unique().tolist()
    option = st.selectbox("Selectionnez une année pour changer les wordclouds", annee_df)

    st.write(" ")
    st.write(" ")
    st.subheader("Appuyer sur la double flèche pour agrandir l'image.")
    st.write(" ")
    st.write(" ")

    # Première ligne de 4 wordclouds
    ligne1_espace1, ligne1_1, ligne1_espace2, ligne1_2, ligne1_espace3, ligne1_3, ligne1_espace4, ligne1_4  = st.columns(
        # 0.1 pour délimiter la colonne/ligne vide et 1 pour les pleines (pour définir comment se réparti l'image)
        (0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1)
    )

    with ligne1_1:
        wc.wordcloud_mensuel(dataframe, option, 'Janvier')


    with ligne1_2:
        wc.wordcloud_mensuel(dataframe, option, 'Février')

    with ligne1_3:
        wc.wordcloud_mensuel(dataframe, option, 'Mars')

    with ligne1_4:
        wc.wordcloud_mensuel(dataframe, option, 'Avril')

       # Deuxième ligne de 4 wordclouds
    ligne2_espace1, ligne2_1, ligne2_espace2, ligne2_2, ligne2_espace3, ligne2_3, ligne2_espace4, ligne2_4  = st.columns(
        # 0.1 pour délimiter la colonne/ligne vide et 1 pour les pleines (pour définir comment se réparti l'image)
        (0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1)
    )

   
    with ligne2_1:
        wc.wordcloud_mensuel(dataframe, option, 'Mai')

    with ligne2_2:
        wc.wordcloud_mensuel(dataframe, option, 'Juin')

    with ligne2_3:
        wc.wordcloud_mensuel(dataframe, option, 'Juillet')

    with ligne2_4:
        wc.wordcloud_mensuel(dataframe, option, 'Août')

        # Troisième ligne de 4 wordclouds
    ligne3_espace1, ligne3_1, ligne3_espace2, ligne3_2, ligne3_espace3, ligne3_3, ligne3_espace4, ligne3_4  = st.columns(
        # 0.1 pour délimiter la colonne/ligne vide et 1 pour les pleines (pour définir comment se réparti l'image)
        (0.1, 1, 0.1, 1, 0.1, 1, 0.1, 1)
    )
    
    with ligne3_1:
        wc.wordcloud_mensuel(dataframe, option, 'Septembre')

    with ligne3_2:
        wc.wordcloud_mensuel(dataframe, option, 'Octobre')

    with ligne3_3:
        wc.wordcloud_mensuel(dataframe, option, 'Novembre')

    with ligne3_4:
        wc.wordcloud_mensuel(dataframe, option, 'Décembre')