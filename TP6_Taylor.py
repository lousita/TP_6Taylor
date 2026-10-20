# Eléonore Veyron
# TP6 TAYLOR 

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

#%% 2. Découverte d'autograd

import autograd.numpy as np
from autograd import grad #grad ne s'applique qu'à un scalaire

# Domaine 
X = np.linspace(0,np.pi*2,10)

# %% Dérivée

sin_der = np.vectorize(grad(np.sin))

print(sin_der(X))

# %%

print(sin_der(X)==np.cos(X))

#%% Formule de Taylor 
# Verson 1 : dérivées fournies 

from math import factorial

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
sinus10 = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]
X = np.linspace(-2 * np.pi, 2 * np.pi, 400)

print(X, taylor1(X,sinus10))

import matplotlib
matplotlib.use("TkAgg")
print(matplotlib.get_backend())


import matplotlib.pyplot as plt 

plt.plot(X,taylor1(X,sinus10))
plt.plot(X,np.sin(X))
plt.show()

#%% Version 2 : dérivées calculées avec autograd
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

# exp à l'ordre 2 : 1 + x + x^2/2
assert np.allclose(taylor2(X, np.exp, 2), 1 + X + X**2 / 2)

# sinus au degré 10, à comparer avec np.sin(X)
Y = np.sin(X)
Y2 = taylor2(X, np.sin, 10)

plt.plot(X,Y)
plt.plot(X,Y2)
plt.show()

compteur=0
D= Y[Y-Y2<10**(-3)]

print(len(D)/len(X)*100,"%")

plt.plot(X,np.cos(X))
plt.plot(X,taylor2(X,np.cos,0))
plt.show()

#%% Une fonction personnalisée

def custom(X):
    """retourne 2 * sin(X) + cos(X/4)"""
    return 2*sin(X)+cos(X/4)


