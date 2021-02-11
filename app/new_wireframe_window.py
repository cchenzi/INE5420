import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from wireframe import Wireframe
from utils import Shape


class NewWireframeWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(421, 221)
        self.partnerDialog = parent
        self.display_file = self.partnerDialog.display_file
        self.points = []
        self.color = QtCore.Qt.black
        self.setup()

    def setup(self):

        self.newPointsListWidget = QtWidgets.QListWidget(self)
        self.newPointsListWidget.setGeometry(QtCore.QRect(140, 30, 261, 131))
        self.newPointsListWidget.setObjectName("newPointsListWidget")
        self.drawPolygonPushButton = QtWidgets.QPushButton(self)
        self.drawPolygonPushButton.setEnabled(True)
        self.drawPolygonPushButton.setGeometry(QtCore.QRect(280, 180, 120, 34))
        self.drawPolygonPushButton.setObjectName("drawPolygonPushButton")

        self.colorPickerPushButton = QtWidgets.QPushButton(self)
        self.colorPickerPushButton.setGeometry(QtCore.QRect(140, 180, 120, 34))
        self.colorPickerPushButton.setObjectName("pickColorPushButton")

        self.deletePointPushButton = QtWidgets.QPushButton(self)
        self.deletePointPushButton.setGeometry(QtCore.QRect(50, 171, 51, 34))
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
        self.setWindowTitle(_translate("Form", "New Wireframe"))
        self.drawPolygonPushButton.setText(_translate("Form", "Draw"))
        self.addNewPointPushButton.setText(_translate("Form", "Add "))
        self.deletePointPushButton.setText(_translate("Form", "Delete"))
        self.colorPickerPushButton.setText(_translate("Form", "Pick Color"))
        self.setPointsLabel.setText(_translate("Form", "Set points:"))
        self.newXLabel.setText(_translate("Form", "X:"))
        self.newYLabel.setText(_translate("Form", "Y:"))

    def new_window(self):
        self.points = []
        self.set_text_draw_button()
        self.show()

    def add_new_point(self):
        x = float(self.newXTextEdit.toPlainText())
        y = float(self.newYTextEdit.toPlainText())
        # self.partnerDialog.console_print(f"Points={(x, y)}")
        self.points.append((x, y))
        self.partnerDialog.console_print(f"Points after append={self.points}")
        self.newXTextEdit.clear()
        self.newYTextEdit.clear()
        point_id = len(self.points) - 1
        point_str = f"Point {point_id}: {x}, {y}"
        self.newPointsListWidget.insertItem(point_id, point_str)
        self.set_text_draw_button()

    def add_new_wireframe(self):
        wireframe_id = self.partnerDialog.wireframe_count
        wireframe = Wireframe(self.points, wireframe_id, self.color)
        self.display_file.append(wireframe)
        self.partnerDialog.console_print(f"New wireframe added={wireframe.name}")
        self.close()
        self.partnerDialog.draw_wireframe(wireframe)
        self.partnerDialog.listWidget.insertItem(wireframe_id, wireframe.name)
        self.partnerDialog.wireframe_count += 1
        self.newPointsListWidget.clear()

    def delete_active_point(self):
        item = self.newPointsListWidget.currentRow()
        self.newPointsListWidget.takeItem(item)
        self.points.pop(item)
        self.set_text_draw_button()
        self.partnerDialog.console_print(f"Point {item} deleted!")

    def pick_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.color = color
            self.partnerDialog.console_print("Color updated")

    def set_buttons_actions(self):
        self.addNewPointPushButton.clicked.connect(self.add_new_point)
        self.drawPolygonPushButton.clicked.connect(self.add_new_wireframe)
        self.deletePointPushButton.clicked.connect(self.delete_active_point)
        self.colorPickerPushButton.clicked.connect(self.pick_color)

    def set_text_draw_button(self):
        self.drawPolygonPushButton.setText(f"Draw {Shape(len(self.points)).name}")
