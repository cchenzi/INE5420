import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from wireframe import Wireframe


class NewWireframeWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(421, 221)
        self.partnerDialog = parent
        self.display_file = self.partnerDialog.display_file
        self.points = []
        self.setup()

    def setup(self):

        self.newPointsListWidget = QtWidgets.QListWidget(self)
        self.newPointsListWidget.setGeometry(QtCore.QRect(140, 30, 261, 131))
        self.newPointsListWidget.setObjectName("newPointsListWidget")
        self.drawPolygonPushButton = QtWidgets.QPushButton(self)
        self.drawPolygonPushButton.setEnabled(True)
        self.drawPolygonPushButton.setGeometry(QtCore.QRect(310, 180, 88, 34))
        self.drawPolygonPushButton.setObjectName("drawPolygonPushButton")

        self.deletePointPushButton = QtWidgets.QPushButton(self)
        self.deletePointPushButton.setGeometry(QtCore.QRect(210, 180, 88, 34))
        self.deletePointPushButton.setObjectName("deletePointPushButton")

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
        self.set_buttons_actions()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.drawPolygonPushButton.setText(_translate("Form", "Draw"))
        self.addNewPointPushButton.setText(_translate("Form", "Add "))
        self.deletePointPushButton.setText(_translate("Form", "Delete"))
        self.setPointsLabel.setText(_translate("Form", "Set points:"))
        self.newXLabel.setText(_translate("Form", "X:"))
        self.newYLabel.setText(_translate("Form", "Y:"))

    def new_window(self):
        self.points = []
        self.show()

    def add_new_point(self):
        x = int(self.newXTextEdit.toPlainText())
        y = int(self.newYTextEdit.toPlainText())
        # self.partnerDialog.console_print(f"Points={(x, y)}")
        self.points.append((x, y))
        self.partnerDialog.console_print(f"Points after append={self.points}")
        self.newXTextEdit.clear()
        self.newYTextEdit.clear()
        point_id = len(self.points) - 1
        point_str = f"Point {point_id}: {x}, {y}"
        self.newPointsListWidget.insertItem(point_id, point_str)

    def add_new_wireframe(self):
        wireframe = Wireframe(self.points, len(self.display_file))
        self.display_file.append(wireframe)
        self.partnerDialog.console_print(f"New wireframe added={wireframe.name}")
        self.close()
        self.partnerDialog.draw_wireframe(wireframe)
        self.newPointsListWidget.clear()

    def delete_active_point(self):
        item = self.newPointsListWidget.currentRow()
        self.newPointsListWidget.takeItem(item)
        self.partnerDialog.console_print(f"Point {item} deleted!")
        self.points.pop(item)

    def set_buttons_actions(self):
        self.addNewPointPushButton.clicked.connect(self.add_new_point)
        self.drawPolygonPushButton.clicked.connect(self.add_new_wireframe)
        self.deletePointPushButton.clicked.connect(self.delete_active_point)
