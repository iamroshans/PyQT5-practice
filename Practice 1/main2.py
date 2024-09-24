from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5 import QtWidgets
import sys
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("My first window!")

        self.setupUI()
    def setupUI(self):
        self.text=QLabel(self)
        self.text.setText("Hi this is my first code.")
        self.text.move(50,50)

        self.btn1=QtWidgets.QPushButton(self)
        self.btn1.setText("Click on me")
        self.btn1.clicked.connect(self.on_clicked)

    def on_clicked(self):
            self.text.setText("This text has been changed")
def main():
    app=QApplication(sys.argv)
    win=Ui_MainWindow()

    win.show()
    sys.exit(app.exec_())

main()