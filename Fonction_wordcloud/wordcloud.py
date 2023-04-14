from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


# Constante masque 
emplacement_icone = "discord_remplir.jpg"
mask = np.array(Image.open(emplacement_icone))
mask[mask == 255] = 255


# Fonction qui créra les wordclouds # colormap = 'bone', "Spectral"
def wordcloud_discord(data, title, mask=None):
    cloud = WordCloud(scale=3,
                        max_words=100,
                        colormap='tab10',
                        mask=mask,
                        #repeat=True,
                        background_color='white',
                        collocations=True,
                        contour_color='royalblue',
                        normalize_plurals=True,
                        random_state=42,
                        width = 350, height = 350,
                        contour_width=10).generate_from_text(data)
    plt.figure(figsize=(15,7))
    plt.imshow(cloud, alpha = 1 , interpolation='nearest')
    plt.axis('off')
    plt.title(title)
    st.pyplot()


# Pour les wordclouds mensuels

# Boucler le texte par mois
def texte_mensuel(dataframe, input_annee, mois):
    texte_mois = dataframe[(dataframe["year"] == input_annee) & (dataframe["month_str"] == mois)]
    texte_mois = " ".join(texte_mois["texte_clean"])
    return texte_mois

# Wordcloud annuel
def wordcloud_mensuel(dataframe, input_anne, mois):
    texte_mois = texte_mensuel(dataframe, input_anne, mois)
    title = mois
    try :
        wordcloud_discord(texte_mois, mois, mask=mask)
    except ValueError:
        st.write("Pas de messages échangé ce mois-ci")

# Pour les wordclouds annuels

# Boucler le texte par année
def texte_annuel(dataframe, input_annee):
    texte_an = dataframe[dataframe["year"] == input_annee]
    texte_an = " ".join(texte_an["texte_clean"])
    return texte_an

# Wordcloud annuel
def wordcloud_annuel(dataframe, input_anne):
    texte_an = texte_annuel(dataframe, input_anne)
    title = "Année {}".format(texte_an)
    wordcloud_discord(texte_an, input_anne, mask=mask)


# Pour le word cloud de présentation (tout le df)

# Renvoyer le texte de tout le df
def wordcloud_all_texte(dataframe):
    texte_all = " ".join(dataframe["texte_clean"])
    return texte_all
# Wordcloud sur tout le df
def wordcloud_all_df(dataframe):
    texte_all = wordcloud_all_texte(dataframe)
    title = "Aperçu des mots réccurents"
    wordcloud_discord(texte_all, title, mask=mask)


### Récupérer fréquence 

## Pour tout le df
# Récupérer le/les mots qui reviennent le plus en terme de fréquence
def wordcloud_frequence(data):
    cloud = WordCloud(scale=3,
                        max_words=100,
                        colormap='tab10',
                        repeat=True,
                        background_color='white',
                        collocations=True,
                        contour_color='royalblue',
                        normalize_plurals=True,
                        random_state=42,
                        width = 400, height = 400,
                        contour_width=10).generate_from_text(data)
    freq = cloud.words_
    freq = list(freq)[0]
    return freq

# Renvoyer le texte de tout le df
def wordcloud_all_freq(dataframe):
    texte_all = " ".join(dataframe["texte_clean"])
    return wordcloud_frequence(texte_all)


def wordcloud_all_freq_mois(dataframe, input_mois):
    df_mois_fonc = dataframe[dataframe["month_str"] == input_mois]
    texte_all = " ".join(df_mois_fonc["texte_clean"])
    return wordcloud_frequence(texte_all)

# Récupérer le mot d'une année 
def wordcloud_mot_annee(dataframe, input_annee):
    df_mois_fonc = dataframe[dataframe["year"] == input_annee]
    texte_all = " ".join(df_mois_fonc["texte_clean"])
    return wordcloud_frequence(texte_all)

# Mini Masque
emplacement_icone2 = "mini_wc.jpg"
mini_mask = np.array(Image.open(emplacement_icone2))
mini_mask[mini_mask == 255] = 255

# Wordcloud des 20 mots récurrents

def word_cloud_20_freq(data, mask=None):
    cloud = WordCloud(scale=3,
                        max_words=10,
                        colormap='tab20',
                        mask=mask,
                        #repeat=True,
                        background_color='white',
                        collocations=True,
                        contour_color='royalblue',
                        normalize_plurals=True,
                        random_state=42,
                        width = 80, height = 20,
                        max_font_size = 10,
                        contour_width=10).generate_from_text(data)
    plt.figure(figsize=(5,4))
    plt.imshow(cloud, alpha = 1 , interpolation='nearest')
    plt.axis('off')
    st.pyplot()

# Boucler le texte par mois
def mini_wordcloud_mois(dataframe, mois):
    texte_mois = dataframe[dataframe["month_str"] == mois]
    texte_mois = " ".join(texte_mois["texte_clean"])
    word_cloud_20_freq(texte_mois, )

