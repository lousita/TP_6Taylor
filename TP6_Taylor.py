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

def sin_der(X):
    return np.vectorize(grad(np.sin(X)))

print(sin_der(X))
Y=[0]
print(sin_der(Y))

# %%

der = sin_der(X)
diff = der[der != np.vectorize(np.cos(X))]
if diff == []:
    print("On a bien égalité entre sin_der(X) et np.cos(X)")

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
    Y=[]
    for k in range(len(X)):
        Y.append(sum([derivatives[i] / math.factorial(i) * X[k]**i for i in range(len(derivatives))]))
    return Y
