
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LES_EFFORTS_SUR_DENTS(object):
    def setupUi(self, LES_EFFORTS_SUR_DENTS):
        LES_EFFORTS_SUR_DENTS.setObjectName("LES_EFFORTS_SUR_DENTS")
        LES_EFFORTS_SUR_DENTS.resize(660, 594)

        LES_EFFORTS_SUR_DENTS.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LES_EFFORTS_SUR_DENTS.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(LES_EFFORTS_SUR_DENTS)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(LES_EFFORTS_SUR_DENTS)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 814, 567))
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

        self.pushButton_EFFORTS_DROITE.setStyleSheet("background-color: #00ff7f; color: black;")

        self.pushButton_EFFORTS_DROITE.setObjectName("pushButton_EFFORTS_DROITE")
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

        self.pushButton_EFFORTS_CONCOURANT.setStyleSheet("background-color: #00ff7f; color: black;")

        self.pushButton_EFFORTS_CONCOURANT.setObjectName("pushButton_EFFORTS_CONCOURANT")
        self.gridLayout.addWidget(self.pushButton_EFFORTS_CONCOURANT, 2, 0, 1, 1)
        self.pushButton_EFFORTS_ROUE_VIS = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS_ROUE_VIS.setFont(font)

        self.pushButton_EFFORTS_ROUE_VIS.setStyleSheet("background-color: #00ff7f; color: black;")

        self.pushButton_EFFORTS_ROUE_VIS.setObjectName("pushButton_EFFORTS_ROUE_VIS")
        self.gridLayout.addWidget(self.pushButton_EFFORTS_ROUE_VIS, 3, 0, 1, 1)
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setFont(font)

        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setStyleSheet("background-color: #ff557f; color: black;")
        
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setObjectName("pushButton_RETOUR_EFFORTS_SUR_DENTS")
        self.gridLayout.addWidget(self.pushButton_RETOUR_EFFORTS_SUR_DENTS, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_EFFORTS_HELICOIDALE = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS_HELICOIDALE.setFont(font)

        self.pushButton_EFFORTS_HELICOIDALE.setStyleSheet("background-color: #00ff7f; color: black;")

        self.pushButton_EFFORTS_HELICOIDALE.setObjectName("pushButton_EFFORTS_HELICOIDALE")
        self.gridLayout.addWidget(self.pushButton_EFFORTS_HELICOIDALE, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(LES_EFFORTS_SUR_DENTS)
        QtCore.QMetaObject.connectSlotsByName(LES_EFFORTS_SUR_DENTS)

    def retranslateUi(self, LES_EFFORTS_SUR_DENTS):
        _translate = QtCore.QCoreApplication.translate
        LES_EFFORTS_SUR_DENTS.setWindowTitle(_translate("LES_EFFORTS_SUR_DENTS", "LES_EFFORTS_SUR_DENTS"))
        self.pushButton_EFFORTS_DROITE.setText(_translate("LES_EFFORTS_SUR_DENTS", "CALCUL DES EFFORTS SUR LES ENGRENAGES PARALLELES\n"
"  A DENTURE DROITE"))
        self.pushButton_EFFORTS_CONCOURANT.setText(_translate("LES_EFFORTS_SUR_DENTS", "CALCUL DES EFFORTS SUR LES ENGRENAGES CONIQUES\n"
"  OU AXES CONCOURANTS"))
        self.pushButton_EFFORTS_ROUE_VIS.setText(_translate("LES_EFFORTS_SUR_DENTS", "CALCUL DES EFFORTS SUR LES ENGRENAGES A \n"
" ROUE ET VIS SANS FIN"))
        self.pushButton_RETOUR_EFFORTS_SUR_DENTS.setText(_translate("LES_EFFORTS_SUR_DENTS", "RETOUR"))
        self.pushButton_EFFORTS_HELICOIDALE.setText(_translate("LES_EFFORTS_SUR_DENTS", "CALCUL DES EFFORTS SUR LES ENGRENAGES PARALLELES\n"
"  A DENTURE HELICOIDALE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LES_EFFORTS_SUR_DENTS = QtWidgets.QWidget()
    ui = Ui_LES_EFFORTS_SUR_DENTS()
    ui.setupUi(LES_EFFORTS_SUR_DENTS)
    LES_EFFORTS_SUR_DENTS.show()
    sys.exit(app.exec_())
