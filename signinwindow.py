from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox,QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
from gamewindow import Ui_MainWindow
class SignalSenter(QtCore.QObject):
    show_reg = QtCore.pyqtSignal()
class SignWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # self.setupUi(self)
        # self.retranslateUi(self)
        # self.hide_status = 0 
        # self.pushButton.clicked.connect(self.clicked_btn)
        # self.db.connection()
        # self.signin_btn.clicked.connect(self.get_to_base)
    # def get_to_base(self):
    #     self.us = User(email=self.lineEdit.text(),passw=self.lineEdit_2.text())
    #     if self.us.get_base(self.db):
    #         md = QMediaPlayer(self)
    #         out = QAudioOutput(self)
    #         out.setVolume(50)
    #         md.setAudioOutput(out)
    #         md.setSource(QtCore.QUrl("audio/click.mp3"))
    #         md.play()
    #         QMessageBox.about(self,"Info","Hammasi joyida")
    #     else:
    #         QMessageBox.about(self,"Info","Email topilmadi")
        self.game = Ui_MainWindow()
        self.setupUi(self)
        self.retranslateUi(self)
        self.res_signal= SignalSenter()
        # self.pushButton_2.clicked.connect(self.cancel_btn_clicked)
        self.signin_btn.clicked.connect(self.sign)
    def cancel_btn_clicked(self):
        self.res_signal.show_reg.emit()

        self.close()

    def sign(self):
        email = self.lineEdit.text()
        pas = self.lineEdit_2.text()
        
        s=True
        for i in open("pass.txt","r").readlines():
            if(i.split()[0]==email and i.split()[1]==pas):
                self.game.show()
                self.hide()
                s=False
        if s:
            QtWidgets.QMessageBox.about(self,"Xato","Siz ro'yxatdan o'tmagansiz!")
    def clicked_btn(self):
        if self.hide_status == 0:
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.hide_status = 1
            self.pushButton.setIcon(QIcon("img/hide.png"))
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
            self.hide_status = 0
            self.pushButton.setIcon(QIcon("img/view.png"))            
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 408)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(700, 408))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(120, 120))
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/padlock.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_mail = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_mail.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_mail.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lbl_mail.setText("")
        self.lbl_mail.setPixmap(QtGui.QPixmap("img/gmail.png"))
        self.lbl_mail.setScaledContents(True)
        self.lbl_mail.setObjectName("lbl_mail")
        self.gridLayout.addWidget(self.lbl_mail, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lbl_mail_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_mail_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_mail_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lbl_mail_2.setText("")
        self.lbl_mail_2.setPixmap(QtGui.QPixmap("img/password.png"))
        self.lbl_mail_2.setScaledContents(True)
        self.lbl_mail_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_mail_2.setObjectName("lbl_mail_2")
        self.gridLayout.addWidget(self.lbl_mail_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 25))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signin_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signin_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.signin_btn.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"    background-color: rgb(85, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    width:45px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/signin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.signin_btn.setIcon(icon2)
        self.signin_btn.setObjectName("signin_btn")
        self.horizontalLayout.addWidget(self.signin_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.signup_btn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signup_btn_2.setMinimumSize(QtCore.QSize(0, 40))
        self.signup_btn_2.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"    background-color: rgb(85, 85, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    width:45px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.signup_btn_2.setIcon(icon3)
        self.signup_btn_2.setObjectName("signup_btn_2")
        self.horizontalLayout.addWidget(self.signup_btn_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign In"))
        MainWindow.setToolTip(_translate("MainWindow", "Bu asosiy oyna"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "example@gmail.com"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "*********"))
        self.checkBox.setText(_translate("MainWindow", "Remember me"))
        self.signin_btn.setText(_translate("MainWindow", "Sign In"))
        self.signup_btn_2.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sg = SignWindow()
    sg.show()
    app.exec()
