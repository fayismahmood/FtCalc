# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 405)
        MainWindow.setMinimumSize(QtCore.QSize(260, 405))
        MainWindow.setMaximumSize(QtCore.QSize(260, 405))
        MainWindow.setStyleSheet("#centralwidget{\n"
"background:#2e262f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Dis = QtWidgets.QLineEdit(self.centralwidget)
        self.Dis.setGeometry(QtCore.QRect(0, 0, 261, 51))
        self.Dis.setStyleSheet("#Dis{\n"
"    padding:10px;\n"
"    width:100%;\n"
"    border:red solid 1px;\n"
"    font-size:30px;\n"
"    background:#433b44;\n"
"    color:white;\n"
"}")
        self.Dis.setObjectName("Dis")
        self.Nums_2 = QtWidgets.QFrame(self.centralwidget)
        self.Nums_2.setGeometry(QtCore.QRect(10, 70, 231, 221))
        self.Nums_2.setStyleSheet("#Nums_2 QPushButton{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:white;\n"
"    border:2px solid white; \n"
"    font-size:20px;\n"
"}\n"
"#Nums_2 QPushButton:hover{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:#2e262f;\n"
"    background-color:white;\n"
"    font-size:20px;\n"
"    transition:3s;\n"
"}\n"
"\n"
"")
        self.Nums_2.setObjectName("Nums_2")
        self.Nums = QtWidgets.QGridLayout(self.Nums_2)
        self.Nums.setContentsMargins(0, 0, 0, 0)
        self.Nums.setSpacing(6)
        self.Nums.setObjectName("Nums")
        self.pushButton_6 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.Nums.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton.setObjectName("pushButton")
        self.Nums.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.Nums.addWidget(self.pushButton_10, 0, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.Nums.addWidget(self.pushButton_13, 3, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.Nums.addWidget(self.pushButton_15, 3, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.Nums.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_11.setObjectName("pushButton_11")
        self.Nums.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.Nums.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.Nums.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.Nums.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Nums.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.Nums.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.Nums.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.Nums.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.Nums.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.Nums_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.Nums.addWidget(self.pushButton_14, 3, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 310, 111, 41))
        self.pushButton_17.setStyleSheet(" QPushButton{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:white;\n"
"    border:2px solid white; \n"
"    font-size:20px;\n"
"}\n"
" QPushButton:hover{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:#2e262f;\n"
"    background-color:white;\n"
"    font-size:20px;\n"
"    transition:3s;\n"
"}\n"
"\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(130, 310, 53, 41))
        self.pushButton_18.setStyleSheet(" QPushButton{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:white;\n"
"    border:2px solid white; \n"
"    font-size:20px;\n"
"} QPushButton:hover{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:#2e262f;\n"
"    background-color:white;\n"
"    font-size:20px;\n"
"    transition:3s;\n"
"}\n"
"\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(190, 310, 51, 41))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:white;\n"
"    border:2px solid white; \n"
"    font-size:20px;\n"
"}\n"
" QPushButton:hover{\n"
"    width:50px;\n"
"    height:50px;\n"
"    border-radius:10px;\n"
"    color:#2e262f;\n"
"    background-color:white;\n"
"    font-size:20px;\n"
"    transition:3s;\n"
"}\n"
"\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Dis.setText(_translate("MainWindow", "488"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_10.setText(_translate("MainWindow", "CE"))
        self.pushButton_13.setText(_translate("MainWindow", "0"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_11.setText(_translate("MainWindow", "+"))
        self.pushButton_12.setText(_translate("MainWindow", "-"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_16.setText(_translate("MainWindow", "X"))
        self.pushButton_2.setText(_translate("MainWindow", "3"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setText(_translate("MainWindow", "1"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_14.setText(_translate("MainWindow", "%"))
        self.pushButton_17.setText(_translate("MainWindow", "="))
        self.pushButton_18.setText(_translate("MainWindow", "/"))
        self.pushButton_19.setText(_translate("MainWindow", "/"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
