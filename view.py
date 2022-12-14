from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(375, 235))
        MainWindow.setMaximumSize(QtCore.QSize(375, 235))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_csv_path = QtWidgets.QLabel(self.centralwidget)
        self.label_csv_path.setGeometry(QtCore.QRect(20, 90, 139, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_csv_path.setFont(font)
        self.label_csv_path.setObjectName("label_csv_path")
        self.label_app = QtWidgets.QLabel(self.centralwidget)
        self.label_app.setGeometry(QtCore.QRect(70, 20, 234, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_app.setFont(font)
        self.label_app.setObjectName("label_app")
        self.input_csv_path = QtWidgets.QLineEdit(self.centralwidget)
        self.input_csv_path.setGeometry(QtCore.QRect(170, 90, 161, 22))
        self.input_csv_path.setObjectName("input_csv_path")
        self.label_warning_multiple_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_warning_multiple_1.setEnabled(True)
        self.label_warning_multiple_1.setGeometry(QtCore.QRect(30, 110, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning_multiple_1.setFont(font)
        self.label_warning_multiple_1.setObjectName("label_warning_multiple_1")
        self.label_saved = QtWidgets.QLabel(self.centralwidget)
        self.label_saved.setGeometry(QtCore.QRect(30, 150, 303, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_saved.setFont(font)
        self.label_saved.setObjectName("label_saved")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(60, 180, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName("button_submit")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(190, 180, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.label_hint = QtWidgets.QLabel(self.centralwidget)
        self.label_hint.setGeometry(QtCore.QRect(180, 70, 127, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_hint.setFont(font)
        self.label_hint.setObjectName("label_hint")
        self.label_warning_multiple_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_warning_multiple_2.setGeometry(QtCore.QRect(30, 130, 307, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning_multiple_2.setFont(font)
        self.label_warning_multiple_2.setObjectName("label_warning_multiple_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project 1"))
        self.label_csv_path.setText(_translate("MainWindow", "Enter path to CSV: "))
        self.label_app.setText(_translate("MainWindow", "Curve Grade Calculator"))
        self.label_warning_multiple_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Couldn\'t find CSV file: place CSV in same folder</span></p></body></html>"))
        self.label_saved.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">Grades saved to curved_grades.csv</span></p></body></html>"))
        self.button_submit.setText(_translate("MainWindow", "SUBMIT"))
        self.button_clear.setText(_translate("MainWindow", "CLEAR"))
        self.label_hint.setText(_translate("MainWindow", "Student\'s Grades"))
        self.label_warning_multiple_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">CSV format should be name,grade: e.g. John,93</span></p></body></html>"))