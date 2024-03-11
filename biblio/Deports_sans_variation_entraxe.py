


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DEPORTS_SANS_VARIATION_ENTRAXE(object):
    def setupUi(self, DEPORTS_SANS_VARIATION_ENTRAXE):
        DEPORTS_SANS_VARIATION_ENTRAXE.setObjectName("DEPORTS_SANS_VARIATION_ENTRAXE")
        DEPORTS_SANS_VARIATION_ENTRAXE.resize(643, 300)

        DEPORTS_SANS_VARIATION_ENTRAXE.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DEPORTS_SANS_VARIATION_ENTRAXE.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DEPORTS_SANS_VARIATION_ENTRAXE)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3_SANS_VARIATION = QtWidgets.QPushButton(DEPORTS_SANS_VARIATION_ENTRAXE)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_SANS_VARIATION.setFont(font)
        self.pushButton_3_SANS_VARIATION.setObjectName("pushButton_3_SANS_VARIATION")

        self.pushButton_3_SANS_VARIATION.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_3_SANS_VARIATION, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_SANS_VARIATION = QtWidgets.QPushButton(DEPORTS_SANS_VARIATION_ENTRAXE)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SANS_VARIATION.setFont(font)
        self.pushButton_SANS_VARIATION.setObjectName("pushButton_SANS_VARIATION")

        self.pushButton_SANS_VARIATION.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_SANS_VARIATION, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_2_SANS_VARIATION = QtWidgets.QPushButton(DEPORTS_SANS_VARIATION_ENTRAXE)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2_SANS_VARIATION.setFont(font)
        self.pushButton_2_SANS_VARIATION.setObjectName("pushButton_2_SANS_VARIATION")

        self.pushButton_2_SANS_VARIATION.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_2_SANS_VARIATION, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_4_SANS_VARIATION = QtWidgets.QPushButton(DEPORTS_SANS_VARIATION_ENTRAXE)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4_SANS_VARIATION.setFont(font)
        self.pushButton_4_SANS_VARIATION.setObjectName("pushButton_4_SANS_VARIATION")

        self.pushButton_4_SANS_VARIATION.setStyleSheet("background-color: #ff557f; color: black;")

        self.gridLayout.addWidget(self.pushButton_4_SANS_VARIATION, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(DEPORTS_SANS_VARIATION_ENTRAXE)
        QtCore.QMetaObject.connectSlotsByName(DEPORTS_SANS_VARIATION_ENTRAXE)

    def retranslateUi(self, DEPORTS_SANS_VARIATION_ENTRAXE):
        _translate = QtCore.QCoreApplication.translate
        DEPORTS_SANS_VARIATION_ENTRAXE.setWindowTitle(_translate("DEPORTS_SANS_VARIATION_ENTRAXE", "DEPORTS SANS VARIATION D\'ENTRAXE"))
        self.pushButton_3_SANS_VARIATION.setText(_translate("DEPORTS_SANS_VARIATION_ENTRAXE", "METHODE DE MAAG-TASCHENBUCH"))
        self.pushButton_SANS_VARIATION.setText(_translate("DEPORTS_SANS_VARIATION_ENTRAXE", "METHODE ISO"))
        self.pushButton_2_SANS_VARIATION.setText(_translate("DEPORTS_SANS_VARIATION_ENTRAXE", "METHODE DE W.RICHTER"))
        self.pushButton_4_SANS_VARIATION.setText(_translate("DEPORTS_SANS_VARIATION_ENTRAXE", "RETOUR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DEPORTS_SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
    ui = Ui_DEPORTS_SANS_VARIATION_ENTRAXE()
    ui.setupUi(DEPORTS_SANS_VARIATION_ENTRAXE)
    DEPORTS_SANS_VARIATION_ENTRAXE.show()
    sys.exit(app.exec_())
