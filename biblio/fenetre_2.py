
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_different_type_engrenage(object):
    def setupUi(self, different_type_engrenage):
        different_type_engrenage.setObjectName("different_type_engrenage")
        different_type_engrenage.resize(632, 290)

        #different_type_engrenage.setWindowModality(QtCore.Qt.ApplicationModal)
        different_type_engrenage.setStyleSheet("background-color: #00aaff;")

        self.gridLayout_2 = QtWidgets.QGridLayout(different_type_engrenage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bouton_case1 = QtWidgets.QPushButton(different_type_engrenage)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case1.setFont(font)
        self.bouton_case1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bouton_case1.setObjectName("bouton_case1")

        self.bouton_case1.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case1, 0, 0, 1, 1)
        self.bouton_case2 = QtWidgets.QPushButton(different_type_engrenage)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case2.setFont(font)
        self.bouton_case2.setObjectName("bouton_case2")

        self.bouton_case2.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case2, 0, 1, 1, 1)
        self.bouton_case3 = QtWidgets.QPushButton(different_type_engrenage)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case3.setFont(font)
        self.bouton_case3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bouton_case3.setObjectName("bouton_case3")

        self.bouton_case3.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case3, 1, 0, 1, 1)
        self.bouton_case4 = QtWidgets.QPushButton(different_type_engrenage)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_case4.setFont(font)
        self.bouton_case4.setObjectName("bouton_case4")

        self.bouton_case4.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.bouton_case4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.bouton_retour_ch11 = QtWidgets.QPushButton(different_type_engrenage)
        self.bouton_retour_ch11.setMinimumSize(QtCore.QSize(100, 0))
        self.bouton_retour_ch11.setMaximumSize(QtCore.QSize(180, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bouton_retour_ch11.setFont(font)
        self.bouton_retour_ch11.setObjectName("bouton_retour_ch11")

        

        self.bouton_retour_ch11.setStyleSheet("background-color: #ff557f; color: black;")
        self.verticalLayout.addWidget(self.bouton_retour_ch11, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(different_type_engrenage)
        QtCore.QMetaObject.connectSlotsByName(different_type_engrenage)

    
    def retranslateUi(self, different_type_engrenage):
        _translate = QtCore.QCoreApplication.translate
        different_type_engrenage.setWindowTitle(_translate("different_type_engrenage", "fenetre_2"))
        self.bouton_case1.setText(_translate("different_type_engrenage", "ENGRENAGES : ETUDE \n"
" GEOMETRIQUE ET\n"
"CINEMATIQUE"))
        self.bouton_case2.setText(_translate("different_type_engrenage", "ENGRENAGES : \n"
"PARALLELES \n"
"DENTURES DEPORTEES"))
        self.bouton_case3.setText(_translate("different_type_engrenage", "ENGRENAGES : \n"
" CONCOURANTS ET\n"
"GAUCHES"))
        self.bouton_case4.setText(_translate("different_type_engrenage", "ENGRENAGES : \n"
"ETUDES \n"
"DYNAMIQUES"))
        self.bouton_retour_ch11.setText(_translate("different_type_engrenage", "RETOUR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    different_type_engrenage = QtWidgets.QWidget()
    ui = Ui_different_type_engrenage()
    ui.setupUi(different_type_engrenage)
    different_type_engrenage.setMinimumSize(1080, 720)  # Définit la taille minimale de la fenêtre
    different_type_engrenage.showMaximized()  # Maximise la fenêtre pour qu'elle occupe tout l'écran
    different_type_engrenage.show()

    sys.exit(app.exec_())
