import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import plotly_express as px
import streamlit as st
import Fonction_wordcloud.wordcloud as wc

# Procédure pour afficher des informations sur le df et retourner le df qui contient les années
def stats_generales(df_fonc, input_annee):
    # annee = input de l'utilisateur
    stats_annee = df_fonc[df_fonc["year"] == input_annee]
    return stats_annee

# Réapartition en fonction de l'année avec legende exterieure
def graph_repartition(df_fonc, input_annee):
    jour_annee = stats_generales(df_fonc, input_annee)
    jour_annee = jour_annee.sort_values(by=["month"])

    # Organiser les jours de la semaine et les mois
    jour_annee["day_str"] = pd.Categorical(jour_annee["day_str"], 
                                ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'])
    order_hue = jour_annee["month_str"].unique().tolist()
    order_legend = list(order_hue)
    order_legend.reverse()
    # 
    sns.set_theme(style="whitegrid",)
    plt.subplots(figsize = (15,7))
    plt.subplot() 
    sns.histplot(data=jour_annee, x="day_str", hue='month_str', element="bars", 
             common_norm=True, multiple="dodge", palette="tab20", stat="count",
             cbar=True, shrink=.8, hue_order=order_hue)
    plt.legend(order_legend, 
                loc="upper right", title='Mois', bbox_to_anchor=(1.15, 1.00))
    #plt.title("Répartition des conversation de {} par mois".format(input_annee))
    plt.xlabel(' ')
    plt.ylabel(' ')
    
    plt.show()
    st.pyplot()

# Pie chart conversations par jour en fonction de l'année
def graph_pieplot_day(df_fonc, input_annee):
        jour_annee = stats_generales(df_fonc, input_annee)

        label = ["Dimanche", "Samedi", "Vendredi", "Jeudi", "Mercredi", "Mardi", 'Lundi',]
        size = [len(jour_annee[jour_annee["day_str"] == label[6]]), len(jour_annee[jour_annee["day_str"] == label[5]]), len(jour_annee[jour_annee["day_str"] == label[4]]),
                len(jour_annee[jour_annee["day_str"] == label[3]]), len(jour_annee[jour_annee["day_str"] == label[2]]), len(jour_annee[jour_annee["day_str"] == label[1]]),
                len(jour_annee[jour_annee["day_str"] == label[0]]), ]

        fig, ax = plt.subplots()
        sns.set_theme(style="whitegrid",)
        ax1 = plt.subplot()
        colors = sns.color_palette('tab20')
        ax1.pie(size,
                labels= label, colors = colors,
                explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,),
                autopct='%1.1f%%', startangle=90)
        ax1.set_title("Réparition par jour des conversation sur l'année {}".format(input_annee))
        plt.tight_layout()
        st.pyplot(fig)


# Donut comparatif pour les mois
def graph_donut_mois_sns(df_fonc, input_annee):

        df_fonc = df_fonc[df_fonc["year"] == input_annee]

        size = [len(df_fonc[df_fonc["month_str"] == month]) for month in df_fonc["month_str"].unique()]
        size.reverse()

        label = df_fonc["month_str"].unique().tolist()
        
        label.reverse()

        sns.set_theme(style="whitegrid",)
        fig, ax = plt.subplots()
        ax1 = plt.subplot()
        colors = sns.color_palette('tab20')
        pie = plt.pie(size,
                colors = colors,
                rotatelabels = 270,
                radius=1.2,
                labeldistance=0.45,
                #autopct='%1.1f%%',
                counterclock=False,
                pctdistance=1.05,
                #wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
                startangle=90)
        
        
        plt.legend(pie[0], label, bbox_to_anchor=(1.05,1.05), loc="upper left", )
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)
        #plt.title("Conversations sur l'annéee {}".format(input_annee))
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)

# Line plot des années

def line_plot_an(dataframe):
    # Créer les labels
    liste_an = dataframe["year"].unique().tolist()
    # Fixer l'ordre des mois
    dataframe["month_str"] = pd.Categorical(dataframe["month_str"], 
                                            ['Janvier', 'Février', 'Mars', "Mai", "Avril", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"])
    # Donner une forme allongée au graph
    fig, ax = plt.subplots(figsize=(10,3))
   
    # Itérer autant de line que d'année dispo
    for an in liste_an:
        df_an = dataframe[dataframe["year"] == an]
        # Changer le thème 
        sns.set_style(style="whitegrid")

        ax = sns.lineplot(data=df_an["month_str"].value_counts(sort=False), label=an, linewidth=2.5)
    # Faire pivoter les mois pour les rendre lisibles
    plt.xticks(rotation=45, ha='right')  
    plt.ylabel("")
    #plt.title("\n Conversations par mois/année \n ")
    # Sortir la légende pour qu'elle ne couvre pas les lignes
    plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1.00))
    plt.show()
    st.pyplot(fig)


# Pie chart conversations par jour en fonction du mois
def graph_pieplot_day(df_fonc, input_mois):
        df_mensuel = df_fonc[df_fonc["month_str"] == input_mois]

        label = ['Lundi', "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",]
        size = [len(df_mensuel[df_mensuel["day_str"] == label[0]]), len(df_mensuel[df_mensuel["day_str"] == label[1]]), len(df_mensuel[df_mensuel["day_str"] == label[2]]),
                len(df_mensuel[df_mensuel["day_str"] == label[3]]), len(df_mensuel[df_mensuel["day_str"] == label[4]]), len(df_mensuel[df_mensuel["day_str"] == label[5]]),
                len(df_mensuel[df_mensuel["day_str"] == label[6]]), ]
       
        size_pie = []
        label_pie = []
        liste_explode = []
        for i, (label, size) in enumerate(zip(label, size )):
                if size != 0 :
                        size_pie.append(size)
                        label_pie.append(label)
                        liste_explode.append(0.10)

        fig, ax = plt.subplots(figsize=(5,3))
        sns.set_theme(style="whitegrid",)
        ax1 = plt.subplot()
        colors = sns.color_palette('deep')
        ax1.pie(size_pie,
                labels= label_pie, colors = colors,
                explode = liste_explode, 
                autopct='%1.0f%%', startangle=90, counterclock=False)
        plt.tight_layout()
        st.pyplot(fig)


# Barplot des 10 mots les plus réccurents

def freq_mot_mois(dataframe, input_mois):
    df_mois_fonc = dataframe[dataframe["month_str"] == input_mois]
    all_texte_mois = " ".join(df_mois_fonc["texte_clean"])
    freq_mots = nltk.word_tokenize(all_texte_mois)

    freq_mots = nltk.FreqDist(freq_mots)

    # Faire un top 10 des mots qui reviennent
    freq_mots20 = freq_mots.most_common(n=10)

    # Transformer la fréquence en serie pandas
    serie_graph = pd.Series(dict(freq_mots20)).reset_index()
    serie_graph.rename(columns={"index" : "mot", 0 : "occurences"}, inplace=True)

    # Graph pour les 10 mots qui reviennent
    fig, ax = plt.subplots(figsize=(12,8))

    sns.barplot(data = serie_graph,  x="mot", y="occurences", palette="pastel")
    plt.xticks(rotation=30, ha='right', )
    plt.yticks(range(0, serie_graph["occurences"].max(), 1))
    plt.ylabel(" ")
    plt.xlabel(" ")
    plt.show()
    st.pyplot(fig)


# Donut plotly

def graph_donut_mois(df_fonc, input_annee):
        
        df_fonc = df_fonc[df_fonc["year"] == input_annee]

        df_fonc.rename(columns={"month_str": "Mois", "month" : "Nombre de lignes" }, inplace=True)

        fig = px.pie(df_fonc, names="Mois",  values="Nombre de lignes", hole=0.6, width=800, height=400,
                     category_orders={"Mois": ['Janvier', 'Février', 'Mars', "Mai", "Avril", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]},
                     color_discrete_sequence=px.colors.qualitative.T10)
        fig.update_traces(textinfo='percent')

        fig.update_layout(legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.3,
                        xanchor="center",
                        x=0.5
                        ))

        #fig.show()
        st.plotly_chart(fig, use_container_width=True)


## Viz répartition journée des messages

# Définir des ranges horaires
def range_horaire(heure): 

    if 8 <= heure < 12:
        return "Matin"
    elif 12 <= heure < 18:
        return "Journée"
    else :
        return "Soirée"

def range_horaire_message(df_fonc, input_mois):
    # Definir les lignes du mois
    df_mensuel = df_fonc[df_fonc["month_str"] == input_mois]
    # Parser pour récupérer les dates du mois
    df_mensuel["Timestamp"] = pd.to_datetime(df_mensuel["Timestamp"], format= '%Y-%m-%d %H:%M:%S.%f')
    df_mensuel["hour"] = df_mensuel["Timestamp"].dt.hour
    df_mensuel["date"] = df_mensuel["Timestamp"].dt.date
    # Appliquer la catégorie de range horaires
    df_mensuel["ranges_horaires"] = df_mensuel["hour"].apply(lambda heure : range_horaire(heure))
    # Afficher la date et concat pour un affichage plus clair
    df_mensuel["date_graph"] = pd.to_datetime(df_mensuel["date"], format= '%Y-%m-%d').dt.day
    df_mensuel["date_graph"] = df_mensuel["day_str"].astype(str) + ' ' + df_mensuel["date_graph"].astype(str)

    fig, ax = plt.subplots(figsize=(10,3))
    sns.set_theme(style="whitegrid",)
    sns.countplot(data=df_mensuel, hue="ranges_horaires", x="date_graph",
                    palette="viridis")
    plt.xticks(rotation=25, ha='right')
    plt.ylabel("")
    plt.xlabel("")
    plt.legend(bbox_to_anchor = (0.50, -0.40), ncols=3,) 
    #plt.show()
    st.pyplot(fig)
