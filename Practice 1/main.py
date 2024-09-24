from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
from PyQt5 import QtWidgets
def on_clicked():
    print("Pressed")
def main():
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setGeometry(100,200,300,300)
    window.setWindowTitle("My first window")

    text=QLabel(window)
    text.setText("Hi this is my first code")
    text.move(50,50)

    btn1=QtWidgets.QPushButton(window)
    btn1.setText("Click on me")
    btn1.clicked.connect(on_clicked)
    window.show()
    sys.exit(app.exec())
main()