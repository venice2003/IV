from PyQt6.QtCore import Qt,QEvent,QObject
from PyQt6.QtWidgets import  QMainWindow,  QStackedWidget, QPushButton,QLineEdit,QFrame,QTextEdit,QApplication
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Medical Records')
        self.setGeometry(800, 300, 500, 500)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Load the UI files
        self.firstUI = uic.loadUi('./Screens/mainWindow.ui')
        self.secondUI = uic.loadUi('./Screens/emergencyScreen.ui')

        # Add the UI files to the stacked widget
        self.stacked_widget.addWidget(self.firstUI)
        self.stacked_widget.addWidget(self.secondUI)

        nextButton = self.firstUI.findChild(QPushButton, 'welcomeNext')
        nextButton.clicked.connect(self.next)

        backButton = self.secondUI.findChild(QPushButton, 'consultBack')
        backButton.clicked.connect(self.back)

        reset_button = self.firstUI.findChild(QPushButton, 'resetButton')
        reset_button1 = self.secondUI.findChild(QPushButton, 'resetButton')
        reset_button.clicked.connect(lambda: self.resetForm("welcomeForm"))
        reset_button1.clicked.connect(lambda: self.resetForm("consultForm"))


        # Connect the clicked signal of the reset button to the reset_form function
    def resetForm(self,frameName):
        print(frameName)
        # Find the frame in the UI
        frame = self.findChild(QFrame, frameName)

        if frame is not None:
            # Iterate over the child widgets of the frame
            for widget in frame.findChildren(QLineEdit)+frame.findChildren(QTextEdit):
                if isinstance(widget, QLineEdit):
                    # Clear the text of QLineEdit widgets
                    widget.clear()
                if isinstance(widget, QTextEdit):
                    # Clear the text of QLineEdit widgets
                    widget.clear()
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