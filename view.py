# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 500)
        MainWindow.setMinimumSize(QtCore.QSize(375, 500))
        MainWindow.setMaximumSize(QtCore.QSize(375, 500))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_total_students = QtWidgets.QLabel(self.centralwidget)
        self.label_total_students.setGeometry(QtCore.QRect(40, 90, 108, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_students.setFont(font)
        self.label_total_students.setObjectName("label_total_students")
        self.label_student_grades = QtWidgets.QLabel(self.centralwidget)
        self.label_student_grades.setGeometry(QtCore.QRect(40, 120, 115, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_student_grades.setFont(font)
        self.label_student_grades.setObjectName("label_student_grades")
        self.label_app = QtWidgets.QLabel(self.centralwidget)
        self.label_app.setGeometry(QtCore.QRect(100, 20, 169, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_app.setFont(font)
        self.label_app.setObjectName("label_app")
        self.input_total_students = QtWidgets.QLineEdit(self.centralwidget)
        self.input_total_students.setGeometry(QtCore.QRect(170, 90, 161, 22))
        self.input_total_students.setObjectName("input_total_students")
        self.input_student_grades = QtWidgets.QLineEdit(self.centralwidget)
        self.input_student_grades.setGeometry(QtCore.QRect(170, 120, 161, 22))
        self.input_student_grades.setObjectName("input_student_grades")
        self.button_submit_single = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit_single.setGeometry(QtCore.QRect(60, 440, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit_single.setFont(font)
        self.button_submit_single.setObjectName("button_submit_single")
        self.button_clear_single = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_single.setGeometry(QtCore.QRect(200, 440, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear_single.setFont(font)
        self.button_clear_single.setObjectName("button_clear_single")
        self.label_hidden_summary = QtWidgets.QLabel(self.centralwidget)
        self.label_hidden_summary.setGeometry(QtCore.QRect(100, 270, 152, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_hidden_summary.setFont(font)
        self.label_hidden_summary.setObjectName("label_hidden_summary")
        self.label_warning_multiple_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_warning_multiple_1.setEnabled(True)
        self.label_warning_multiple_1.setGeometry(QtCore.QRect(30, 150, 289, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning_multiple_1.setFont(font)
        self.label_warning_multiple_1.setObjectName("label_warning_multiple_1")
        self.label_saved = QtWidgets.QLabel(self.centralwidget)
        self.label_saved.setGeometry(QtCore.QRect(70, 190, 234, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_saved.setFont(font)
        self.label_saved.setObjectName("label_saved")
        self.label_saved.setStyleSheet("color: rgb(75, 181, 67)")
        self.label_student_grade = QtWidgets.QLabel(self.centralwidget)
        self.label_student_grade.setGeometry(QtCore.QRect(40, 330, 107, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_student_grade.setFont(font)
        self.label_student_grade.setObjectName("label_student_grade")
        self.input_student_grade = QtWidgets.QLineEdit(self.centralwidget)
        self.input_student_grade.setGeometry(QtCore.QRect(170, 330, 161, 22))
        self.input_student_grade.setObjectName("input_student_grade")
        self.label_highest_grade = QtWidgets.QLabel(self.centralwidget)
        self.label_highest_grade.setGeometry(QtCore.QRect(40, 300, 106, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_highest_grade.setFont(font)
        self.label_highest_grade.setObjectName("label_highest_grade")
        self.input_highest_grade = QtWidgets.QLineEdit(self.centralwidget)
        self.input_highest_grade.setGeometry(QtCore.QRect(170, 300, 161, 22))
        self.input_highest_grade.setObjectName("input_highest_grade")
        self.button_submit_multiple = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit_multiple.setGeometry(QtCore.QRect(60, 220, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit_multiple.setFont(font)
        self.button_submit_multiple.setObjectName("button_submit_multiple")
        self.button_clear_multiple = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_multiple.setGeometry(QtCore.QRect(200, 220, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear_multiple.setFont(font)
        self.button_clear_multiple.setObjectName("button_clear_multiple")
        self.label_hidden_summary_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_hidden_summary_2.setGeometry(QtCore.QRect(100, 60, 160, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_hidden_summary_2.setFont(font)
        self.label_hidden_summary_2.setObjectName("label_hidden_summary_2")
        self.label_student_grade_converted = QtWidgets.QLabel(self.centralwidget)
        self.label_student_grade_converted.setGeometry(QtCore.QRect(100, 410, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_student_grade_converted.setFont(font)
        self.label_student_grade_converted.setObjectName("label_student_grade_converted")
        self.label_student_grade_converted.setStyleSheet("color: rgb(75, 181, 67)")
        self.label_warning_single_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_warning_single_1.setEnabled(True)
        self.label_warning_single_1.setGeometry(QtCore.QRect(40, 360, 294, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning_single_1.setFont(font)
        self.label_warning_single_1.setObjectName("label_warning_single_1")
        self.label_warning_multiple_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_warning_multiple_2.setEnabled(True)
        self.label_warning_multiple_2.setGeometry(QtCore.QRect(10, 170, 345, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning_multiple_2.setFont(font)
        self.label_warning_multiple_2.setObjectName("label_warning_multiple_2")
        self.label_warning_single_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_warning_single_2.setEnabled(True)
        self.label_warning_single_2.setGeometry(QtCore.QRect(40, 380, 294, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_warning_single_2.setFont(font)
        self.label_warning_single_2.setObjectName("label_warning_single_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project 1"))
        self.label_total_students.setText(_translate("MainWindow", "Total Students"))
        self.label_student_grades.setText(_translate("MainWindow", "Student Grades"))
        self.label_app.setText(_translate("MainWindow", "Grade Calculator"))
        self.button_submit_single.setText(_translate("MainWindow", "SUBMIT"))
        self.button_clear_single.setText(_translate("MainWindow", "CLEAR"))
        self.label_hidden_summary.setText(_translate("MainWindow", "For a Single Student"))
        self.label_warning_multiple_1.setText(_translate("MainWindow", "Enter total students as single number, e.g. 5"))
        self.label_saved.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">Grades saved to grades.csv</span></p></body></html>"))
        self.label_student_grade.setText(_translate("MainWindow", "Student Grade"))
        self.label_highest_grade.setText(_translate("MainWindow", "Highest Grade"))
        self.button_submit_multiple.setText(_translate("MainWindow", "SUBMIT"))
        self.button_clear_multiple.setText(_translate("MainWindow", "CLEAR"))
        self.label_hidden_summary_2.setText(_translate("MainWindow", "For Multiple Students"))
        self.label_student_grade_converted.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55aa00;\">Student\'s Grade: A</span></p></body></html>"))
        self.label_warning_single_1.setText(_translate("MainWindow", "Enter highest grade as single number, e.g. 93"))
        self.label_warning_multiple_2.setText(_translate("MainWindow", "Enter student grades separated by space, e.g. 77 88"))
        self.label_warning_single_2.setText(_translate("MainWindow", "Enter student grade is single number, e.g. 88"))
