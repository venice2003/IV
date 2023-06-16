from PyQt6.QtWidgets import  QMainWindow,  QStackedWidget, QPushButton,QLineEdit,QFrame,QTextEdit,QCheckBox
from PyQt6 import uic
resetObject = "reset"
nextObject = "next"
backObject = "back"
nextEnd = "nextEnd"
formFrame ="formFrame"
files = ['./Screens/mainWindow.ui', './Screens/emergencyScreen.ui', './Screens/medicHistory.ui']
uiObjects = []
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Medical Records')
        self.setGeometry(0, 00, 1024, 768)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        # List of UI file paths

        for filePath in files:
            ui = uic.loadUi(filePath)
            uiObjects.append(ui)
            self.stacked_widget.addWidget(ui)
        for index, ui in enumerate(uiObjects):
            nextButton = ui.findChild(QPushButton, nextObject)
            if nextButton : nextButton.clicked.connect(self.next)
            print(index)
            reset_button = ui.findChild(QPushButton, resetObject)
            reset_button.clicked.connect(lambda checked, ui=ui: self.resetForm(checked,ui))
            backButton = ui.findChild(QPushButton, backObject)
            backButton.clicked.connect(self.back)
            if index ==len(uiObjects):  
                nextButton = ui.findChild(QPushButton, nextEnd)
                nextButton.clicked.connect(self.submit)
    def resetForm(self, checked, ui):
        frame = ui.findChild(QFrame, formFrame)
        if frame is not None:
            # Iterate over the child widgets of the frame
            for widget in frame.findChildren(QLineEdit) + frame.findChildren(QTextEdit) + frame.findChildren(QCheckBox):
                if isinstance(widget, QLineEdit) or isinstance(widget, QTextEdit):
                    # Clear the text of QLineEdit and QTextEdit widgets
                    widget.clear()
                if isinstance(widget, QCheckBox):
                    # Uncheck the checkboxes
                    widget.setChecked(False)
    def next(self):
        # Change the current index of the QStackedWidget
        current_index = self.stacked_widget.currentIndex()
        new_index = (current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(new_index)
    def back(self, isAdded:bool):
        # Change the current index of the QStackedWidget
        current_index = self.stacked_widget.currentIndex()
        new_index = (current_index - 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(new_index)