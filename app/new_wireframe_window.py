import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QToolTip,
    QMessageBox,
    QLabel,
)


class NewWireframeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(421, 221)
        self.setup()

    def setup(self):

        self.newPointsTextBrowser = QtWidgets.QTextBrowser(self)
        self.newPointsTextBrowser.setGeometry(QtCore.QRect(140, 30, 261, 131))
        self.newPointsTextBrowser.setObjectName("newPointsTextBrowser")
        self.drawPolygonPushButton = QtWidgets.QPushButton(self)
        self.drawPolygonPushButton.setEnabled(True)
        self.drawPolygonPushButton.setGeometry(QtCore.QRect(310, 180, 88, 34))
        self.drawPolygonPushButton.setObjectName("drawPolygonPushButton")
        self.addNewPointPushButton = QtWidgets.QPushButton(self)
        self.addNewPointPushButton.setGeometry(QtCore.QRect(50, 130, 51, 34))
        self.addNewPointPushButton.setObjectName("addNewPointPushButton")
        self.setPointsLabel = QtWidgets.QLabel(self)
        self.setPointsLabel.setGeometry(QtCore.QRect(10, 30, 81, 18))
        self.setPointsLabel.setObjectName("setPointsLabel")
        self.newXLabel = QtWidgets.QLabel(self)
        self.newXLabel.setGeometry(QtCore.QRect(30, 60, 21, 18))
        self.newXLabel.setObjectName("newXLabel")
        self.newYLabel = QtWidgets.QLabel(self)
        self.newYLabel.setGeometry(QtCore.QRect(30, 100, 16, 16))
        self.newYLabel.setObjectName("newYLabel")
        self.newXTextEdit = QtWidgets.QTextEdit(self)
        self.newXTextEdit.setGeometry(QtCore.QRect(50, 50, 51, 31))
        self.newXTextEdit.setObjectName("newXTextEdit")
        self.newYTextEdit = QtWidgets.QTextEdit(self)
        self.newYTextEdit.setGeometry(QtCore.QRect(50, 90, 51, 31))
        self.newYTextEdit.setObjectName("newYTextEdit")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.drawPolygonPushButton.setText(_translate("Form", "Draw"))
        self.addNewPointPushButton.setText(_translate("Form", "Add "))
        self.setPointsLabel.setText(_translate("Form", "Set points:"))
        self.newXLabel.setText(_translate("Form", "X:"))
        self.newYLabel.setText(_translate("Form", "Y:"))
