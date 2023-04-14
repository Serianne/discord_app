import streamlit as st
import streamlit.components.v1 as components
from bloxs import B
import Fonction_stat_viz.viz as viz
import Fonction_wordcloud.wordcloud as wc
import pandas as pd


### Partie dashboard

def moyenne_convers_mensuelle(dataframe_mois, input_mois): 
    df_moyenne_mensuelle = dataframe_mois[dataframe_mois["month_str"] == input_mois]
    df_moyenne_mensuelle["Timestamp"] = pd.to_datetime(df_moyenne_mensuelle["Timestamp"], format= '%Y-%m-%d %H:%M:%S.%f')
    df_moyenne_mensuelle["date"] = df_moyenne_mensuelle["Timestamp"].dt.date
    moyenne = round(df_moyenne_mensuelle.groupby("date")["texte_clean"].count().mean())
    return moyenne


def moyenne_convers_anuelle(dataframe_annee, input_annee): 
    df_moyenne_anuelle = dataframe_annee[dataframe_annee["year"] == input_annee]
    df_moyenne_anuelle["Timestamp"] = pd.to_datetime(df_moyenne_anuelle["Timestamp"], format= '%Y-%m-%d %H:%M:%S.%f')
    df_moyenne_anuelle["date"] = df_moyenne_anuelle["Timestamp"].dt.date
    moyenne = round(df_moyenne_anuelle.groupby("date")["texte_clean"].count().mean())
    return moyenne

def moyenne_convers_tout_df(dataframe): 
    dataframe["Timestamp"] = pd.to_datetime(dataframe["Timestamp"], format= '%Y-%m-%d %H:%M:%S.%f')
    dataframe["date"] = dataframe["Timestamp"].dt.date
    moyenne = round(dataframe.groupby("date")["texte_clean"].count().mean())
    return moyenne


def dashboard_show(dataframe):
    anne_df = dataframe["year"].unique().tolist()
    anne_df.sort()

    
    espace_1, bloc, espace_2 = st.columns([0.5, 4, 0.5])

    mot_le_plus_frequent = wc.wordcloud_all_freq(dataframe)

    with bloc:
        st.header("Corpus")    
        blox_stats_gene = B([
                    B(len(dataframe), "Total des messages", points=[len(dataframe[dataframe["month"] == i]) for i in range(1,13)], 
                                                chart_type="bar", color="green"),
                    
                    B(len(dataframe["year"].unique()), "Année(s) disponible(s)", points=[len(dataframe[dataframe["year"] == i]) for i in dataframe["year"].unique() ], 
                                                chart_type="stepped", color="red"),

                    B(round(moyenne_convers_tout_df(dataframe)), 
                                        "Moyenne messages/jours", points=[len(dataframe[dataframe["day_str"] == i]) for i in dataframe["day_str"].unique() ], 
                                                chart_type="line", color="royalblue"),
                    
                    B(mot_le_plus_frequent, "Mot le plus fréquent du corpus", percent_change= round(len(dataframe[dataframe["texte_clean"].str.contains(mot_le_plus_frequent)])/len(dataframe) *100, 2))

                ])._repr_html_()
            
        components.html(blox_stats_gene, width=1100, height=400, scrolling=True)

        choix_annee = st.selectbox("Selectionnez une année : ", anne_df)

    # Conteneur partie annuelle
    with st.expander("Dashboard par année "):

        # Créer un quadrillage pour agencer les graphiques

        vide_titre, ligne_titre, ligne_titre2, ligne_titre3 = st.columns([0.1, 2 ,0.5, 3])
        with ligne_titre:
            st.subheader("Chiffres pour {}".format(choix_annee))
        
        with ligne_titre3:
            st.subheader("Evolution par année/mois des messages")

        vide2_1, ligne2_1, ligne2_2, ligne2_3, ligne2_4, ligne2_5, vide2_2 = st.columns([0.1, 0.5, 0.5, 0.6, 0.1, 3, 0.1])

        with ligne2_1:
            motannee = wc.wordcloud_mot_annee(dataframe, choix_annee)
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.image("mot_annee.png", use_column_width="auto")
            st.metric(label="Mot de l'année:", value=motannee)

        with ligne2_2:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.image("icone_nbr_convers.png", use_column_width="auto")
            st.metric(label="Messages", value=len(dataframe[dataframe["year"] == choix_annee]))

        with ligne2_3:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.image("moyenne_an.png", use_column_width="auto")
            st.metric(label="Moyenne messages/mois", value=moyenne_convers_anuelle(dataframe, choix_annee))

        with ligne2_5:
            viz.line_plot_an(dataframe)
            
            

        vide2_1, ligne2_titre, ligne2_titre2, ligne2_titre3, vide2_2 = st.columns([0.2, 2.5 ,0.1, 3.5, 0.1])

        with ligne2_titre:
            st.subheader("Messages par mois")
        
        with ligne2_titre3:
            st.subheader("Messages jour/mois ")




        # Les 2 dernières lignes du dashboard annuel
        ligne1_1, vide1_1, ligne1_2,  = st.columns([2, 0.5, 4])
        with ligne1_1:

            viz.graph_donut_mois(dataframe, choix_annee)
            st.write("Cliquez pour cocher/décocher.")
        with ligne1_2:
            
            viz.graph_repartition(dataframe, choix_annee)


    ### Deuxième partie 

    # En dehors du conteneur option pour définir le choix du mois sur lequel faire un focus        
    df_mois = dataframe[dataframe["year"] == choix_annee]
    mois_df = df_mois["month_str"].unique().tolist()

    # Conteneur partie mensuelle
    with st.expander("Dashboard par mois"):
        # Selecteur mois

        col_vide1, col_header1, col_input, col_vide3 = st.columns([0.05, 0.5, 0.6, 2])
        with col_header1 : 
            st.header("Focus sur :")

        with col_input:    
            select_mois = st.selectbox("", mois_df)
        

        # Lignes pour agencer le dashboard mensuel
        vide1_1, ligne1_1, vide1_2, bloc1_1, vide1_3, ligne1_2, vide1_4 = st.columns([0.10, 0.8, 0.50, 2, 0.5, 2.4, 0.2])
        with ligne1_1:
            st.image("nbr_mess_mois.png", use_column_width="auto")
            st.metric(label="Messages :", value=len(df_mois[df_mois["month_str"] == select_mois]))

            st.image("moyenne_an.png", use_column_width="auto")
            st.metric(label="Moyenne message/mois:", value= moyenne_convers_mensuelle(df_mois, select_mois))

            st.image("podium.png", use_column_width="auto")
            st.metric(label="Le mot le plus fréquent :", value= wc.wordcloud_all_freq_mois(df_mois, select_mois))
        with bloc1_1:
            st.write(" ")
            st.write(" ")
            st.subheader("Répartition hebdomadaire")
 
            viz.graph_pieplot_day(df_mois, select_mois)

        with ligne1_2:
            st.write(" ")
            st.write(" ")
            st.subheader("Les 10 mots les plus fréquents")
            viz.freq_mot_mois(df_mois, select_mois)

            

    
