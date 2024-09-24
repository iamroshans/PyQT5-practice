from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
import sys
from PyQt5 import QtCore

tasks=["Write email","finish feature","Watch Tutorial"]

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("dailyplanner.ui",self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.updateTaskList()

    def calendarDateChanged(self):
        print("The calender date was changed.")
        dateSelected=self.calendarWidget.selectedDate().toPyDate()
#         Use QDate if you're working with PyQt-specific functionality or widgets that rely on the QDate type.
# Use datetime.date (via toPyDate()) if you're interacting with standard Python code or libraries that expect native date objects.
        print("Date selected",dateSelected)

    def updateTaskList(self):
        for task in tasks:
            item=QListWidgetItem(task) 
            item.setFlags(item.flags()|QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())