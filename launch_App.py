# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:13:31 2023

@author: romai
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


liste_des_vols = [["Aéroport de Paris Charles de Gaulle, Paris, France","Aéroport international de Narita, Tokyo, Japon"],
["Aéroport international Mohammed-V de Casablanca, Casablanca, Maroc","Aéroport international de Gatwick, Londres, Angleterre, Royaume-Uni"],
["Aéroport Léonard de Vinci de Rome-Fiumicino, Rome, Italie","Aéroport international OR Tambo, Johannesbourg, Afrique du sud"],
["Aéroport international Pearson de Toronto, Toronto, ON, Canada","Aéroport international d'Athènes Elefthérios-Venizélos, Athènes, Grèce"],
["Aéroport international de Riga, Riga, Lettonie","Vienna Schwechat International Airport, Vienne, Autriche"],
["Aéroport international du Caire, Le Caire, Egypte","Chhatrapati Shivaji International Airport, Mumbai, Maharashtra, Inde"],
["Aéroport Adolfo-Suárez de Madrid-Barajas, Madrid, Madrid, Espagne","Aéroport international Reina Sofía de Tenerife Sud, Ténérife, Îles Canaries, Espagne"],
["Aéroport international John F. Kennedy, New York, NY, Etats-Unis","Aéroport international de Los Angeles, Los Angeles, CA, Etats-Unis"],
["Aéroport de Paris Charles de Gaulle, Paris, France","Aéroport Kingsford Smith de Sydney, Sydney, Nouvelles Galles du Sud, Australie"]]

# import des données 
data = pd.read_csv("final_dataset.csv")
# data = pd.read_csv("data/final_dataset.csv")

# création de nouvelles colonnes pour manipuler le dataframe
data["day"]=data["Date"].apply(lambda x: int(x.split("/")[0]) )
data["heure"]=data["Heure de départ"].apply(lambda x: int(x[:2]))
data["minute"]=data["Heure de départ"].apply(lambda x: int(x[3:]))

data.sort_values(by=["heure","minute"],inplace=True)


#----------------------------------------------------------
st.title('Plateforme de comparaison des Prix de trajets selon le VPN ')

st.header('Selection des paramètres')

trajet=st.selectbox(label="Sélectionnez votre trajet", options=liste_des_vols)
depart=trajet[0]
arrive=trajet[1]


day_to_filter = st.slider('Sélectionnez votre jours',1, 31, 30)
hours_to_filter = st.slider('Sélectionnez votre heurs de départ',1, 24, 8)

# Filtrer le dataframe selon les paramètres sélectionnés 
df_to_plot=data[(data.day==day_to_filter) & (data["heure"]>hours_to_filter) & (data["Depart"]==depart) &(data["Arrivé"]==arrive)]
# Trier le dataframe par heure de départ croissante 
df_to_plot.sort_values(by=["heure","minute"],inplace=True)

#Afficher la dataset filtré et trié
st.dataframe(data=df_to_plot[['VPN','Prix', 'Temps de vol',
       'Heure de départ', "Heure d'arrivé","Nombre d'escales", "Compagnies"]])
##----------------------------------------------------------------------------------------------------------------
st.subheader("Pour l’ensemble des vols qui ont été filtré.")
st.subheader("Vous pouvez maintenant comparer les différents prix de trajets selon le pays dans lequel votre VPN est positionné.")



hour_selected=st.selectbox(label="Sélectionnez une horaire de départ d’un des trajets disponibles ", options=df_to_plot["Heure de départ"].unique())

data_trajet=data[ (data["Depart"]==depart) &(data["Arrivé"]==arrive) & (data["Heure de départ"]==hour_selected)]
liste_pays=data.VPN.unique()
liste_prix=[]

for p in liste_pays:
    try:
        liste_prix.append(data_trajet[data_trajet.VPN==p]["Prix"].values[0])
    except:
        liste_prix.append(0)

liste_prix_int=[]

for i in liste_prix:
    if i==0:
        liste_prix_int.append(0)
    else:
        liste_prix_int.append(int(i.replace("€","").strip()))



fig=plt.figure(figsize=(10, 6))
plt.plot(liste_pays,liste_prix_int)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.ylabel("Prix du billet d'avion")
plt.xlabel("Pays de localisation du VPN")
st.pyplot(fig)
