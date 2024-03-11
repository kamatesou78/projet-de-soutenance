

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fenetre_case1(object):
    def setupUi(self, fenetre_case1):
        fenetre_case1.setObjectName("fenetre_case1")
        fenetre_case1.resize(718, 629)
        fenetre_case1.setStyleSheet("background-color: #00aaff;")

        self.gridLayout_2 = QtWidgets.QGridLayout(fenetre_case1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bouton_case11 = QtWidgets.QPushButton(fenetre_case1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case11.setFont(font)
        self.bouton_case11.setObjectName("bouton_case11")

        self.bouton_case11.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case11, 0, 0, 1, 1)
        self.bouton_case12 = QtWidgets.QPushButton(fenetre_case1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case12.setFont(font)
        self.bouton_case12.setObjectName("bouton_case12")

        self.bouton_case12.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case12, 0, 1, 1, 1)
        self.bouton_case14 = QtWidgets.QPushButton(fenetre_case1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case14.setFont(font)
        self.bouton_case14.setObjectName("bouton_case14")

        self.bouton_case14.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case14, 1, 1, 1, 1)
        self.bouton_case13 = QtWidgets.QPushButton(fenetre_case1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case13.setFont(font)
        self.bouton_case13.setObjectName("bouton_case13")

        self.bouton_case13.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case13, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.bouton_case15 = QtWidgets.QPushButton(fenetre_case1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case15.setFont(font)
        self.bouton_case15.setObjectName("bouton_case15")

        self.bouton_case15.setStyleSheet("background-color: #00ff7f; color: black;")
        self.verticalLayout.addWidget(self.bouton_case15, 0, QtCore.Qt.AlignHCenter)
        self.bouton_retour_ch12 = QtWidgets.QPushButton(fenetre_case1)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_retour_ch12.setFont(font)
        self.bouton_retour_ch12.setObjectName("bouton_retour_ch12")

        self.bouton_retour_ch12.setStyleSheet("background-color: #ff557f; color: black;")
        self.verticalLayout.addWidget(self.bouton_retour_ch12, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(fenetre_case1)
        QtCore.QMetaObject.connectSlotsByName(fenetre_case1)

    def retranslateUi(self, fenetre_case1):
        _translate = QtCore.QCoreApplication.translate
        fenetre_case1.setWindowTitle(_translate("fenetre_case1", "fenetre_de_la_case1"))
        self.bouton_case11.setText(_translate("fenetre_case1", "ENGRENAGES\n"
" DROITS\n"
"A DENTURE DROITE                                    \n"
"         EXTERIEUR        "))
        self.bouton_case12.setText(_translate("fenetre_case1", "ENGRENAGES\n"
" DROITS\n"
"A DENTURE HELICOIDALE\n"
" EXTERIEUR"))
        self.bouton_case14.setText(_translate("fenetre_case1", "ENGRENAGES\n"
" DROITS\n"
" A DENTURE HELICOIDALE \n"
" INTERIEUR"))
        self.bouton_case13.setText(_translate("fenetre_case1", "ENGRENAGES\n"
" DROITS\n"
"A DENTURE DROITE \n"
"INTERIEUR"))
        self.bouton_case15.setText(_translate("fenetre_case1", "CALCULE DU MODULE\n"
" ET CHOIX DES VALEURS\n"
" NORMALISEES DU MODULE"))
        self.bouton_retour_ch12.setText(_translate("fenetre_case1", "RETOUR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetre_case1 = QtWidgets.QWidget()
    ui = Ui_fenetre_case1()
    ui.setupUi(fenetre_case1)
    fenetre_case1.show()
    sys.exit(app.exec_())
