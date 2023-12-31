# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from gamewindow import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLineEdit
from aiogram import*
from asyncio import run
from aiogram.types import Message
from aiogram.filters.command import Command


class SignalSenter(QtCore.QObject):
    show_reg = QtCore.pyqtSignal()
class RegistrWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.game = Ui_MainWindow()
        self.setupUi(self)
        self.retranslateUi(self)
        self.sg = SignalSenter()
        self.pushButton_2.clicked.connect(self.back_clic)
    
    def back_clic(self):
        self.sg.show_reg.emit()
        self.close()

    def closeEvent(self,a0:QtGui.QCloseEvent)->None:
        ans = QtWidgets.QMessageBox.question(self,"Savol?","Chiqmoqchimisiz?",
                                             QtWidgets.QMessageBox.StandardButton.Yes|
                                             QtWidgets.QMessageBox.StandardButton.No)
        if ans == QtWidgets.QMessageBox.StandardButton.No:
            self.sg.show_reg.emit()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Sign Up")
        
        MainWindow.resize(539, 490)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_3 = QtWidgets.QGridLayout(parent=self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.setWindowIcon(QtGui.QIcon("img/add.png"))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.clicked.connect(self.e_s)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)


        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)

        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)

        



        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        


        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 223, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.telez_id)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Uzbekistan"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Russia"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Kazakistan"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Kirgizistan"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Tadjikistan"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Turkmanistan"))
        self.comboBox.setItemText(6, _translate("MainWindow", "America"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Saudia Arabiston"))
        self.comboBox.setItemText(8, _translate("MainWindow", "China"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Alex"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "********"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "example@gmail.com"))
        self.label_4.setText(_translate("MainWindow", "Mobile Number:"))
        self.lineEdit_4.setInputMask(_translate("MainWindow", "\\+\\9\\9\\8-99-999-99-99"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Country:"))
        self.label_6.setText(_translate("MainWindow", "Telegram ID:"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Your telegram ID"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))

    def e_s(self):
        if str(self.lineEdit_3.echoMode()) == "EchoMode.Normal":
            self.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Password)
            self.pushButton_3.setIcon(QtGui.QIcon("img/view.png"))
            
        else:
            self.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Normal)
            self.pushButton_3.setIcon(QtGui.QIcon("img/hide.png"))
    

    def telez_id(self):
            import requests
            chatid = self.lineEdit_5.text()
            token = "6071644424:AAGlecwnLQCqZFn-nOysBVjMg46ty5kY0Ns"
            url = f'https://api.telegram.org/bot{token}/sendMessage'
            data = {'chat_id': chatid, 'text': f"""📜You are signed up on Our platform
    Your email: {self.lineEdit_2.text()}
    Your password: {self.lineEdit_3.text()}"""}
            if requests.post(url, data).json()["ok"]==False:
        
                QtWidgets.QMessageBox.about(self,"Xato","Siz botga start bermagansiz!")
            else:
                open("pass.txt","a").write(f"{self.lineEdit_2.text()} {self.lineEdit_3.text()}\n")
                QtWidgets.QMessageBox.about(self,"yes","Siz ro'yxatdan o'tdingiz!")
                self.game.show()
                self.hide()

# if __name__=="__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     sig = RegistrWindow()
#     gm = Ui_MainWindow()
#     sig.show()

#     app.exec()