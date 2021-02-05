import sys
from main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    main_window = Ui_MainWindow()
    main_window.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()