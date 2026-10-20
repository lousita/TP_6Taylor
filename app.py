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

FONCTION = {"sinus" = np.sin(x), "cosinus" = np.cosinus(x)
            "exponentiel"= np.exp(x), "log"= np.log(1+x)
            "custom"= custom(x)}

