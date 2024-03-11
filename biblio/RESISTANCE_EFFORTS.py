
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RESISTANCE_EFFORT(object):
    def setupUi(self, RESISTANCE_EFFORT):
        RESISTANCE_EFFORT.setObjectName("RESISTANCE_EFFORT")
        RESISTANCE_EFFORT.resize(730, 343)

        RESISTANCE_EFFORT.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RESISTANCE_EFFORT.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(RESISTANCE_EFFORT)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_EFFORTS = QtWidgets.QPushButton(RESISTANCE_EFFORT)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_EFFORTS.setFont(font)
        self.pushButton_EFFORTS.setObjectName("pushButton_EFFORTS")

        self.pushButton_EFFORTS.setStyleSheet("background-color: #00ff7f; color: black;")
        self.verticalLayout.addWidget(self.pushButton_EFFORTS, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_RESISTANCE = QtWidgets.QPushButton(RESISTANCE_EFFORT)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_RESISTANCE.setFont(font)
        self.pushButton_RESISTANCE.setObjectName("pushButton_RESISTANCE")

        self.pushButton_RESISTANCE.setStyleSheet("background-color: #00ff7f; color: black;")
        self.verticalLayout.addWidget(self.pushButton_RESISTANCE, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.RETOUR_RESISTRANCE_EFFORTS = QtWidgets.QPushButton(RESISTANCE_EFFORT)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RETOUR_RESISTRANCE_EFFORTS.setFont(font)
        self.RETOUR_RESISTRANCE_EFFORTS.setObjectName("RETOUR_RESISTRANCE_EFFORTS")

        self.RETOUR_RESISTRANCE_EFFORTS.setStyleSheet("background-color: #ff557f; color: black;")
        self.verticalLayout.addWidget(self.RETOUR_RESISTRANCE_EFFORTS, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(RESISTANCE_EFFORT)
        QtCore.QMetaObject.connectSlotsByName(RESISTANCE_EFFORT)

    def retranslateUi(self, RESISTANCE_EFFORT):
        _translate = QtCore.QCoreApplication.translate
        RESISTANCE_EFFORT.setWindowTitle(_translate("RESISTANCE_EFFORT", "CALCUL RESISTANCE-EFFORTS"))
        self.pushButton_EFFORTS.setText(_translate("RESISTANCE_EFFORT", "DETERMINATION DES CHARGES (EFFORTS) \n"
"SUR LES DENTS"))
        self.pushButton_RESISTANCE.setText(_translate("RESISTANCE_EFFORT", "CALCUL DE RESISTANCE DES ENGRENAGES \n"
"PARALLELES"))
        self.RETOUR_RESISTRANCE_EFFORTS.setText(_translate("RESISTANCE_EFFORT", "RETOUR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RESISTANCE_EFFORT = QtWidgets.QWidget()
    ui = Ui_RESISTANCE_EFFORT()
    ui.setupUi(RESISTANCE_EFFORT)
    RESISTANCE_EFFORT.show()
    sys.exit(app.exec_())
