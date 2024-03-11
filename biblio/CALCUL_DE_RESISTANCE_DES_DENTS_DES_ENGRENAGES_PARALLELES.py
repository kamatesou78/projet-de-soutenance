
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RESISTANCE_ENGRENAGE_PARALLELE(object):
    def setupUi(self, RESISTANCE_ENGRENAGE_PARALLELE):
        RESISTANCE_ENGRENAGE_PARALLELE.setObjectName("RESISTANCE_ENGRENAGE_PARALLELE")
        #RESISTANCE_ENGRENAGE_PARALLELE.setWindowModality(QtCore.Qt.ApplicationModal)
        RESISTANCE_ENGRENAGE_PARALLELE.resize(719, 594)

        RESISTANCE_ENGRENAGE_PARALLELE.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RESISTANCE_ENGRENAGE_PARALLELE.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(RESISTANCE_ENGRENAGE_PARALLELE)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(RESISTANCE_ENGRENAGE_PARALLELE)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 927, 567))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_EFFORTS_DROITE = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS_DROITE.setFont(font)
        self.pushButton_EFFORTS_DROITE.setObjectName("pushButton_EFFORTS_DROITE")

        self.pushButton_EFFORTS_DROITE.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_EFFORTS_DROITE, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.pushButton_EFFORTS_CONCOURANT = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS_CONCOURANT.setFont(font)
        self.pushButton_EFFORTS_CONCOURANT.setObjectName("pushButton_EFFORTS_CONCOURANT")

        self.pushButton_EFFORTS_CONCOURANT.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_EFFORTS_CONCOURANT, 2, 0, 1, 1)
        self.pushButton_EFFORTS_ROUE_VIS = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS_ROUE_VIS.setFont(font)
        self.pushButton_EFFORTS_ROUE_VIS.setObjectName("pushButton_EFFORTS_ROUE_VIS")

        self.pushButton_EFFORTS_ROUE_VIS.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_EFFORTS_ROUE_VIS, 3, 0, 1, 1)
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setFont(font)
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setObjectName("pushButton_RETOUR_EFFORTS_SUR_DENTS")

        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setStyleSheet("background-color: #ff557f; color: black;")

        self.gridLayout.addWidget(self.pushButton_RETOUR_EFFORTS_SUR_DENTS, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_EFFORTS_HELICOIDALE = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS_HELICOIDALE.setFont(font)
        self.pushButton_EFFORTS_HELICOIDALE.setObjectName("pushButton_EFFORTS_HELICOIDALE")

        self.pushButton_EFFORTS_HELICOIDALE.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_EFFORTS_HELICOIDALE, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(RESISTANCE_ENGRENAGE_PARALLELE)
        QtCore.QMetaObject.connectSlotsByName(RESISTANCE_ENGRENAGE_PARALLELE)

    def retranslateUi(self, RESISTANCE_ENGRENAGE_PARALLELE):
        _translate = QtCore.QCoreApplication.translate
        RESISTANCE_ENGRENAGE_PARALLELE.setWindowTitle(_translate("RESISTANCE_ENGRENAGE_PARALLELE", "CALCUL DE RESISTANCE SUR LES ENGRENAGES PARALLELES"))
        self.pushButton_EFFORTS_DROITE.setText(_translate("RESISTANCE_ENGRENAGE_PARALLELE", "CALCUL DE RESISTANCE DES DENTS DES ENGRENAGES A DENTURE\n"
" DROITE SANS IMPOSER L\'ENTRAXE DE FONCTIONNEMENT"))
        self.pushButton_EFFORTS_CONCOURANT.setText(_translate("RESISTANCE_ENGRENAGE_PARALLELE", "CALCUL DE RESISTANCE DES DENTS DES ENGRENAGES A DENTURE\n"
" HELICOIDALE SANS IMPOSER L\'ENTRAXE DE FONCTIONNEMENT"))
        self.pushButton_EFFORTS_ROUE_VIS.setText(_translate("RESISTANCE_ENGRENAGE_PARALLELE", "CALCUL DE RESISTANCE DES DENTS DES ENGRENAGES A DENTURE\n"
" HELICOIDALE AVEC ENTRAXE DE FONCTIONNEMENT IMPOSER"))
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setText(_translate("RESISTANCE_ENGRENAGE_PARALLELE", "RETOUR"))
        self.pushButton_EFFORTS_HELICOIDALE.setText(_translate("RESISTANCE_ENGRENAGE_PARALLELE", "CALCUL DE RESISTANCE DES DENTS DES ENGRENAGES A DENTURE\n"
" DROITE AVEC ENTRAXE DE FONCTIONNEMENT IMPOSER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RESISTANCE_ENGRENAGE_PARALLELE = QtWidgets.QWidget()
    ui = Ui_RESISTANCE_ENGRENAGE_PARALLELE()
    ui.setupUi(RESISTANCE_ENGRENAGE_PARALLELE)
    RESISTANCE_ENGRENAGE_PARALLELE.show()
    sys.exit(app.exec_())
