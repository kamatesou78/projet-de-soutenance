import numpy as np
'''import numpy as np permet  d'importer la bibliothèque NumPy, qui est largement utilisée 
pour effectuer des calculs numériques en Python
'''

import matplotlib.pyplot as plt
'''
import matplotlib.pyplot as plt permet d'importer la bibliothèque Matplotlib, qui est utilisée 
pour tracer des graphiques en Python. 
'''
# Permet de creer un tableau numpy pour les coordonnées des points x et y
x_points = np.array([10,20, 40, 60, 80, 100, 120, 160, 180, 200])
y_points = np.array([1.66, 1.5, 1.34, 1.25, 1.17, 1.13, 1.09, 1.03, 1.01, 1 ])

# Permet d'Ajuster une équation polynomiale aux points x et y
coefficients = np.polyfit(x_points, y_points, deg=len(x_points) - 1)

# Permet d'afficher les coefficients du polynôme a l'aide de print
print("Coefficients du polynôme :", coefficients)

# Permet d'Afficher l'équation polynomiale a l'aide de print
equation = np.poly1d(coefficients)
print("Équation polynomiale :\n", equation)

# Permet de générer 100 valeurs de x pour le tracé de la courbe
x_curve = np.linspace(min(x_points), max(x_points), 100)
y_curve = equation(x_curve)

# Tracer la courbe
# Permet de tracer les points de donnees sur la graqhique
plt.scatter(x_points, y_points, label='Points') 
# Cette ligne trace la courbe interpolée à partir des valeurs x et y
plt.plot(x_curve, y_curve, label='Courbe interpolée', color='red')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


'''
##########################################################

from PyQt5 import QtCore, QtGui, QtWidgets

from menu import Ui_LOGICIEL_DE_CALCUL

from biblio.calcul_module import Ui_calcul_module

from biblio.contenu_case1 import Ui_fenetre_case1

from biblio.denture_droiteEX import Ui_denture_droite_ch1

from biblio.denture_droiteIN import Ui_denture_droite_ch11

from biblio.denture_droite_hE import Ui_denture_droite_hE_ch1

from biblio.denture_droite_hI import Ui_denture_droite_hI_ch1

from biblio.fenetre_2 import Ui_different_type_engrenage

from biblio.Engrenages_Deportees import 
Ui_ENGRENAGES_DEPORTEES

from biblio.Engrenages_deportes_avec_variation_entraxe 
import Ui_VARIATION_ENTRAXE

from biblio.Engrenages_deportes_sans_variation_entraxe
import Ui_SANS_VARIATION_ENTRAXE

from biblio.Deports_avec_variation_entraxe 
import Ui_DEPORTS_AVEC_VARIATION_ENTRAXE

from biblio.Deports_sans_variation_entraxe 
import Ui_DEPORTS_SANS_VARIATION_ENTRAXE

from biblio.Methode_ISO_Sans_Variation_Entraxe 
import Ui_METHODE_ISO_SANS_VARIATION_ENTRAXE 

from biblio.Methode_MAAG_TASCHENBUCH_Sans_Variation_Entraxe 
import Ui_METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE 

from biblio.Methode_W_RICHTER_Sans_Variation_Entraxe
import Ui_METHODE_WRICHTER_SANS_VARIATION_ENTRAXE

from biblio.Methode_ISO_denture_droite 
import Ui_METHODE_ISO_D_DROITE

from biblio.Methode_METHODE_ISO_denture_helicoidale 
import Ui_METHODE_ISO_D_HELICOIDALE

from biblio.Methode_W_RICHTER_denture_droite 
import Ui_METHODE_W_RICHTER_D_DROITE

from biblio.Methode_METHODE_DE_W_RICHTER_denture_helicoidale 
import Ui_METHODE_DE_W_RICHTER_D_HELICOIDALE

from biblio.Methode_MAAG_TASCHENBUCH_denture_droite 
import Ui_METHODE_MAAG_TASCHENBUCH_D_DROITE

from biblio.Methode_MAAG_TASCHENBUCH_denture_helicoidale 
import Ui_METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE

from biblio.denture_droite_EXTERIEUR_DEPORTE 
import Ui_Denture_droite_deporteE

from biblio.denture_droite_INTERIEUR_DEPORTE 
import Ui_Denture_droite_deporteIN

from biblio.denture_droiteH_deporteIN 
import Ui_Denture_droiteH_deporteIN

from biblio.denture_droiteH_deporteEX 
import Ui_Denture_droiteH_deporteE

from biblio.denture_droite_EXTERIEUR_DEPORTE_VARIATION_ANT_NON_IMPOSE 
import Ui_Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE

from biblio.denture_droite_INTERIEUR_DEPORTE_VARIATION_ANT_NON_IMPOSE 
import Ui_Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE

from biblio.denture_droiteH_deporteEX_VARIATION_ENTRAXE_NON_IMPOSE 
import Ui_Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE 

from biblio.denture_droiteH_deporteIN_VARIATION_ENTRAXE_NON_IMPOSE 
import Ui_Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE 

from biblio.DENTURE_DROITE_EXTERIEUR_DEPORTE_VARIATION_ENT_IMPOSE 
import Ui_Denture_droite_deporteEX_VARIATION_ENT_IMPOSE 

from biblio.DENTURE_DROITE_INTERIEUR_DEPORTE_VARIATION_ENT_IMPOSE 
import Ui_Denture_droite_deporteIN_VARIATION_ENT_IMPOSE

from biblio.DENTURE_HELICOIDALE_deporteEXTERIEUR_VARIATION_ENTRAXE_IMPOSE 
import Ui_Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE

from biblio.DENTURE_HELICOIDALE_deporteINTERIEUR_VARIATION_ENTRAXE_IMPOSE 
import Ui_Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE 

from biblio.ENGRENAGE_CONCOURANTE import 
Ui_ENGRENAGE_CONCOURANTE

from biblio.ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE 
import Ui_ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE

from biblio.ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE 
import Ui_ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE

from biblio.ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE 
import Ui_ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE

from biblio.ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE 
import Ui_ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE

from biblio.ROUE_VIS_SANS_FIN 
import Ui_ROUE_VIS_SANS_FIN

from biblio.RESISTANCE_EFFORTS 
import Ui_RESISTANCE_EFFORT

from biblio.LES_EFFORTS_SUR_DENTS 
import Ui_LES_EFFORTS_SUR_DENTS 

from biblio.LES_EFFORTS_DENTURE_DROITE_PARALLELE 
import Ui_DENTURE_DROITE_PARALLELE 

from biblio.LES_EFFORTS_DENTURE_HELICOIDALE_PARALLELE 
import Ui_DENTURE_HELICOIDALE_PARALLELE 

from biblio.LES_EFFORTS_DENTURE_CONIQUE 
import Ui_DENTURE_CONIQUE 

from biblio.LES_EFFORTS_ROUE_ET_VIS 
import Ui_LES_EFFORTS_ROUE_ET_VIS 

from biblio.CALCUL_DE_RESISTANCE_DES_DENTS_DES_ENGRENAGES_PARALLELES 
import Ui_RESISTANCE_ENGRENAGE_PARALLELE 

from biblio.RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE 
import Ui_RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE 

from biblio.RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE 
import Ui_RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE 

from biblio.RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE 
import Ui_RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE 

from biblio.RESISTANCE_HELICOI_ENTRAXE_IMPOSE 
import Ui_RESISTANCE_HELICOI_ENTRAXE_IMPOSE 
'''



