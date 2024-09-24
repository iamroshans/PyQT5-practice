from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main():
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setGeometry(100,200,300,300)
    window.setWindowTitle("My first window")
    window.show()
    sys.exit(app.exec())
main()