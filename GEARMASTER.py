from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_LOGICIEL_DE_CALCUL
from biblio.calcul_module import Ui_calcul_module
from biblio.contenu_case1 import Ui_fenetre_case1
from biblio.denture_droiteEX import Ui_denture_droite_ch1
from biblio.denture_droiteIN import Ui_denture_droite_ch11
from biblio.denture_droite_hE import Ui_denture_droite_hE_ch1
from biblio.denture_droite_hI import Ui_denture_droite_hI_ch1
from biblio.fenetre_2 import Ui_different_type_engrenage
from biblio.Engrenages_Deportees import Ui_ENGRENAGES_DEPORTEES
from biblio.Engrenages_deportes_avec_variation_entraxe import Ui_VARIATION_ENTRAXE
from biblio.Engrenages_deportes_sans_variation_entraxe import Ui_SANS_VARIATION_ENTRAXE
from biblio.Deports_avec_variation_entraxe import Ui_DEPORTS_AVEC_VARIATION_ENTRAXE
from biblio.Deports_sans_variation_entraxe import Ui_DEPORTS_SANS_VARIATION_ENTRAXE
from biblio.Methode_ISO_Sans_Variation_Entraxe import Ui_METHODE_ISO_SANS_VARIATION_ENTRAXE 
from biblio.Methode_MAAG_TASCHENBUCH_Sans_Variation_Entraxe import Ui_METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE 
from biblio.Methode_W_RICHTER_Sans_Variation_Entraxe import Ui_METHODE_WRICHTER_SANS_VARIATION_ENTRAXE
from biblio.Methode_ISO_denture_droite import Ui_METHODE_ISO_D_DROITE
from biblio.Methode_METHODE_ISO_denture_helicoidale import Ui_METHODE_ISO_D_HELICOIDALE
from biblio.Methode_W_RICHTER_denture_droite import Ui_METHODE_W_RICHTER_D_DROITE
from biblio.Methode_METHODE_DE_W_RICHTER_denture_helicoidale import Ui_METHODE_DE_W_RICHTER_D_HELICOIDALE
from biblio.Methode_MAAG_TASCHENBUCH_denture_droite import Ui_METHODE_MAAG_TASCHENBUCH_D_DROITE
from biblio.Methode_MAAG_TASCHENBUCH_denture_helicoidale import Ui_METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE
from biblio.denture_droite_EXTERIEUR_DEPORTE import Ui_Denture_droite_deporteE #sans variation d'entraxe
from biblio.denture_droite_INTERIEUR_DEPORTE import Ui_Denture_droite_deporteIN #sans variation d'entraxe
from biblio.denture_droiteH_deporteIN import Ui_Denture_droiteH_deporteIN #sans variation d'entraxe
from biblio.denture_droiteH_deporteEX import Ui_Denture_droiteH_deporteE #sans variation d'entraxe
from biblio.denture_droite_EXTERIEUR_DEPORTE_VARIATION_ANT_NON_IMPOSE import Ui_Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE #avec variation d'entraxe(non impose)
from biblio.denture_droite_INTERIEUR_DEPORTE_VARIATION_ANT_NON_IMPOSE import Ui_Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE #avec variation d'entraxe(non impose)
from biblio.denture_droiteH_deporteEX_VARIATION_ENTRAXE_NON_IMPOSE import Ui_Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE #avec variation d'entraxe(non impose)
from biblio.denture_droiteH_deporteIN_VARIATION_ENTRAXE_NON_IMPOSE import Ui_Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE #avec variation d'entraxe(non impose)
from biblio.DENTURE_DROITE_EXTERIEUR_DEPORTE_VARIATION_ENT_IMPOSE import Ui_Denture_droite_deporteEX_VARIATION_ENT_IMPOSE #avec variation d'entraxe(impose)
from biblio.DENTURE_DROITE_INTERIEUR_DEPORTE_VARIATION_ENT_IMPOSE import Ui_Denture_droite_deporteIN_VARIATION_ENT_IMPOSE #avec variation d'entraxe(impose)
from biblio.DENTURE_HELICOIDALE_deporteEXTERIEUR_VARIATION_ENTRAXE_IMPOSE import Ui_Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE #avec variation d'entraxe(impose)
from biblio.DENTURE_HELICOIDALE_deporteINTERIEUR_VARIATION_ENTRAXE_IMPOSE import Ui_Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE #avec variation d'entraxe(impose)
from biblio.ENGRENAGE_CONCOURANTE import Ui_ENGRENAGE_CONCOURANTE
from biblio.ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE import Ui_ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE
from biblio.ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE import Ui_ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE
from biblio.ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE import Ui_ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE
from biblio.ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE import Ui_ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE
from biblio.ROUE_VIS_SANS_FIN import Ui_ROUE_VIS_SANS_FIN
from biblio.RESISTANCE_EFFORTS import Ui_RESISTANCE_EFFORT # fenetre pour les calculs des effort et des resistances
from biblio.LES_EFFORTS_SUR_DENTS import Ui_LES_EFFORTS_SUR_DENTS # fenetre pour la selection d'un type d'engrenage afin de calculer les efforts sur les dents
from biblio.LES_EFFORTS_DENTURE_DROITE_PARALLELE import Ui_DENTURE_DROITE_PARALLELE # fenetre pour le calcul des efforts_engrenages droit a denture droite
from biblio.LES_EFFORTS_DENTURE_HELICOIDALE_PARALLELE import Ui_DENTURE_HELICOIDALE_PARALLELE # fenetre pour le calcul des efforts_engrenages droit a denture helicoidale
from biblio.LES_EFFORTS_DENTURE_CONIQUE import Ui_DENTURE_CONIQUE # fenetre pour le calcul des efforts_engrenages conique
from biblio.LES_EFFORTS_ROUE_ET_VIS import Ui_LES_EFFORTS_ROUE_ET_VIS # fenetre pour le calcul des efforts Roue_Vis
from biblio.CALCUL_DE_RESISTANCE_DES_DENTS_DES_ENGRENAGES_PARALLELES import Ui_RESISTANCE_ENGRENAGE_PARALLELE # fenetre pour le choix d'un type d'engrenage parallele afin de calculer la resistance
from biblio.RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE import Ui_RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE # Resistance_denture_droite_sans_imposer_entraxe
from biblio.RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE import Ui_RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE # Resistance_denture_droite_avec_entraxe_imposer
from biblio.RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE import Ui_RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE # Resistance_denture_helicoidale_sans_imposer_entraxe
from biblio.RESISTANCE_HELICOI_ENTRAXE_IMPOSE import Ui_RESISTANCE_HELICOI_ENTRAXE_IMPOSE # Resistance_denture_helicoidale_avec_entraxe_imposer


import sys

# Creation des boutons retours
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

def retour_8():
	ENGRENAGES_DEPORTEES.close()

def retour_9():
	DEPORTS_SANS_VARIATION_ENTRAXE.close()

def retour_10():
	DEPORTS_AVEC_VARIATION_ENTRAXE.close()

def retour_11():
	SANS_VARIATION_ENTRAXE.close()

def retour_12():
	VARIATION_ENTRAXE.close()

def retour_13():
	METHODE_ISO_SANS_VARIATION_ENTRAXE.close()

def retour_14():
	METHODE_WRICHTER_SANS_VARIATION_ENTRAXE.close()

def retour_15():
	METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE.close()

def retour_16():
	METHODE_ISO_D_DROITE.close()

def retour_17():
	METHODE_W_RICHTER_D_DROITE.close()

def retour_18():
	METHODE_MAAG_TASCHENBUCH_D_DROITE.close()

def retour_19():
	METHODE_ISO_D_HELICOIDALE.close()

def retour_20():
	METHODE_DE_W_RICHTER_D_HELICOIDALE.close()

def retour_21():
	METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE.close()

def retour_22():
	Denture_droite_deporteE.close()

def retour_23():
	Denture_droite_deporteIN.close()

def retour_24():
	Denture_droiteH_deporteIN.close()

def retour_25():
	Denture_droiteH_deporteE.close()

def retour_26():
	Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE.close()

def retour_27():
	Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE.close()	

def retour_28():
	Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE.close()

def retour_29():
	Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE.close()

def retour_30():
	Denture_droite_deporteEX_VARIATION_ENT_IMPOSE.close()	

def retour_31():
	Denture_droite_deporteIN_VARIATION_ENT_IMPOSE.close()

def retour_32():
	Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE.close()

def retour_33():
	Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE.close()	

def retour_34():
	ENGRENAGE_CONCOURANTE.close()

def retour_35():
	ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE.close()

def retour_36():
	ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE.close()

def retour_37():
	ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE.close()

def retour_38():
	ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE.close()

def retour_39():
	ROUE_VIS_SANS_FIN.close()

def retour_40():
	RESISTANCE_EFFORT.close()

def retour_41():
	LES_EFFORTS_SUR_DENTS.close()

def retour_42():
	DENTURE_DROITE_PARALLELE.close()

def retour_43():
	DENTURE_HELICOIDALE_PARALLELE.close()

def retour_44():
	DENTURE_CONIQUE.close()

def retour_45():
	LES_EFFORTS_ROUE_ET_VIS.close()

def retour_46():
	RESISTANCE_ENGRENAGE_PARALLELE.close()

def retour_47():
	RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE.close()

def retour_48():
	RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE.close()

def retour_49():
	RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE.close()

def retour_50():
	RESISTANCE_HELICOI_ENTRAXE_IMPOSE.close()
# FIN Bouton retour

def premier_fenetre():
	LOGICIEL_DE_CALCUL.setMinimumSize(1080, 720)  # Définit la taille minimale de la fenêtre
	LOGICIEL_DE_CALCUL.show()
	LOGICIEL_DE_CALCUL.showMaximized()
	different_type_engrenage.hide()  # Maximise la fenêtre pour qu'elle occupe tout l'écran

#FENETRE 2
def afficherfenetre2():
	different_type_engrenage.setMinimumSize(1080, 720)  # permet de définir la taille minimale de la fenêtre
	different_type_engrenage.showMaximized()
	LOGICIEL_DE_CALCUL.hide()
	  # permet de maximiser la fenêtre pour qu'elle occupe tout l'écran

# DEBUT CHAPITRE 1

def affichercase1():
	fenetre_case1.setMinimumSize(1080, 720)
	fenetre_case1.showMaximized()
	different_type_engrenage.hide()
		

def afficherdenture_droite_exterieur():
	denture_droite_ch1.setMinimumSize(1080, 720)
	denture_droite_ch1.showMaximized()
	#denture_droite_ch1.show()

def afficherdenture_droite_interieur():
	denture_droite_ch11.setMinimumSize(1080, 720)
	denture_droite_ch11.showMaximized()
	#denture_droite_ch11.show()

def afficferdenture_droite_hE():
	denture_droite_hE_ch1.setMinimumSize(1080, 720)
	denture_droite_hE_ch1.showMaximized()
	#denture_droite_hE_ch1.show()	


def afficferdenture_droite_hI():
	denture_droite_hI_ch1.setMinimumSize(1080, 720)
	denture_droite_hI_ch1.showMaximized()
	#denture_droite_hI_ch1.show()

def affichermodule():
	calcul_module.setMinimumSize(1080, 720)
	calcul_module.showMaximized()
	#calcul_module.show()
# FIN CHAPITRE 1

# DEBUT CHAPITRE 2

def afficher_Engrenages_Deportees():
	ENGRENAGES_DEPORTEES.setMinimumSize(1080, 720)
	ENGRENAGES_DEPORTEES.showMaximized()
	#ENGRENAGES_DEPORTEES.show()

def afficher_DEPORTS_SANS_VARIATION_ENTRAXE():
	DEPORTS_SANS_VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	DEPORTS_SANS_VARIATION_ENTRAXE.showMaximized()
	#DEPORTS_SANS_VARIATION_ENTRAXE.show()


def afficher_DEPORTS_AVEC_VARIATION_ENTRAXE():
	DEPORTS_AVEC_VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	DEPORTS_AVEC_VARIATION_ENTRAXE.showMaximized()
	#DEPORTS_AVEC_VARIATION_ENTRAXE.show()


def afficher_SANS_VARIATION_ENTRAXE():
	SANS_VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	SANS_VARIATION_ENTRAXE.showMaximized()
	#SANS_VARIATION_ENTRAXE.show()


def afficher_VARIATION_ENTRAXE():
	VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	VARIATION_ENTRAXE.showMaximized()
	#VARIATION_ENTRAXE.show()


def afficher_METHODE_ISO_SANS_VARIATION_ENTRAXE():
	METHODE_ISO_SANS_VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	METHODE_ISO_SANS_VARIATION_ENTRAXE.showMaximized()
	#METHODE_ISO_SANS_VARIATION_ENTRAXE.show()

def afficher_METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE():
	METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE.showMaximized()
	#METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE.show()

def afficher_METHODE_WRICHTER_SANS_VARIATION_ENTRAXE():
	METHODE_WRICHTER_SANS_VARIATION_ENTRAXE.setMinimumSize(1080, 720)
	METHODE_WRICHTER_SANS_VARIATION_ENTRAXE.showMaximized()
	#METHODE_WRICHTER_SANS_VARIATION_ENTRAXE.show()


def afficher_METHODE_ISO_D_DROITE():
	METHODE_ISO_D_DROITE.setMinimumSize(1080, 720)
	METHODE_ISO_D_DROITE.showMaximized()
	#METHODE_ISO_D_DROITE.show()


def afficher_METHODE_ISO_D_HELICOIDALE():
	METHODE_ISO_D_HELICOIDALE.setMinimumSize(1080, 720)
	METHODE_ISO_D_HELICOIDALE.showMaximized()
	#METHODE_ISO_D_HELICOIDALE.show()

def afficher_METHODE_W_RICHTER_D_DROITE():
	METHODE_W_RICHTER_D_DROITE.setMinimumSize(1080, 720)
	METHODE_W_RICHTER_D_DROITE.showMaximized()
	#METHODE_W_RICHTER_D_DROITE.show()

def afficher_METHODE_DE_W_RICHTER_D_HELICOIDALE():
	METHODE_DE_W_RICHTER_D_HELICOIDALE.setMinimumSize(1080, 720)
	METHODE_DE_W_RICHTER_D_HELICOIDALE.showMaximized()
	#METHODE_DE_W_RICHTER_D_HELICOIDALE.show()

def afficher_METHODE_MAAG_TASCHENBUCH_D_DROITE():
	METHODE_MAAG_TASCHENBUCH_D_DROITE.setMinimumSize(1080, 720)
	METHODE_MAAG_TASCHENBUCH_D_DROITE.showMaximized()
	#METHODE_MAAG_TASCHENBUCH_D_DROITE.show()

def afficher_METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE():
	METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE.setMinimumSize(1080, 720)
	METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE.showMaximized()
	#METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE.show()

def afficher_Denture_droite_deporteE():
	Denture_droite_deporteE.setMinimumSize(1080, 720)
	Denture_droite_deporteE.showMaximized()
	#Denture_droite_deporteE.show()

def afficher_Denture_droite_deporteIN():
	Denture_droite_deporteIN.setMinimumSize(1080, 720)
	Denture_droite_deporteIN.showMaximized()
	#Denture_droite_deporteIN.show()

def afficher_Denture_droiteH_deporteIN():
	Denture_droiteH_deporteIN.setMinimumSize(1080, 720)
	Denture_droiteH_deporteIN.showMaximized()
	#Denture_droiteH_deporteIN.show()

def afficher_Denture_droiteH_deporteE():
	Denture_droiteH_deporteE.setMinimumSize(1080, 720)
	Denture_droiteH_deporteE.showMaximized()
	#Denture_droiteH_deporteE.show()

def afficher_Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE():
	Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE.setMinimumSize(1080, 720)
	Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE.showMaximized()
	#Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE.show()


def afficher_Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE():
	Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE.setMinimumSize(1080, 720)
	Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE.showMaximized()
	#Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE.show()

def afficher_Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE():
	Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE.setMinimumSize(1080, 720)
	Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE.showMaximized()
	#Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE.show()


def afficher_Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE():
	Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE.setMinimumSize(1080, 720)
	Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE.showMaximized()
	#Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE.show()

def afficher_Denture_droite_deporteEX_VARIATION_ENT_IMPOSE():
	Denture_droite_deporteEX_VARIATION_ENT_IMPOSE.setMinimumSize(1080, 720)
	Denture_droite_deporteEX_VARIATION_ENT_IMPOSE.showMaximized()
	#Denture_droite_deporteEX_VARIATION_ENT_IMPOSE.show()

def afficher_Denture_droite_deporteIN_VARIATION_ENT_IMPOSE():
	Denture_droite_deporteIN_VARIATION_ENT_IMPOSE.setMinimumSize(1080, 720)
	Denture_droite_deporteIN_VARIATION_ENT_IMPOSE.showMaximized()
	#Denture_droite_deporteIN_VARIATION_ENT_IMPOSE.show()

def afficher_Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE():
	Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE.setMinimumSize(1080, 720)
	Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE.showMaximized()
	#Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE.show()

def afficher_Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE():
	Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE.setMinimumSize(1080, 720)
	Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE.showMaximized()
	#Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE.show()

# FIN CHAPITRE 2


# DEBUT CHAPITRE 3

def afficher_ENGRENAGE_CONCOURANTE():
	ENGRENAGE_CONCOURANTE.setMinimumSize(1080, 720)
	ENGRENAGE_CONCOURANTE.showMaximized()
	#ENGRENAGE_CONCOURANTE.show()

def afficher_ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE():
	ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE.setMinimumSize(1080, 720)
	ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE.showMaximized()
	#ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE.show()

def afficher_ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE():
	ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE.setMinimumSize(1080, 720)
	ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE.showMaximized()
	#ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE.show()

def afficher_ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE():
	ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE.setMinimumSize(1080, 720)
	ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE.showMaximized()
	#ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE.show()

def afficher_ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE():
	ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE.setMinimumSize(1080, 720)
	ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE.showMaximized()
	#ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE.show()

def afficher_ROUE_VIS_SANS_FIN():
	ROUE_VIS_SANS_FIN.setMinimumSize(1080, 720)
	ROUE_VIS_SANS_FIN.showMaximized()
	#ROUE_VIS_SANS_FIN.show()

# FIN CHAPITRE 3

# DEBUT CHAPITRE 4

def afficher_RESISTANCES_EFFORTS():
	RESISTANCE_EFFORT.setMinimumSize(1080, 720)
	RESISTANCE_EFFORT.showMaximized()
	
def afficher_LES_EFFORTS_SUR_DENTS():
	LES_EFFORTS_SUR_DENTS.setMinimumSize(1080, 720)
	LES_EFFORTS_SUR_DENTS.showMaximized()

def afficher_DENTURE_DROITE_PARALLELE():
	DENTURE_DROITE_PARALLELE.setMinimumSize(1080, 720)
	DENTURE_DROITE_PARALLELE.showMaximized()

def afficher_DENTURE_HELICOIDALE_PARALLELE():
	DENTURE_HELICOIDALE_PARALLELE.setMinimumSize(1080, 720)
	DENTURE_HELICOIDALE_PARALLELE.showMaximized()

def afficher_DENTURE_CONIQUE():
	DENTURE_CONIQUE.setMinimumSize(1080, 720)
	DENTURE_CONIQUE.showMaximized()

def afficher_LES_EFFORTS_ROUE_ET_VIS():
	LES_EFFORTS_ROUE_ET_VIS.setMinimumSize(1080, 720)
	LES_EFFORTS_ROUE_ET_VIS.showMaximized()


def afficher_RESISTANCE_ENGRENAGE_PARALLELE():
	RESISTANCE_ENGRENAGE_PARALLELE.setMinimumSize(1080, 720)
	RESISTANCE_ENGRENAGE_PARALLELE.showMaximized()

def afficher_RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE():
	RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE.setMinimumSize(1080, 720)
	RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE.showMaximized()

def afficher_RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE():
	RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE.setMinimumSize(1080, 720)
	RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE.showMaximized()

def afficher_RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE():
	RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE.setMinimumSize(1080, 720)
	RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE.showMaximized()


def afficher_RESISTANCE_HELICOI_ENTRAXE_IMPOSE():
	RESISTANCE_HELICOI_ENTRAXE_IMPOSE.setMinimumSize(1080, 720)
	RESISTANCE_HELICOI_ENTRAXE_IMPOSE.showMaximized()

# CREATION DE LA FENETRE MENU
app = QtWidgets.QApplication(sys.argv)
LOGICIEL_DE_CALCUL = QtWidgets.QMainWindow()
ui = Ui_LOGICIEL_DE_CALCUL()
ui.setupUi(LOGICIEL_DE_CALCUL)
ui.pushButton_2.clicked.connect(retour)

# creation de la fenetre_2
different_type_engrenage = QtWidgets.QWidget()
uifenetre_2 = Ui_different_type_engrenage()
uifenetre_2.setupUi(different_type_engrenage)
uifenetre_2.bouton_retour_ch11.clicked.connect(premier_fenetre)
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
########### FIN DES SOUS FENETRES DU 1ER CHAPITRE ###########


########### SOUS FENETRES DU 2ieme CHAPITRE ###########

# creation de la fenetre engrenages deportes
ENGRENAGES_DEPORTEES = QtWidgets.QWidget()
uiENGRENAGEDEPORTES = Ui_ENGRENAGES_DEPORTEES()
uiENGRENAGEDEPORTES.setupUi(ENGRENAGES_DEPORTEES)
uiENGRENAGEDEPORTES.pushButton_5_CH20.clicked.connect(retour_8)


# creation de la fenetre determination des deports sans variation d'entraxe
DEPORTS_SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
uiDEPORTS_SV_ENTRAXE = Ui_DEPORTS_SANS_VARIATION_ENTRAXE()
uiDEPORTS_SV_ENTRAXE.setupUi(DEPORTS_SANS_VARIATION_ENTRAXE)
uiDEPORTS_SV_ENTRAXE.pushButton_4_SANS_VARIATION.clicked.connect(retour_9)

# creation de la fenetre determination des deports avec variation d'entraxe
DEPORTS_AVEC_VARIATION_ENTRAXE = QtWidgets.QWidget()
uiDEPORTS_AV_ENTRAXE = Ui_DEPORTS_AVEC_VARIATION_ENTRAXE()
uiDEPORTS_AV_ENTRAXE.setupUi(DEPORTS_AVEC_VARIATION_ENTRAXE)
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION_7.clicked.connect(retour_10)

# creation de la fenetre engrenage deportes sans variation d'entraxe
SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
uiSANS_V_ENTRAXE = Ui_SANS_VARIATION_ENTRAXE()
uiSANS_V_ENTRAXE.setupUi(SANS_VARIATION_ENTRAXE)
uiSANS_V_ENTRAXE.pushButton_9_CH22.clicked.connect(retour_11)

# creation de la fenetre engrenage deportes avec variation d'entraxe
VARIATION_ENTRAXE = QtWidgets.QWidget()
uiAVEC_V_ENTRAXE = Ui_VARIATION_ENTRAXE()
uiAVEC_V_ENTRAXE.setupUi(VARIATION_ENTRAXE)
uiAVEC_V_ENTRAXE.pushButton_9_CH21.clicked.connect(retour_12)


# Fenetre Methode ISO sans variation d'entraxe
METHODE_ISO_SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
uiMETHODE_ISO_SANS = Ui_METHODE_ISO_SANS_VARIATION_ENTRAXE()
uiMETHODE_ISO_SANS.setupUi(METHODE_ISO_SANS_VARIATION_ENTRAXE)
uiMETHODE_ISO_SANS.pushButton_2.clicked.connect(retour_13)

# Fenetre METHODE DE MAAGTASCHENBUCH SANS VARIATION ENTRAXE
METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
uiMETHODE_MAAG_SANS = Ui_METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE()
uiMETHODE_MAAG_SANS.setupUi(METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE)
uiMETHODE_MAAG_SANS.pushButton_2.clicked.connect(retour_15)

# Fenetre METHODE DE MAAGTASCHENBUCH SANS VARIATION ENTRAXE
METHODE_WRICHTER_SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
uiMETHODE_WRICHTER_SANS = Ui_METHODE_WRICHTER_SANS_VARIATION_ENTRAXE()
uiMETHODE_WRICHTER_SANS.setupUi(METHODE_WRICHTER_SANS_VARIATION_ENTRAXE)
uiMETHODE_WRICHTER_SANS.pushButton_2.clicked.connect(retour_14)

# Fenetre METHODE ISO AVEC VARIATION D'ENTRAXE DENTURE DROITE
METHODE_ISO_D_DROITE = QtWidgets.QWidget()
uiMETHODE_ISO_D = Ui_METHODE_ISO_D_DROITE()
uiMETHODE_ISO_D.setupUi(METHODE_ISO_D_DROITE)
uiMETHODE_ISO_D.pushButton_2.clicked.connect(retour_16)

# Fenetre METHODE ISO AVEC VARIATION D'ENTRAXE HELICOIDALE
METHODE_ISO_D_HELICOIDALE = QtWidgets.QWidget()
uiMETHODE_ISO_D_HELI = Ui_METHODE_ISO_D_HELICOIDALE()
uiMETHODE_ISO_D_HELI.setupUi(METHODE_ISO_D_HELICOIDALE)
uiMETHODE_ISO_D_HELI.pushButton_2.clicked.connect(retour_19)

# Fenetre METHODE DE W.RICHTER AVEC VARIATION D'ENTRAXE DENTURE DROITE
METHODE_W_RICHTER_D_DROITE = QtWidgets.QWidget()
uiMETHODE_W_RICHTER_D = Ui_METHODE_W_RICHTER_D_DROITE()
uiMETHODE_W_RICHTER_D.setupUi(METHODE_W_RICHTER_D_DROITE)
uiMETHODE_W_RICHTER_D.pushButton_2.clicked.connect(retour_17)

# Fenetre METHODE DE W.RICHTER AVEC VARIATION D'ENTRAXE DENTURE HELICOIDALE
METHODE_DE_W_RICHTER_D_HELICOIDALE = QtWidgets.QWidget()
uiMETHODE_DE_W_RICHTER_H = Ui_METHODE_DE_W_RICHTER_D_HELICOIDALE()
uiMETHODE_DE_W_RICHTER_H.setupUi(METHODE_DE_W_RICHTER_D_HELICOIDALE)
uiMETHODE_DE_W_RICHTER_H.pushButton_2.clicked.connect(retour_20)

# Fenetre METHODE_MAAG_TASCHENBUCH AVEC VARIATION D'ENTRAXE DENTURE DROITE
METHODE_MAAG_TASCHENBUCH_D_DROITE = QtWidgets.QWidget()
uiMETHODE_MAAG_D = Ui_METHODE_MAAG_TASCHENBUCH_D_DROITE()
uiMETHODE_MAAG_D.setupUi(METHODE_MAAG_TASCHENBUCH_D_DROITE)
uiMETHODE_MAAG_D.pushButton_2.clicked.connect(retour_18)


# Fenetre METHODE_MAAG_TASCHENBUCH AVEC VARIATION D'ENTRAXE DENTURE HELICOIDALE
METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE = QtWidgets.QWidget()
uiMETHODE_MAAG_H = Ui_METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE()
uiMETHODE_MAAG_H.setupUi(METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE)
uiMETHODE_MAAG_H.pushButton_2.clicked.connect(retour_21)


# fenetre denture droite deporte exterieur sans variation d'entraxe
Denture_droite_deporteE = QtWidgets.QWidget()
uiDenture_droite_deporteE = Ui_Denture_droite_deporteE()
uiDenture_droite_deporteE.setupUi(Denture_droite_deporteE)
uiDenture_droite_deporteE.pushButton_2.clicked.connect(retour_22)

# fenetre denture droite deporte interieur sans variation d'entraxe
Denture_droite_deporteIN = QtWidgets.QWidget()
uiDenture_droite_deporteIN = Ui_Denture_droite_deporteIN()
uiDenture_droite_deporteIN.setupUi(Denture_droite_deporteIN)
uiDenture_droite_deporteIN.pushButton_2.clicked.connect(retour_23)

# fenetre denture helicoidale deporte interieur sans variation d'entraxe
Denture_droiteH_deporteIN = QtWidgets.QWidget()
uiDenture_droiteH_deporteIN = Ui_Denture_droiteH_deporteIN()
uiDenture_droiteH_deporteIN.setupUi(Denture_droiteH_deporteIN)
uiDenture_droiteH_deporteIN.pushButton_2.clicked.connect(retour_24)

# fenetre denture helicoidale deporte exterieur sans variation d'entraxe
Denture_droiteH_deporteE = QtWidgets.QWidget()
uiDenture_droiteH_deporteE = Ui_Denture_droiteH_deporteE()
uiDenture_droiteH_deporteE.setupUi(Denture_droiteH_deporteE)
uiDenture_droiteH_deporteE.pushButton_2.clicked.connect(retour_25)

# fenetre denture droite deporte exterieur avec variation d'entraxe (entraxe non impose)
Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE = QtWidgets.QWidget()
uideporteEX_VARIATION_ANT_NON_IMPOSE = Ui_Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE()
uideporteEX_VARIATION_ANT_NON_IMPOSE.setupUi(Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE)
uideporteEX_VARIATION_ANT_NON_IMPOSE.pushButton_2.clicked.connect(retour_26)

# fenetre denture droite deporte interieur avec variation d'entraxe (entraxe non impose)
Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE = QtWidgets.QWidget()
uideporteIN_VARIATION_ANT_NON_IMPOSE = Ui_Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE()
uideporteIN_VARIATION_ANT_NON_IMPOSE.setupUi(Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE)
uideporteIN_VARIATION_ANT_NON_IMPOSE.pushButton_2.clicked.connect(retour_27)

# fenetre denture helicoidale deporte exterieur avec variation d'entraxe (entraxe non impose)
Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE = QtWidgets.QWidget()
uiDenture_droiteH_deporteE_VARIATION = Ui_Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE()
uiDenture_droiteH_deporteE_VARIATION.setupUi(Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE)
uiDenture_droiteH_deporteE_VARIATION.pushButton_2.clicked.connect(retour_28)

# fenetre denture helicoidale deporte interieur avec variation d'entraxe (entraxe non impose)
Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE = QtWidgets.QWidget()
uiDenture_droiteH_deporteIN_VARIATION = Ui_Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE()
uiDenture_droiteH_deporteIN_VARIATION.setupUi(Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE)
uiDenture_droiteH_deporteIN_VARIATION.pushButton_2.clicked.connect(retour_29)

# fenetre denture droite deporte exterieur avec variation d'entraxe (entraxe impose)
Denture_droite_deporteEX_VARIATION_ENT_IMPOSE = QtWidgets.QWidget()
uiDenture_droiteEX_ENTRAXE_IMPOSE = Ui_Denture_droite_deporteEX_VARIATION_ENT_IMPOSE()
uiDenture_droiteEX_ENTRAXE_IMPOSE.setupUi(Denture_droite_deporteEX_VARIATION_ENT_IMPOSE)
uiDenture_droiteEX_ENTRAXE_IMPOSE.pushButton_2.clicked.connect(retour_30)

# fenetre denture droite deporte interieur avec variation d'entraxe (entraxe impose)
Denture_droite_deporteIN_VARIATION_ENT_IMPOSE = QtWidgets.QWidget()
uiDenture_droiteIN_ENTRAXE_IMPOSE = Ui_Denture_droite_deporteIN_VARIATION_ENT_IMPOSE()
uiDenture_droiteIN_ENTRAXE_IMPOSE.setupUi(Denture_droite_deporteIN_VARIATION_ENT_IMPOSE)
uiDenture_droiteIN_ENTRAXE_IMPOSE.pushButton_2.clicked.connect(retour_31)

# fenetre denture helicoidale deporte exterieur avec variation d'entraxe (entraxe impose)
Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE = QtWidgets.QWidget()
uiDenture_helicoidal_EX_ENTRAXE_IMPOSE = Ui_Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE()
uiDenture_helicoidal_EX_ENTRAXE_IMPOSE.setupUi(Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE)
uiDenture_helicoidal_EX_ENTRAXE_IMPOSE.pushButton_2.clicked.connect(retour_32)
    
# fenetre denture helicoidale deporte interieur avec variation d'entraxe (entraxe impose)
Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE = QtWidgets.QWidget()
uiDenture_helicoidal_IN_ENTRAXE_IMPOSE = Ui_Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE()
uiDenture_helicoidal_IN_ENTRAXE_IMPOSE.setupUi(Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE)
uiDenture_helicoidal_IN_ENTRAXE_IMPOSE.pushButton_2.clicked.connect(retour_33)

########### FIN DES SOUS FENETRES DU 2ieme CHAPITRE ###########



########### FENETRES DU 3ieme CHAPITRE ###########
ENGRENAGE_CONCOURANTE = QtWidgets.QWidget()
uiENGRENAGE_CONCOURANTE = Ui_ENGRENAGE_CONCOURANTE()
uiENGRENAGE_CONCOURANTE.setupUi(ENGRENAGE_CONCOURANTE)
uiENGRENAGE_CONCOURANTE.pushButton_9_CH21.clicked.connect(retour_34)

ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE = QtWidgets.QWidget()
uiENGRENAGE_CONIQUE_N = Ui_ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE()
uiENGRENAGE_CONIQUE_N.setupUi(ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE)
uiENGRENAGE_CONIQUE_N.pushButton_2.clicked.connect(retour_35)

ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE = QtWidgets.QWidget()
uiENGRENAGE_CONIQUE_D = Ui_ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE()
uiENGRENAGE_CONIQUE_D.setupUi(ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE)
uiENGRENAGE_CONIQUE_D.pushButton_2.clicked.connect(retour_36)

ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE = QtWidgets.QWidget()
uiENGRENAGE_CONIQUE_HELICOIDALE_N = Ui_ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE()
uiENGRENAGE_CONIQUE_HELICOIDALE_N.setupUi(ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE)
uiENGRENAGE_CONIQUE_HELICOIDALE_N.pushButton_2.clicked.connect(retour_37)

ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE = QtWidgets.QWidget()
uiENGRENAGE_CONIQUE_HELICOIDALE_D = Ui_ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE()
uiENGRENAGE_CONIQUE_HELICOIDALE_D.setupUi(ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE)
uiENGRENAGE_CONIQUE_HELICOIDALE_D.pushButton_2.clicked.connect(retour_38)

ROUE_VIS_SANS_FIN = QtWidgets.QWidget()
uiROUE_VIS = Ui_ROUE_VIS_SANS_FIN()
uiROUE_VIS.setupUi(ROUE_VIS_SANS_FIN)
uiROUE_VIS.pushButton_2.clicked.connect(retour_39)
########### FIN DES SOUS FENETRES DU 3ieme CHAPITRE ###########


########### FENETRES DU 4ieme CHAPITRE ###########

# creation de la fenetre pour les caluls des efforts et des resistances
RESISTANCE_EFFORT = QtWidgets.QWidget()
uiRESISTANCE_EFFORT = Ui_RESISTANCE_EFFORT()
uiRESISTANCE_EFFORT.setupUi(RESISTANCE_EFFORT)
uiRESISTANCE_EFFORT.RETOUR_RESISTRANCE_EFFORTS.clicked.connect(retour_40)

LES_EFFORTS_SUR_DENTS = QtWidgets.QWidget()
uiLES_EFFORTS_SUR_DENTS = Ui_LES_EFFORTS_SUR_DENTS()
uiLES_EFFORTS_SUR_DENTS.setupUi(LES_EFFORTS_SUR_DENTS)
uiLES_EFFORTS_SUR_DENTS.pushButton_RETOUR_EFFORTS_SUR_DENTS.clicked.connect(retour_41)

DENTURE_DROITE_PARALLELE = QtWidgets.QWidget()
uiDENTURE_DROITE_PARALLELE = Ui_DENTURE_DROITE_PARALLELE()
uiDENTURE_DROITE_PARALLELE.setupUi(DENTURE_DROITE_PARALLELE)
uiDENTURE_DROITE_PARALLELE.pushButton_2.clicked.connect(retour_42)

DENTURE_HELICOIDALE_PARALLELE = QtWidgets.QWidget()
uiDENTURE_HELICOIDALE_PARALLELE = Ui_DENTURE_HELICOIDALE_PARALLELE()
uiDENTURE_HELICOIDALE_PARALLELE.setupUi(DENTURE_HELICOIDALE_PARALLELE)
uiDENTURE_HELICOIDALE_PARALLELE.pushButton_2.clicked.connect(retour_43)

DENTURE_CONIQUE = QtWidgets.QWidget()
uiDENTURE_CONIQUE = Ui_DENTURE_CONIQUE()
uiDENTURE_CONIQUE.setupUi(DENTURE_CONIQUE)
uiDENTURE_CONIQUE.pushButton_2.clicked.connect(retour_44)

LES_EFFORTS_ROUE_ET_VIS = QtWidgets.QWidget()
uiLES_EFFORTS_ROUE_ET_VIS = Ui_LES_EFFORTS_ROUE_ET_VIS()
uiLES_EFFORTS_ROUE_ET_VIS.setupUi(LES_EFFORTS_ROUE_ET_VIS)
uiLES_EFFORTS_ROUE_ET_VIS.pushButton_2.clicked.connect(retour_45)

# fenetre pour le calcul de resistance des dents des engrenages paralleles
RESISTANCE_ENGRENAGE_PARALLELE = QtWidgets.QWidget()
uiRESISTANCE_ENGRENAGE_PARALLELE = Ui_RESISTANCE_ENGRENAGE_PARALLELE()
uiRESISTANCE_ENGRENAGE_PARALLELE.setupUi(RESISTANCE_ENGRENAGE_PARALLELE)
uiRESISTANCE_ENGRENAGE_PARALLELE.pushButton_RETOUR_EFFORTS_SUR_DENTS.clicked.connect(retour_46)

# fenetre pour le calcul de resistance des engrenages parallele a denture droite sans imposer entraxe
RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE = QtWidgets.QWidget()
uiRESISTANCE_DROITE_ENTRAXE_NON_IMPOSE = Ui_RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE()
uiRESISTANCE_DROITE_ENTRAXE_NON_IMPOSE.setupUi(RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE)
uiRESISTANCE_DROITE_ENTRAXE_NON_IMPOSE.RETOUR_RESISTANCE_DROITE_PARALLELE_ENTRAXE_NON_IMPOSE.clicked.connect(retour_47)

# fenetre pour le calcul de resistance des engrenages parallele a denture droite avec entraxe imposer
RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE = QtWidgets.QWidget()
uiRESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE = Ui_RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE()
uiRESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE.setupUi(RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE)
uiRESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE.RETOUR_RESISTANCE_HELICOI_PARALLELE.clicked.connect(retour_48)

RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE = QtWidgets.QWidget()
uiRESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE = Ui_RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE()
uiRESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE.setupUi(RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE)
uiRESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE.RETOUR_RESISTANCE_HELICOI_PARALLELE_ENTRAXE_NON_IMPOSE.clicked.connect(retour_49)

RESISTANCE_HELICOI_ENTRAXE_IMPOSE = QtWidgets.QWidget()
uiRESISTANCE_HELICOI_ENTRAXE_IMPOSE = Ui_RESISTANCE_HELICOI_ENTRAXE_IMPOSE()
uiRESISTANCE_HELICOI_ENTRAXE_IMPOSE.setupUi(RESISTANCE_HELICOI_ENTRAXE_IMPOSE)
uiRESISTANCE_HELICOI_ENTRAXE_IMPOSE.RETOUR_RESISTANCE_HELICOI_PARALLELE.clicked.connect(retour_50)


LOGICIEL_DE_CALCUL.setMinimumSize(1080, 720)  # Définit la taille minimale de la fenêtre
LOGICIEL_DE_CALCUL.show()
LOGICIEL_DE_CALCUL.showMaximized()  # Maximise la fenêtre pour qu'elle occupe tout l'écran


# Le bouton d'ouverture de la fenetre 2
ui.pushButton.clicked.connect(afficherfenetre2)


# Les boutons_ouverture (CHAPITRE 1)
uifenetre_2.bouton_case1.clicked.connect(affichercase1)
uicase1.bouton_case11.clicked.connect(afficherdenture_droite_exterieur)
uicase1.bouton_case13.clicked.connect(afficherdenture_droite_interieur)
uicase1.bouton_case15.clicked.connect(affichermodule)
uicase1.bouton_case12.clicked.connect(afficferdenture_droite_hE)
uicase1.bouton_case14.clicked.connect(afficferdenture_droite_hI)
# Fin des boutons_ouverture (CHAPITRE 1)

# Les boutons_ouverture (CHAPITRE 2)
uifenetre_2.bouton_case2.clicked.connect(afficher_Engrenages_Deportees)
uiENGRENAGEDEPORTES.pushButton_2_CH20.clicked.connect(afficher_DEPORTS_SANS_VARIATION_ENTRAXE)
uiENGRENAGEDEPORTES.pushButton_CH20.clicked.connect(afficher_DEPORTS_AVEC_VARIATION_ENTRAXE)
uiENGRENAGEDEPORTES.pushButton_4_CH20.clicked.connect(afficher_SANS_VARIATION_ENTRAXE)
uiENGRENAGEDEPORTES.pushButton_3_CH20.clicked.connect(afficher_VARIATION_ENTRAXE)

# bouton pour l'ouverture des differentes methodes pour le calcul des deports sans variation d'entraxe
uiDEPORTS_SV_ENTRAXE.pushButton_SANS_VARIATION.clicked.connect(afficher_METHODE_ISO_SANS_VARIATION_ENTRAXE)
uiDEPORTS_SV_ENTRAXE.pushButton_3_SANS_VARIATION.clicked.connect(afficher_METHODE_MAAGTASCHENBUCH_SANS_VARIATION_ENTRAXE)
uiDEPORTS_SV_ENTRAXE.pushButton_2_SANS_VARIATION.clicked.connect(afficher_METHODE_WRICHTER_SANS_VARIATION_ENTRAXE)

# bouton pour l'ouverture des differentes methodes pour le calcul des deports avec variation d'entraxe
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION.clicked.connect(afficher_METHODE_ISO_D_DROITE)
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION_2.clicked.connect(afficher_METHODE_ISO_D_HELICOIDALE)
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION_3.clicked.connect(afficher_METHODE_W_RICHTER_D_DROITE)
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION_4.clicked.connect(afficher_METHODE_DE_W_RICHTER_D_HELICOIDALE)
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION_5.clicked.connect(afficher_METHODE_MAAG_TASCHENBUCH_D_DROITE)
uiDEPORTS_AV_ENTRAXE.pushButton_AVEC_VARIATION_6.clicked.connect(afficher_METHODE_MAAG_TASCHENBUCH_D_HELICOIDALE)

# bouton pour l'ouverture des differents type d'engrenage sans variation d'entraxe
uiSANS_V_ENTRAXE.pushButton_CH22.clicked.connect(afficher_Denture_droite_deporteE)
uiSANS_V_ENTRAXE.pushButton_2_CH22.clicked.connect(afficher_Denture_droite_deporteIN)
uiSANS_V_ENTRAXE.pushButton_4_CH22.clicked.connect(afficher_Denture_droiteH_deporteIN)
uiSANS_V_ENTRAXE.pushButton_3_CH22.clicked.connect(afficher_Denture_droiteH_deporteE)


# bouton pour l'ouverture des differents type d'engrenage avec variation d'entraxe
uiAVEC_V_ENTRAXE.pushButton_CH21.clicked.connect(afficher_Denture_droite_deporteEX_VARIATION_ANT_NON_IMPOSE)
uiAVEC_V_ENTRAXE.pushButton_2_CH21.clicked.connect(afficher_Denture_droite_deporteIN_VARIATION_ANT_NON_IMPOSE)
uiAVEC_V_ENTRAXE.pushButton_3_CH21.clicked.connect(afficher_Denture_droiteH_deporteE_VARIATION_ANT_NON_IMPOSE)
uiAVEC_V_ENTRAXE.pushButton_4_CH21.clicked.connect(afficher_Denture_droiteH_deporteIN_VARIATION_ANT_NON_IMPOSE)

uiAVEC_V_ENTRAXE.pushButton_5_CH21.clicked.connect(afficher_Denture_droite_deporteEX_VARIATION_ENT_IMPOSE)
uiAVEC_V_ENTRAXE.pushButton_6_CH21.clicked.connect(afficher_Denture_droite_deporteIN_VARIATION_ENT_IMPOSE)
uiAVEC_V_ENTRAXE.pushButton_7_CH21.clicked.connect(afficher_Denture_droiteH_deporteE_VARIATION_ENT_IMPOSE)
uiAVEC_V_ENTRAXE.pushButton_8_CH21.clicked.connect(afficher_Denture_droiteH_deporteIN_VARIATION_ENT_IMPOSE)
#Fin des boutons_ouverture (CHAPITRE 2)

# Les boutons_ouverture (CHAPITRE 3)
uifenetre_2.bouton_case3.clicked.connect(afficher_ENGRENAGE_CONCOURANTE)
uiENGRENAGE_CONCOURANTE.pushButton_CH31.clicked.connect(afficher_ENGRENAGE_CONIQUE_DROIT_DENTURE_NORMALE)
uiENGRENAGE_CONCOURANTE.pushButton_2_CH31.clicked.connect(afficher_ENGRENAGE_CONIQUE_DROIT_DENTURE_DEPORTEE)
uiENGRENAGE_CONCOURANTE.pushButton_3_CH31.clicked.connect(afficher_ENGRENAGE_CONIQUE_HELICOIDALE_NON_DEPORTEE)
uiENGRENAGE_CONCOURANTE.pushButton_4_CH31.clicked.connect(afficher_ENGRENAGE_CONIQUE_HELICOIDALE_DEPORTEE)
uiENGRENAGE_CONCOURANTE.pushButton_5_CH31.clicked.connect(afficher_ROUE_VIS_SANS_FIN)
#Fin des boutons_ouverture (CHAPITRE 3)

# Les boutons_ouverture (CHAPITRE 4)
uifenetre_2.bouton_case4.clicked.connect(afficher_RESISTANCES_EFFORTS)
uiRESISTANCE_EFFORT.pushButton_EFFORTS.clicked.connect(afficher_LES_EFFORTS_SUR_DENTS)
uiLES_EFFORTS_SUR_DENTS.pushButton_EFFORTS_DROITE.clicked.connect(afficher_DENTURE_DROITE_PARALLELE)
uiLES_EFFORTS_SUR_DENTS.pushButton_EFFORTS_HELICOIDALE.clicked.connect(afficher_DENTURE_HELICOIDALE_PARALLELE)
uiLES_EFFORTS_SUR_DENTS.pushButton_EFFORTS_CONCOURANT.clicked.connect(afficher_DENTURE_CONIQUE)
uiLES_EFFORTS_SUR_DENTS.pushButton_EFFORTS_ROUE_VIS.clicked.connect(afficher_LES_EFFORTS_ROUE_ET_VIS)
uiRESISTANCE_EFFORT.pushButton_RESISTANCE.clicked.connect(afficher_RESISTANCE_ENGRENAGE_PARALLELE)
uiRESISTANCE_ENGRENAGE_PARALLELE.pushButton_EFFORTS_DROITE.clicked.connect(afficher_RESISTANCE_DROITE_ENTRAXE_NON_IMPOSE)
uiRESISTANCE_ENGRENAGE_PARALLELE.pushButton_EFFORTS_HELICOIDALE.clicked.connect(afficher_RESISTANCE_DROITE_AVEC_ENTRAXE_IMPOSE)
uiRESISTANCE_ENGRENAGE_PARALLELE.pushButton_EFFORTS_CONCOURANT.clicked.connect(afficher_RESISTANCE_HELICOI_ENTRAXE_NON_IMPOSE)
uiRESISTANCE_ENGRENAGE_PARALLELE.pushButton_EFFORTS_ROUE_VIS.clicked.connect(afficher_RESISTANCE_HELICOI_ENTRAXE_IMPOSE)


sys.exit(app.exec_())