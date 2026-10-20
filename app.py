# Eléonore Veyron
# TP6 TAYLOR - VERSION STREAMLIT 

import streamlit as st


#%% Première application


st.title("Approximation de Taylor")
st.header("Première approximation") #sous-titre
st.write("Bienvenue dans votre outil de visualisation.")

#ecrire dans le terminal 
# streamlit run opp.py
#avec opp le nom du fichier qu'on veut ouvrier avec streamlit

#%% Afficher une formule 
st.latex(r'''P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} \, x^k''')

#%% Modèle d'exécution

valeur = st.slider("Choisissez une valeur", 0, 10)
st.write("Vous avez choisi :", valeur)

#%% 4 L'application widgets et graphique

import streamlit as st
import autograd.numpy as np
from autograd import grad
from math import factorial
import matplotlib.pyplot as plt


def custom(X):
    """retourne 2 * sin(X) + cos(X/4)"""
    return 2*np.sin(X)+np.cos(X/4)



FONCTION = {"sinus" : np.sin, "cosinus" : np.cos,
            "exponentiel" : np.exp, "log" : lambda x:np.log(1+x),
            "custom" : custom}

#4.3 Widgets 

with st.sidebar:
    nom_fonction= st.selectbox("Fonction", list(FONCTION))
    n = st.slider("n", 0, 10)
    intervalle = st.slider("intervalle", 2.0, 20.0, 12.6)

# 4.4 Calculs et tracé
f = FONCTIONS["nom"]