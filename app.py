import streamlit as st
from datetime import date
from PIL import Image
from pandas import read_csv
import pandas as pd
import seaborn as sns
import scipy as sc
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

# --- Configuration de la page ---
st.set_page_config(page_title="Analyse des ventes Beans & Pods", layout="wide")

# --- Menu de navigation et sidebar ---
st.sidebar.title("🔍 Navigation")
menu = st.sidebar.selectbox('Sélectionner une option', ['Accueil', 'Aperçu des données', 'Visualisation','Recommandations'])

# --- Affichage du titre principal ---
st.markdown(
    """
    <div style='text-align:center'>
        <h1> Analyse des Ventes - Beans & Pods</h1>
        <p>Visualisation et exploration des ventes par canal, région et type de produit.</p>
    </div>
    """, unsafe_allow_html=True
)

# --- Chargement des données ---
try:
    # Définition du chemin du fichier
    fichier = 'data/BeansDataSet.csv'
    
    # Lecture du fichier CSV
    data = read_csv(fichier)

    # Affichage des 5 premières lignes
    st.write("Chargement des données avec succes ! Voici un aperçu :")
    st.dataframe(data.head())

except FileNotFoundError:
    st.error("Le fichier est introuvable. Veuillez vérifier le chemin.")
    st.stop()
except Exception as e:
    st.error(f"Une erreur est survenue : {e}")
    st.stop()

# --- Page Accueil ---
if menu == 'Accueil':
    st.subheader("🏠 Accueil")
    st.write("Bienvenue dans l'analyse des ventes Beans & Pods.")
    st.write("Explorez les ventes par canal, par région et par type de produit.")
    
    # Affichage des statistiques de base
    st.subheader("Statistiques générales")
    st.write(data.describe())

    st.subheader("📈 Nombre de ventes par canal")
    figure, ax = plt.subplots()
    data['Channel'].value_counts().plot(kind='bar', color=['green', 'orange'], ax=ax)
    ax.set_xlabel('Canal')
    ax.set_ylabel('Nombre de ventes')
    st.pyplot(figure)

# --- Page Aperçu des données ---
elif menu == 'Aperçu des données':
    st.subheader(" Aperçu des données")
    
    # Affichage des 10 premières lignes
    st.write("Les 10 premières lignes du dataset :")
    st.dataframe(data.head(10))
    
    # Nombre de ventes par région
    st.subheader("🌍 Répartition des ventes par région")
    region_count = data['Region'].value_counts()
    st.write(region_count)

    # Graphique des ventes par région
    st.subheader(" Graphique des ventes par région")
    figure, ax = plt.subplots()
    region_count.plot(kind='bar', color=['blue', 'red', 'green'], ax=ax)
    ax.set_xlabel('Region')
    ax.set_ylabel('Nombre de ventes')
    st.pyplot(figure)

    # Statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

    # Matrice de corrélation
    st.subheader("Matrice de corrélation")
    # Filtrer uniquement les colonnes numériques
    numerical_data = data.select_dtypes(include=['float64', 'int64'])

    # Affichage de la corrélation uniquement sur les colonnes numériques
    st.write(numerical_data.corr())

    
    # --- Section Visualisation ---
elif menu == 'Visualisation':
    st.markdown("<h2 style='text-align: center;'> Visualisation des ventes</h2>", unsafe_allow_html=True)

    # Histogramme des ventes par canal
    st.subheader('Ventes par canal (Store vs Online)')
    fig, ax = plt.subplots()
    data['Channel'].value_counts().plot(kind='bar', color=['blue', 'orange'], ax=ax)
    ax.set_xlabel('Canal')
    ax.set_ylabel('Nombre de ventes')
    st.pyplot(fig)

    # Ventes par région
    st.subheader('Répartition des ventes par région')
    fig, ax = plt.subplots()
    data['Region'].value_counts().plot(kind='bar', color='green', ax=ax)
    ax.set_xlabel('Region')
    ax.set_ylabel('Nombre de ventes')
    st.pyplot(fig)

    # Matrice de corrélation
    st.subheader('Matrice de corrélation')
    numerical_data = data.select_dtypes(include=['float64', 'int64'])
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numerical_data.corr(), cmap='coolwarm', annot=True, fmt='.2f', ax=ax)
    st.pyplot(fig)

# --- Section Recommandations ---
elif menu == 'Recommandations':
    st.markdown("<h2 style='text-align: center;'>Recommandations Marketing</h2>", unsafe_allow_html=True)

    # ✅ Présentation des recommandations
    st.subheader(" **1️⃣ Augmenter la présence en ligne**")
    st.write("""
    -  **Investir dans la publicité ciblée sur les réseaux sociaux** pour booster les ventes en ligne.
    - **Offrir la livraison gratuite** pour les commandes supérieures à un certain montant afin d'augmenter le panier moyen.
    - *Proposer des promotions exclusives* sur le site web pour attirer davantage de clients.
    """)

    st.subheader("🌍 **2️⃣ Renforcer la présence dans la région Sud**")
    st.write("""
    - **Lancer des promotions régionales spécifiques** pour attirer de nouveaux clients.
    - **Proposer des partenariats avec des cafés locaux** pour renforcer la notoriété de la marque.
    - **Envoyer des campagnes d’emailing ciblées** pour booster la notoriété dans la région Sud.
    """)

    st.subheader(" **3️⃣ Capitaliser sur les capsules Espresso et Lungo**")
    st.write("""
    - **Créer des packs promotionnels** (ex. : 5 boîtes + 1 gratuite) pour encourager les ventes en volume.
    - **Mettre en avant ces produits** sur le site web avec des recommandations personnalisées.
    - **Proposer des abonnements capsules** pour fidéliser la clientèle.
    """)

    st.subheader(" **4️⃣ Relancer les ventes de Latté et Cappuccino**")
    st.write("""
    - **Offrir des dégustations gratuites** en magasin pour faire découvrir ces capsules.
    - **Proposer des capsules gratuites** Latté et Cappuccino lors d’achats en ligne pour booster leur popularité.
    -  **Créer des recettes et tutoriels vidéo** sur les réseaux sociaux pour inspirer les clients.
    """)

    st.subheader("**5️⃣ Améliorer la collecte des données**")
    st.write("""
    - **Ajouter des champs d'informations clients** (âge, genre, préférences) pour affiner le ciblage marketing.
    - **Suivre les préférences d’achat par région et par produit** pour mieux segmenter les clients.
    -  **Analyser les avis clients** pour identifier les améliorations possibles.
    """)

    # ✅ Objectifs finaux
    st.markdown("""
    <div style='text-align: center;'>
        <h3>Objectif final : Augmenter les ventes, fidéliser la clientèle et maximiser la rentabilité.</h3>
    </div>
    """, unsafe_allow_html=True)

# --- Page Visualisation ---

else:
    st.subheader(" Visualisations avancées")

    # Histogrammes
    st.subheader(" Histogrammes")
    data.hist(bins=20, figsize=(15, 10))
    st.pyplot(plt.gcf())

    # Histogramme spécifique : Ventes d'Espresso
    st.subheader("Histogramme des ventes d'Espresso")
    figure, ax = plt.subplots()
    ax.hist(data['Espresso'], color='purple')
    ax.set_xlabel('Quantité vendue')
    ax.set_ylabel('Fréquence')
    st.pyplot(figure)

    # Graphe de densité
    st.subheader("Graphe de densité")
    data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False, sharey=False, figsize=(15, 10))
    st.pyplot(plt.gcf())

    # Boîte à moustaches
    st.subheader("Boîte à moustaches")
    data.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False, figsize=(15, 10))
    st.pyplot(plt.gcf())

    # Matrice de corrélation avec Seaborn
    st.subheader("Matrice de corrélation")
    figure, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(data.corr(), cmap='coolwarm', fmt='.2f', annot=True, ax=ax)
    st.pyplot(figure)

    # Scatter Matrix
    st.subheader("Scatter Matrix")
    scatter_matrix(data, figsize=(15, 10), diagonal='kde', color='green')
    st.pyplot(plt.gcf())

    # Pairplot avec Seaborn
    st.subheader("Graphique Pairplot")
    sns.pairplot(data, hue='Channel', palette='husl')
    st.pyplot(plt.gcf())



st.markdown("---")
st.write("**Projet réalisé par FOGHA TADJOU AISSA REINE - Hiver 2025**")
