import typing
import start_menu
import main_menu
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
import sys

class StartMenuUI(QMainWindow):
    def __init__(self):
        super(StartMenuUI, self).__init__()
        self.stacked_widget = QStackedWidget(self)
        self.start_menu = start_menu.Ui_MainWindow()
        self.main_menu = main_menu.Ui_MainWindow()

        self.start_menu_widget = QWidget()
        self.start_menu.setupUi(self.start_menu_widget)
        self.stacked_widget.addWidget(self.start_menu_widget)

        self.main_menu_widget = QWidget()
        self.main_menu.setupUi(self.main_menu_widget)
        self.stacked_widget.addWidget(self.main_menu_widget)

        self.setCentralWidget(self.stacked_widget)

        self.start_menu.button.clicked.connect(self.show_main_menu)

    def show_main_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_menu_ui = StartMenuUI()
    start_menu_ui.show()
    sys.exit(app.exec_())