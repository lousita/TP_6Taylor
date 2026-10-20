# Eléonore Veyron
# TP6 TAYLOR - VERSION STREAMLIT 








#Remarque :







 
#  il y a deux fichier.py app pour ce qui est lié 
#à streamlit
# et l'autre essai pour tout ce qui est lié à python !
#





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
    largeur = st.slider("largeur", 2.0, 20.0, 12.6)

# 4.4 Calculs et tracé

#Rappel des fonctions 
def taylor1(X, derivatives):
    """
    X : le domaine (sous-entendu X[0] < 0 et X[-1] > 0)
    derivatives : derivatives[n] = f^(n)(0), dérivée n-ième de f en 0

    Retourne Y, l'approximation de Taylor sur X pour une fonction
    qui aurait ces dérivées en 0.
    """
    Y=np.zeros_like(X)
    for i,d in enumerate(derivatives):
        Y = Y + d*X**i/factorial(i)
    return Y

def taylor2(X, f, n):
    """
    X : le domaine
    f : la fonction (sur scalaire)
    n : le degré

    Retourne Y, l'approximation de Taylor de f à l'ordre n sur X.
    """
    derivatives = []
    g = f
    for _ in range(n+1):
        derivatives.append(g(0.0))
        g= grad(g)
    return taylor1(X,derivatives)


f = FONCTION[nom_fonction]
X = np.linspace(-largeur/2,largeur/2,400)
Y=f(X)
Y2=taylor2(X,f,n)

fig,ax=plt.subplots()
ax.plot(X,Y)
ax.plot(X,Y2)
st.pyplot(fig)
