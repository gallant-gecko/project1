from PyQt5.QtWidgets import *
from view import *
import csv
import os.path

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
        self.hide_success_multiple()
        self.button_submit.clicked.connect(self.submit)
        self.button_clear.clicked.connect(self.clear_multiple_inputs)

    def submit(self):
        """
        Function to submit input data found in multiple student calculation
        """
        self.hide_error_multiple()
        self.hide_success_multiple()
        try:
            file = open(f'{self.input_csv_path.text()}', 'r')
        except FileNotFoundError:
            self.label_warning_multiple_1.setHidden(False)
        else:
            try:
                highest_grade, data = self.parse_csv(file)
            except ValueError:
                self.label_warning_multiple_2.setHidden(False)
            else:
                self.output_csv(highest_grade, data)

    def display_success_multiple(self):
        """
        Function to reveal success message for multiple student calculation
        """
        self.label_saved.setStyleSheet("color: rgb(75, 181, 67);")
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
    
    def clear_multiple_inputs(self):
        """
        Function to clear input data, and hide errors and success message for multiple student calculation
        """
        self.hide_error_multiple()
        self.hide_success_multiple()
        self.input_csv_path.setText("")
    
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

    # def get_output_file_name(self):
    #     output_file_name = input("Output file name: ").strip()
        
    #     while os.path.isfile(f'files/{output_file_name}'):
    #         decision = input("Overwrite existing file (y/n): ").strip().lower()
    #         while decision != 'y' and decision != 'n':
    #             decision = input("Enter (y/n): ").strip().lower()

    #         if decision == 'y':
    #             return output_file_name

    #         if decision == 'n':
    #             output_file_name = input("New output file name: ").strip()

    #     return output_file_name

    def parse_csv(self, file):
        """
        Function to parse input csv and return highest grade found and each line in CSV file located in same location as main.py
        :param file: opened csv file
        :return: float, list
        """
        highest_grade = 0.
        data = []
        for line in file:
            data.append(line.strip())
            line = line.strip().split(',')
            current_grade = float(line[1])
            if current_grade  > highest_grade:
                highest_grade = float(line[1])
        file.close()
        return highest_grade, data

    def output_csv(self, highest_grade, data):
        
        with open(f'curved_grades.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Student', 'Grade', 'Curved Grade'])
            for line in data:
                line = line.strip().split(',')
                student = line[0]
                grade = float(line[1])
                csv_writer.writerow([student, grade, self.grade_conversion(highest_grade, grade)])
        self.clear_multiple_inputs()
        self.display_success_multiple()