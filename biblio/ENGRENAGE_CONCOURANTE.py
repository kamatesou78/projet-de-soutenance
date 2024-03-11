
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ENGRENAGE_CONCOURANTE(object):
    def setupUi(self, ENGRENAGE_CONCOURANTE):
        ENGRENAGE_CONCOURANTE.setObjectName("ENGRENAGE_CONCOURANTE")
        ENGRENAGE_CONCOURANTE.resize(660, 594)
        ENGRENAGE_CONCOURANTE.setWindowModality(QtCore.Qt.WindowModal)
        ENGRENAGE_CONCOURANTE.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ENGRENAGE_CONCOURANTE.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(ENGRENAGE_CONCOURANTE)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(ENGRENAGE_CONCOURANTE)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 680, 567))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3_CH31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3_CH31.setFont(font)
        self.pushButton_3_CH31.setObjectName("pushButton_3_CH31")

        self.pushButton_3_CH31.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.pushButton_3_CH31, 2, 0, 1, 1)
        self.pushButton_5_CH31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5_CH31.setFont(font)
        self.pushButton_5_CH31.setObjectName("pushButton_5_CH31")

        self.pushButton_5_CH31.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.pushButton_5_CH31, 4, 0, 1, 1)
        self.pushButton_4_CH31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4_CH31.setFont(font)
        self.pushButton_4_CH31.setObjectName("pushButton_4_CH31")

        self.pushButton_4_CH31.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.pushButton_4_CH31, 3, 0, 1, 1)
        self.pushButton_CH31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CH31.setFont(font)
        self.pushButton_CH31.setObjectName("pushButton_CH31")
        self.gridLayout.addWidget(self.pushButton_CH31, 0, 0, 1, 1)

        self.pushButton_CH31.setStyleSheet("background-color: #00ff7f; color: black;")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.pushButton_9_CH21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9_CH21.setFont(font)
        self.pushButton_9_CH21.setObjectName("pushButton_9_CH21")

        self.pushButton_9_CH21.setStyleSheet("background-color: #ff557f; color: black;")
        self.gridLayout.addWidget(self.pushButton_9_CH21, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_2_CH31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2_CH31.setFont(font)
        self.pushButton_2_CH31.setObjectName("pushButton_2_CH31")

        self.pushButton_2_CH31.setStyleSheet("background-color: #00ff7f; color: black;")
        self.gridLayout.addWidget(self.pushButton_2_CH31, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ENGRENAGE_CONCOURANTE)
        QtCore.QMetaObject.connectSlotsByName(ENGRENAGE_CONCOURANTE)

    def retranslateUi(self, ENGRENAGE_CONCOURANTE):
        _translate = QtCore.QCoreApplication.translate
        ENGRENAGE_CONCOURANTE.setWindowTitle(_translate("ENGRENAGE_CONCOURANTE", "ENGRENAGE_CONCOURANTE"))
        self.pushButton_3_CH31.setText(_translate("ENGRENAGE_CONCOURANTE", "ENGRENAGE CONIQUE  A DENTURE HELICOIDALE\n"
" NORMALE"))
        self.pushButton_5_CH31.setText(_translate("ENGRENAGE_CONCOURANTE", "ENGRENAGE  A ROUE ET VIS\n"
" SANS FIN"))
        self.pushButton_4_CH31.setText(_translate("ENGRENAGE_CONCOURANTE", "ENGRENAGE CONIQUE  A DENTURE HELICOIDALE\n"
" DEPORTEE"))
        self.pushButton_CH31.setText(_translate("ENGRENAGE_CONCOURANTE", "ENGRENAGE CONIQUE DROIT A DENTURE\n"
" NORMALE"))
        self.pushButton_9_CH21.setText(_translate("ENGRENAGE_CONCOURANTE", "RETOUR"))
        self.pushButton_2_CH31.setText(_translate("ENGRENAGE_CONCOURANTE", "ENGRENAGE CONIQUE DROIT A DENTURE\n"
" DEPORTEE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ENGRENAGE_CONCOURANTE = QtWidgets.QWidget()
    ui = Ui_ENGRENAGE_CONCOURANTE()
    ui.setupUi(ENGRENAGE_CONCOURANTE)
    ENGRENAGE_CONCOURANTE.show()
    sys.exit(app.exec_())
