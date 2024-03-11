
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ENGRENAGES_DEPORTEES(object):
    def setupUi(self, ENGRENAGES_DEPORTEES):
        ENGRENAGES_DEPORTEES.setObjectName("ENGRENAGES_DEPORTEES")
        ENGRENAGES_DEPORTEES.resize(697, 396)

        ENGRENAGES_DEPORTEES.setWindowModality(QtCore.Qt.WindowModal)
        ENGRENAGES_DEPORTEES.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ENGRENAGES_DEPORTEES.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(ENGRENAGES_DEPORTEES)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(ENGRENAGES_DEPORTEES)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 874, 369))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2_CH20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2_CH20.setFont(font)
        self.pushButton_2_CH20.setObjectName("pushButton_2_CH20")

        self.pushButton_2_CH20.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout_2.addWidget(self.pushButton_2_CH20, 0, 0, 1, 1)
        self.pushButton_CH20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CH20.setFont(font)
        self.pushButton_CH20.setObjectName("pushButton_CH20")

        self.pushButton_CH20.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout_2.addWidget(self.pushButton_CH20, 0, 1, 1, 1)
        self.pushButton_4_CH20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4_CH20.setFont(font)
        self.pushButton_4_CH20.setObjectName("pushButton_4_CH20")

        self.pushButton_4_CH20.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout_2.addWidget(self.pushButton_4_CH20, 1, 0, 1, 1)
        self.pushButton_3_CH20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_CH20.setFont(font)
        self.pushButton_3_CH20.setObjectName("pushButton_3_CH20")

        self.pushButton_3_CH20.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout_2.addWidget(self.pushButton_3_CH20, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_5_CH20 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5_CH20.setFont(font)
        self.pushButton_5_CH20.setObjectName("pushButton_5_CH20")

        self.pushButton_5_CH20.setStyleSheet("background-color: #ff557f; color: black;")
        self.verticalLayout.addWidget(self.pushButton_5_CH20, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ENGRENAGES_DEPORTEES)
        QtCore.QMetaObject.connectSlotsByName(ENGRENAGES_DEPORTEES)

    def retranslateUi(self, ENGRENAGES_DEPORTEES):
        _translate = QtCore.QCoreApplication.translate
        ENGRENAGES_DEPORTEES.setWindowTitle(_translate("ENGRENAGES_DEPORTEES", "ENGRENAGES DEPORTEES"))
        self.pushButton_2_CH20.setText(_translate("ENGRENAGES_DEPORTEES", "DETERMINATION DES DEPORTS\n"
" SANS VARIATION D\'ENTRAXE"))
        self.pushButton_CH20.setText(_translate("ENGRENAGES_DEPORTEES", "DETERMINATION DES DEPORTS\n"
" AVEC VARIATION D\'ENTRAXE"))
        self.pushButton_4_CH20.setText(_translate("ENGRENAGES_DEPORTEES", "ENGRENAGE DEPORTE\n"
" SANS VARIATION D\'ENTRAXE"))
        self.pushButton_3_CH20.setText(_translate("ENGRENAGES_DEPORTEES", "ENGRENAGE DEPORTE\n"
" AVEC VARIATION D\'ENTRAXE"))
        self.pushButton_5_CH20.setText(_translate("ENGRENAGES_DEPORTEES", "RETOUR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ENGRENAGES_DEPORTEES = QtWidgets.QWidget()
    ui = Ui_ENGRENAGES_DEPORTEES()
    ui.setupUi(ENGRENAGES_DEPORTEES)
    ENGRENAGES_DEPORTEES.show()
    sys.exit(app.exec_())
