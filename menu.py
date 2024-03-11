
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_LOGICIEL_DE_CALCUL(object):
    def setupUi(self, LOGICIEL_DE_CALCUL):
        LOGICIEL_DE_CALCUL.setObjectName("LOGICIEL_DE_CALCUL")
        LOGICIEL_DE_CALCUL.resize(709, 454)
        LOGICIEL_DE_CALCUL.setMinimumSize(QtCore.QSize(709, 454))
        LOGICIEL_DE_CALCUL.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        #############################################################
        LOGICIEL_DE_CALCUL.setStyleSheet("background-color: #00aaff;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../reducteur_gearexpert.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LOGICIEL_DE_CALCUL.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LOGICIEL_DE_CALCUL)
        self.centralwidget.setObjectName("centralwidget")

        ###########################################################
        #self.centralwidget.setStyleSheet("background-color: blue;")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        ################################################
        self.pushButton_2.setStyleSheet("background-color: #ff557f; color: white;")

        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        ###############################################################################
        self.pushButton.setStyleSheet("background-color: #00ff7f; color: white;")

        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(900, 700))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../reducteur_gearexpert.gif"))

        gif_path = r"C:\Users\HD\Desktop\PFE\INTERFACE\reducteur_gearexpert.gif"  # Remplace avec ton chemin complet vers ton image GIF
        movie = QMovie(gif_path)
        self.label_2.setMovie(movie)
        movie.start()

        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        ############################################
        self.label.setStyleSheet("color: #4c0000;")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_3.setStyleSheet("color: yellow;")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        LOGICIEL_DE_CALCUL.setCentralWidget(self.centralwidget)

        self.retranslateUi(LOGICIEL_DE_CALCUL)
        QtCore.QMetaObject.connectSlotsByName(LOGICIEL_DE_CALCUL)

    def retranslateUi(self, LOGICIEL_DE_CALCUL):
        _translate = QtCore.QCoreApplication.translate
        LOGICIEL_DE_CALCUL.setWindowTitle(_translate("LOGICIEL_DE_CALCUL", "LOGICIEL DE CALCUL D\'ENGRENAGE"))
        self.pushButton_2.setText(_translate("LOGICIEL_DE_CALCUL", "Cliquez ici pour quitter le logiciel"))
        self.pushButton.setText(_translate("LOGICIEL_DE_CALCUL", "Cliquez ici pour commencer les calculs"))
        self.label.setText(_translate("LOGICIEL_DE_CALCUL", "BIENVENUE SUR LE LOGICIEL DE CALCUL D\'ENGRENAGE"))
        self.label_3.setText(_translate("LOGICIEL_DE_CALCUL", "GEAR-MASTER"))



