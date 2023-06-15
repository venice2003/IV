import PyQt6
import sys
import mysql
import mysql.connector
from PyQt6.QtWidgets import(QApplication, QWidget, QPushButton,QMainWindow, QLineEdit, QFormLayout, QLabel, QComboBox,)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Medical Records')
        self.setGeometry(800, 300, 500, 500)
        # Apply CSS style to the QPushButton (sample code)
        # self.button.setStyleSheet("""
        #     QPushButton {
        #         background-color: blue;
        #         color: white;
        #         font-size: 16px;
        #         border-radius: 5px;
        #         padding: 10px;
        #     }
            
        #     QPushButton:hover {
        #         background-color: red;
        #     }
        # """)
        # Load the image using QPixmap
        # pixmap = QPixmap("path/to/image.jpg")
        # self.image_label.setPixmap(pixmap)  
        # Set the pixmap on the label
        layout = QFormLayout()
        self.name = QLineEdit()


        layout.addRow("Enter your name:", self.name)
        self.phonenumber = QLineEdit()


        layout.addRow("Phonenumber:", self.phonenumber)
        self.birthdate = QLineEdit()

        month_combo = QComboBox()  
        layout.addRow("Month", month_combo)
        month_combo.move(150, 140)
        month_combo.addItem("JANUARY")
        month_combo.addItem("FEBUARY")
        month_combo.addItem("MARCH")
        month_combo.addItem("MAY")
        month_combo.addItem("JUNE")
        month_combo.addItem("JULY")
        month_combo.addItem("AUGUST")
        month_combo.addItem("SEPTEMBER")
        month_combo.addItem("OCTOBER")
        month_combo.addItem("NOVEMBER")
        month_combo.addItem("DECEMBER")

        year_combo = QComboBox()
        layout.addRow("Year:", year_combo)
        for year in range(2000, 2024):
            year_combo.addItem(str(year))

        day_combo = QComboBox()
        layout.addRow("Day:", day_combo)
        for day in range(1, 31):
            day_combo.addItem(str(day))

        self.address = QLineEdit()
        layout.addRow("Address:", self.address)

        self.weight = QLineEdit()
        layout.addRow("Weight:", self.weight)

        self.height = QLineEdit()
        layout.addRow("Height:", self.height)

        self.Guardians = QLineEdit()
        layout.addRow("Guardians Name:", self.Guardians)

        self.Number = QLineEdit()
        layout.addRow("Number:", self.Number)
    
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.add)
        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clear)
        layout.addWidget(add_button)
        layout.addWidget(clear_button)
        self.log = QLabel("")
        self.log.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.log.adjustSize()
        layout.addWidget(self.log)
        widgets = QWidget()

        widgets.setLayout(layout)
        self.setCentralWidget(widgets)
        add_button.clicked.connect(self.add)


    def add(self):
        # database = db()
        # database.connect(host="localhost", "root","", "medical_db")
        # database.create()
        # tableName=""
        name = self.name.text()
        medical = self.Medical.text()
        phone = self.phone.text()
        # database.create(column_names=['column1','column2','column3'],data=[name,medical,phone],tableName=tableName)

        self.log.setText(f"MedicalRecord of {name} Has been Added to Database")

    
    def clear(self):
        self.name.clear()
        self.log.clear()
        self.add()


app = QApplication(sys.argv)
x = MainWindow()
x.show()
app.exec()