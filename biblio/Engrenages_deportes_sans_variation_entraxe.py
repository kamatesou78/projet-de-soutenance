
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SANS_VARIATION_ENTRAXE(object):
    def setupUi(self, SANS_VARIATION_ENTRAXE):
        SANS_VARIATION_ENTRAXE.setObjectName("SANS_VARIATION_ENTRAXE")
        SANS_VARIATION_ENTRAXE.resize(768, 814)

        SANS_VARIATION_ENTRAXE.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SANS_VARIATION_ENTRAXE.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(SANS_VARIATION_ENTRAXE)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(SANS_VARIATION_ENTRAXE)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 754, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_9_CH22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9_CH22.setFont(font)
        self.pushButton_9_CH22.setObjectName("pushButton_9_CH22") 

        self.pushButton_9_CH22.setStyleSheet("background-color: #ff557f; color: black;")

        self.gridLayout.addWidget(self.pushButton_9_CH22, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_2_CH22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2_CH22.setFont(font)
        self.pushButton_2_CH22.setObjectName("pushButton_2_CH22") 

        self.pushButton_2_CH22.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_2_CH22, 1, 0, 1, 1)
        self.pushButton_CH22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CH22.setFont(font)
        self.pushButton_CH22.setObjectName("pushButton_CH22") 

        self.pushButton_CH22.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_CH22, 0, 0, 1, 1)
        self.pushButton_3_CH22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_CH22.setFont(font)
        self.pushButton_3_CH22.setObjectName("pushButton_3_CH22") 

        self.pushButton_3_CH22.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_3_CH22, 2, 0, 1, 1)
        self.pushButton_4_CH22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4_CH22.setFont(font)
        self.pushButton_4_CH22.setObjectName("pushButton_4_CH22") 

        self.pushButton_4_CH22.setStyleSheet("background-color: #00ff7f; color: black;")

        self.gridLayout.addWidget(self.pushButton_4_CH22, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(SANS_VARIATION_ENTRAXE)
        QtCore.QMetaObject.connectSlotsByName(SANS_VARIATION_ENTRAXE)

    def retranslateUi(self, SANS_VARIATION_ENTRAXE):
        _translate = QtCore.QCoreApplication.translate
        SANS_VARIATION_ENTRAXE.setWindowTitle(_translate("SANS_VARIATION_ENTRAXE", "SANS_VARIATION_ENTRAXE"))
        self.pushButton_9_CH22.setText(_translate("SANS_VARIATION_ENTRAXE", "RETOUR"))
        self.pushButton_2_CH22.setText(_translate("SANS_VARIATION_ENTRAXE", "DENTURE DROITE INTERIEUR DEPORTEE"))
        self.pushButton_CH22.setText(_translate("SANS_VARIATION_ENTRAXE", "DENTURE DROITE EXTERIEUR DEPORTEE"))
        self.pushButton_3_CH22.setText(_translate("SANS_VARIATION_ENTRAXE", "DENTURE HELICOIDALE EXTERIEUR DEPORTEE"))
        self.pushButton_4_CH22.setText(_translate("SANS_VARIATION_ENTRAXE", "DENTURE HELICOIDALE INTERIEUR DEPORTEE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SANS_VARIATION_ENTRAXE = QtWidgets.QWidget()
    ui = Ui_SANS_VARIATION_ENTRAXE()
    ui.setupUi(SANS_VARIATION_ENTRAXE)
    SANS_VARIATION_ENTRAXE.show()
    sys.exit(app.exec_())
