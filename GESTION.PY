'''
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_LOGICIEL_DE_CALCUL
from biblio.calcul_module import Ui_calcul_module
from biblio.contenu_case1 import Ui_fenetre_case1
from biblio.denture_droiteEX import Ui_denture_droite_ch1
from biblio.denture_droiteIN import Ui_denture_droite_ch11
from biblio.denture_droite_hE import Ui_denture_droite_hE_ch1
from biblio.denture_droite_hI import Ui_denture_droite_hI_ch1
from biblio.fenetre_2 import Ui_different_type_engrenage
# RESTE DES MODULES

import sys

def retour():
    LOGICIEL_DE_CALCUL.close() 

def retour_1():
    different_type_engrenage.close()  # Ferme la fenêtre lorsque le bouton "retour" est cliqué 

def retour_2():
	fenetre_case1.close()

def retour_3():
	denture_droite_ch1.close()

def retour_4():
	denture_droite_hE_ch1.close()

def retour_5():
	denture_droite_ch11.close()

def retour_6():
	denture_droite_hI_ch1.close()

def retour_7():
	calcul_module.close()
# RESTE DES FONCTIONS POUR LA FERMETURE DES FENETRES

def afficherfenetre2(): # FONCTION POUR APPELER LA FENETRE ET L'AFFICHER
	different_type_engrenage.setMinimumSize(1080, 720)  
	different_type_engrenage.showMaximized()  

def affichercase1():
	fenetre_case1.setMinimumSize(1080, 720)
	fenetre_case1.showMaximized()
		
def afficherdenture_droite_exterieur():
	denture_droite_ch1.setMinimumSize(1080, 720)
	denture_droite_ch1.showMaximized()

def afficherdenture_droite_interieur():
	denture_droite_ch11.setMinimumSize(1080, 720)
	denture_droite_ch11.showMaximized()

def afficferdenture_droite_hE():
	denture_droite_hE_ch1.setMinimumSize(1080, 720)
	denture_droite_hE_ch1.showMaximized()	

def afficferdenture_droite_hI():
	denture_droite_hI_ch1.setMinimumSize(1080, 720)
	denture_droite_hI_ch1.showMaximized()

def affichermodule():
	calcul_module.setMinimumSize(1080, 720)
	calcul_module.showMaximized()
# RESTE DES FONCTIONS POUR APPELER LES FENETRES ET LEUR AFFICHER

app = QtWidgets.QApplication(sys.argv)
LOGICIEL_DE_CALCUL = QtWidgets.QMainWindow()
ui = Ui_LOGICIEL_DE_CALCUL()
ui.setupUi(LOGICIEL_DE_CALCUL)
ui.pushButton_2.clicked.connect(retour)

# creation de la fenetre_2
different_type_engrenage = QtWidgets.QWidget()
uifenetre_2 = Ui_different_type_engrenage()
uifenetre_2.setupUi(different_type_engrenage)
uifenetre_2.bouton_retour_ch11.clicked.connect(retour_1)
########### SOUS FENETRES DU 1ER CHAPITRE ###########

# creation de la fenetre denture droite exterieur
denture_droite_ch1 = QtWidgets.QWidget()
uidenture_droite = Ui_denture_droite_ch1()
uidenture_droite.setupUi(denture_droite_ch1)
uidenture_droite.pushButton_2.clicked.connect(retour_3)

# creation de la fenetre denture droite interieur
denture_droite_ch11 = QtWidgets.QWidget()
uidenture_droite1 = Ui_denture_droite_ch11()
uidenture_droite1.setupUi(denture_droite_ch11)
uidenture_droite1.pushButton_2.clicked.connect(retour_5)

# creation de la fenetre denture droite helicoidale exterieur
denture_droite_hE_ch1 = QtWidgets.QWidget()
uidenture_droite_hE = Ui_denture_droite_hE_ch1()
uidenture_droite_hE.setupUi(denture_droite_hE_ch1)
uidenture_droite_hE.pushButton_2.clicked.connect(retour_4)

# creation de la fenetre denture droite helicoidale interieur
denture_droite_hI_ch1 = QtWidgets.QWidget()
uidenture_droite_hI = Ui_denture_droite_hI_ch1()
uidenture_droite_hI.setupUi(denture_droite_hI_ch1)
uidenture_droite_hI.pushButton_2.clicked.connect(retour_6)

# creation de la fenetre case1
fenetre_case1 = QtWidgets.QWidget()
uicase1 = Ui_fenetre_case1()
uicase1.setupUi(fenetre_case1)
uicase1.bouton_retour_ch12.clicked.connect(retour_2)

# creation de la fenetre calcul du module
calcul_module = QtWidgets.QWidget()
uimodule = Ui_calcul_module()
uimodule.setupUi(calcul_module)
uimodule.bouton_retour_ch13.clicked.connect(retour_7)

#RESTE CODE

LOGICIEL_DE_CALCUL.setMinimumSize(1080, 720)  
LOGICIEL_DE_CALCUL.show()
LOGICIEL_DE_CALCUL.showMaximized()  

ui.pushButton.clicked.connect(afficherfenetre2)

uifenetre_2.bouton_case1.clicked.connect(affichercase1)
uicase1.bouton_case11.clicked.connect(afficherdenture_droite_exterieur)
uicase1.bouton_case13.clicked.connect(afficherdenture_droite_interieur)
uicase1.bouton_case15.clicked.connect(affichermodule)
uicase1.bouton_case12.clicked.connect(afficferdenture_droite_hE)
uicase1.bouton_case14.clicked.connect(afficferdenture_droite_hI)

#RESTE CODE

sys.exit(app.exec_())


#########################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_LOGICIEL_DE_CALCUL
from biblio.calcul_module import Ui_calcul_module
from biblio.contenu_case1 import Ui_fenetre_case1
from biblio.denture_droiteEX import Ui_denture_droite_ch1
from biblio.denture_droiteIN import Ui_denture_droite_ch11
from biblio.denture_droite_hE import Ui_denture_droite_hE_ch1
from biblio.denture_droite_hI import Ui_denture_droite_hI_ch1
from biblio.fenetre_2 import Ui_different_type_engrenage

import sys

class MainWindowStack(QtWidgets.QStackedWidget):
    def __init__(self):
        super().__init__()
        self.window_stack = []

    def push_window(self, window):
        if self.window_stack:
            current_window = self.window_stack[-1]
            current_window.hide()
        self.window_stack.append(window)
        self.addWidget(window)
        self.setCurrentWidget(window)

    def pop_window(self):
        if self.window_stack:
            last_window = self.window_stack.pop()
            self.removeWidget(last_window)
            last_window.hide()
            if self.window_stack:
                previous_window = self.window_stack[-1]
                previous_window.show()
                self.setCurrentWidget(previous_window)

app = QtWidgets.QApplication(sys.argv)

stacked_windows = MainWindowStack()

LOGICIEL_DE_CALCUL = QtWidgets.QMainWindow()
ui = Ui_LOGICIEL_DE_CALCUL()
ui.setupUi(LOGICIEL_DE_CALCUL)
ui.pushButton_2.clicked.connect(lambda: stacked_windows.pop_window())

different_type_engrenage = QtWidgets.QWidget()
uifenetre_2 = Ui_different_type_engrenage()
uifenetre_2.setupUi(different_type_engrenage)
uifenetre_2.bouton_retour_ch11.clicked.connect(lambda: stacked_windows.pop_window())

# Ajouter d'autres fenêtres et leurs connexions ici...

stacked_windows.push_window(LOGICIEL_DE_CALCUL)

sys.exit(app.exec_())
'''
import math
#################################################################
Z1 = int(input("Z1 = "))
X1 = float(input("X1 = "))
z = Z1
z = int(z)
gao = 2.90085 / z
eo = 0.95 - X1
so = 0.5 * math.pi + 0.7279405 * X1 
ala = math.cos(math.pi / 9) * z / (2 + 2 * X1 + z)
ala = math.atan(math.sqrt(1 - ala * ala) / ala)
als = so / z + 0.01490438 - math.sin(ala) / math.cos(ala) + ala
alf = ala - als
sao = (z + 2 + 2 * X1) * als
ph3 = math.pi / 6 + gao
ph3 = (0.5 + eo / z) * math.sin(ph3) / math.cos(ph3)
ph3 = -ph3 + math.sqrt(ph3 ** 2 + 2 * eo / z)
ph2 = math.sin(gao + ph3)
ph1 = math.cos(gao + ph3)
sf = (z - 2 * eo) * ph2 - ph3 * z * ph1 - 0.519615
ds = (z - 2 * eo) * ph1 + ph3 * z * ph2 - 0.3
hf = 0.5 * (z + 2 + 2 * X1 - ds)
fo = hf - 0.5 * sao * math.sin(alf) / math.cos(alf)
YFa1 = 6.38507 * fo * math.cos(alf) / (sf ** 2)
print("YFa1 =",YFa1 )
