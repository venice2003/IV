from PyQt6.QtWidgets import QApplication
from startScreen import startWindow
app = QApplication([])
window = startWindow()
window.show()
app.exec()
