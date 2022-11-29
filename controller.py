from PyQt5.QtWidgets import *
from view import *
import csv

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Function to initialize GUI with default values
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.hide_error_multiple()
        self.hide_error_single()
        self.hide_success_multiple()
        self.hide_success_single()
        self.button_submit_multiple.clicked.connect(self.submit_multiple)
        self.button_clear_multiple.clicked.connect(self.clear_multiple_inputs)
        self.button_submit_single.clicked.connect(self.submit_single)
        self.button_clear_single.clicked.connect(self.clear_single_inputs)

    def submit_multiple(self):
        """
        Function to submit input data found in multiple student calculation
        """
        self.hide_error_multiple()
        self.hide_success_multiple()
        self.calculate_multiple()
    
    def submit_single(self):
        """
        Function to submit input data found in single student calculation
        """
        self.hide_error_single()
        self.hide_success_single()
        self.calculate_single()

    def calculate_single(self):
        """
        Function to calculate single student curved grade and display to GUI
        """
        try:
            highest_grade = int(self.input_highest_grade.text())
            student_grade = int(self.input_student_grade.text())
        except:
            self.display_error_single()
        else:
            self.hide_error_single()
            self.label_student_grade_converted.setText(f"Student's Grade: {self.grade_conversion(highest_grade, student_grade)}")
            self.display_success_single()
    
    def calculate_multiple(self):
        """
        Function to calculate multiple students curved grades and write results to grades.csv
        """
        try:
            total_students = int(self.input_total_students.text())
            grades = [int(grade) for grade in self.input_student_grades.text().split()]
            while len(grades) > total_students:
                grades.pop()
            best_grade = int(max(grades))
        except:
            self.display_error_multiple()
        else:
            self.hide_error_multiple()
            with open('grades.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["student", "grade", "curved_grade"])
                for student, grade in enumerate(grades):
                    csv_writer.writerow(["student "+str(student+1), grade, self.grade_conversion(best_grade, grade)])
            self.display_success_multiple()
        
    def display_success_multiple(self):
        """
        Function to reveal success message for multiple student calculation
        """
        self.label_saved.setHidden(False)
    
    def hide_success_multiple(self):
        """
        Function to hide success message for multiple student calculation
        """
        self.label_saved.setHidden(True)

    def display_error_multiple(self):
        """
        Function to display error messages for multiple student calculation
        """
        self.label_warning_multiple_1.setHidden(False)
        self.label_warning_multiple_2.setHidden(False)
    
    def hide_error_multiple(self):
        """
        Function to hide error messages for multiple student calculation
        """
        self.label_warning_multiple_1.setHidden(True)
        self.label_warning_multiple_2.setHidden(True)

    def display_success_single(self):
        """
        Function to display converted numerical grade for single student calculation
        """
        self.label_student_grade_converted.setHidden(False)
    
    def hide_success_single(self):
        """
        Function to hide converted numerical grade for single student calculation
        """
        self.label_student_grade_converted.setHidden(True)

    def display_error_single(self):
        """
        Function to display error message for single student calculation
        """
        self.label_warning_single_1.setHidden(False)
        self.label_warning_single_2.setHidden(False)

    def hide_error_single(self):
        """
        Function to hide error message for single student calculation
        """
        self.label_warning_single_1.setHidden(True)
        self.label_warning_single_2.setHidden(True)

    def clear_single_inputs(self):
        """
        Function to clear input data from single student calculation
        """
        self.hide_error_single()
        self.hide_success_single()
        self.input_highest_grade.setText("")
        self.input_student_grade.setText("")
    
    def clear_multiple_inputs(self):
        """
        Function to clear input data, and hide errors and success message for multiple student calculation
        """
        self.hide_error_multiple()
        self.hide_success_multiple()
        self.input_total_students.setText("")
        self.input_student_grades.setText("")
    
    def grade_conversion(self, highest_grade, grade):
        """
        Function to convert numerical grade to letter grade
        :param highest_grade: highest grade for class
        :param grade: grade for current student
        :return: string
        """
        if grade >= highest_grade - 10:
            return "A"
        if grade >= highest_grade - 20:
            return "B"
        if grade >= highest_grade - 30:
            return "C"
        if grade >= highest_grade - 40:
            return "D"
        else:
            return "F"