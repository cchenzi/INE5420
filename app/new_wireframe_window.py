import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from app.wireframe import Wireframe
from app.utils import Shape


class NewWireframeWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(560, 360)
        self.partnerDialog = parent
        self.display_file = self.partnerDialog.display_file
        self.points = []
        self.color = QtCore.Qt.black
        self.setup()

    def setup(self):
        self.newWireframeLabel = QtWidgets.QLabel(self)
        self.newWireframeLabel.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.newWireframeLabel.setObjectName("newWireframeLabel")

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(200, 30, 351, 261))
        self.tabWidget.setObjectName("tabWidget")

        self.newPointsListWidget = QtWidgets.QListWidget(self)
        self.newPointsListWidget.setGeometry(QtCore.QRect(10, 30, 171, 261))
        self.newPointsListWidget.setObjectName("newPointsListWidget")
        self.deletePointPushButton = QtWidgets.QPushButton(self)
        self.deletePointPushButton.setGeometry(QtCore.QRect(10, 300, 171, 25))
        self.deletePointPushButton.setObjectName("deletePointPushButton")
        self.colorPickerPushButton = QtWidgets.QPushButton(self)
        self.colorPickerPushButton.setGeometry(QtCore.QRect(200, 300, 171, 25))
        self.colorPickerPushButton.setObjectName("pickColorPushButton")
        self.addNewPointPushButton = QtWidgets.QPushButton(self)
        self.addNewPointPushButton.setGeometry(QtCore.QRect(380, 300, 171, 25))
        self.addNewPointPushButton.setObjectName("addNewPointPushButton")
        self.drawPolygonPushButton = QtWidgets.QPushButton(self)
        self.drawPolygonPushButton.setEnabled(True)
        self.drawPolygonPushButton.setGeometry(QtCore.QRect(380, 330, 171, 25))
        self.drawPolygonPushButton.setObjectName("drawPolygonPushButton")
        

        self.wireframeTab = QtWidgets.QWidget()
        self.setPointsLabel = QtWidgets.QLabel(self.wireframeTab)
        self.setPointsLabel.setGeometry(QtCore.QRect(10, 10, 81, 18))
        self.setPointsLabel.setObjectName("setPointsLabel")
        self.newXLabel = QtWidgets.QLabel(self.wireframeTab)
        self.newXLabel.setGeometry(QtCore.QRect(30, 45, 21, 18))
        self.newXLabel.setObjectName("newXLabel")
        self.newYLabel = QtWidgets.QLabel(self.wireframeTab)
        self.newYLabel.setGeometry(QtCore.QRect(30, 85, 16, 16))
        self.newYLabel.setObjectName("newYLabel")
        self.newXTextEdit = QtWidgets.QTextEdit(self.wireframeTab)
        self.newXTextEdit.setGeometry(QtCore.QRect(50, 35, 51, 31))
        self.newXTextEdit.setObjectName("newXTextEdit")
        self.newYTextEdit = QtWidgets.QTextEdit(self.wireframeTab)
        self.newYTextEdit.setGeometry(QtCore.QRect(50, 75, 51, 31))
        self.newYTextEdit.setObjectName("newYTextEdit")
        self.fillCheckBox = QtWidgets.QCheckBox(self.wireframeTab)
        self.fillCheckBox.setGeometry(QtCore.QRect(30, 115, 120, 18))
        self.fillCheckBox.setObjectName("fillCheckBox")
        self.fillCheckBox.setEnabled(False)
        self.tabWidget.addTab(self.wireframeTab, "")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.set_buttons_actions()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.newWireframeLabel.setText(
            _translate("Form", "List of Points")
        )
        self.setWindowTitle(_translate("Form", "New Wireframe"))
        self.drawPolygonPushButton.setText(_translate("Form", "Draw"))
        self.addNewPointPushButton.setText(_translate("Form", "Add Point"))
        self.deletePointPushButton.setText(_translate("Form", "Delete Point"))
        self.colorPickerPushButton.setText(_translate("Form", "Pick Color"))
        self.setPointsLabel.setText(_translate("Form", "Set points:"))
        self.newXLabel.setText(_translate("Form", "X:"))
        self.newYLabel.setText(_translate("Form", "Y:"))
        self.fillCheckBox.setText(_translate("Form", "Fill Polygon"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.wireframeTab),
            _translate("Form", "Wireframe"),
        )

    def new_window(self):
        self.points = []
        self.set_text_draw_button()
        self.show()

    def add_new_point(self):
        try:
            x = float(self.newXTextEdit.toPlainText())
            y = float(self.newYTextEdit.toPlainText())
        except ValueError:
            self.partnerDialog.console_print("Invalid or empty value on X or Y")
            return
        # self.partnerDialog.console_print(f"Points={(x, y)}")
        self.points.append((x, y))
        self.partnerDialog.console_print(f"Points after append={self.points}")
        self.newXTextEdit.clear()
        self.newYTextEdit.clear()
        point_id = len(self.points) - 1
        point_str = f"Point {point_id}: {x}, {y}"
        self.newPointsListWidget.insertItem(point_id, point_str)
        self.set_text_draw_button()
        if len(self.points) > 2:
            self.fillCheckBox.setEnabled(True)

    def add_new_wireframe(self):
        if len(self.points) > 0:
            wireframe_id = self.partnerDialog.wireframe_count
            wireframe = Wireframe(
                self.points,
                wireframe_id,
                self.color,
                self.partnerDialog.window_coordinates,
                self.partnerDialog.window_transformations_matrix,
            )
            if self.fillCheckBox.isChecked():
                wireframe.filled = True
            self.display_file.append(wireframe)
            self.partnerDialog.draw_wireframe(wireframe)
            self.partnerDialog.draw_native_objects()
            # self.partnerDialog.redraw_wireframes()
            self.partnerDialog.listWidget.insertItem(wireframe_id, wireframe.name)
            self.partnerDialog.wireframe_count += 1
            self.newPointsListWidget.clear()
            self.partnerDialog.console_print(f"New wireframe added={wireframe.name}")
        self.fillCheckBox.setChecked(False)
        self.fillCheckBox.setEnabled(False)
        self.close()

    def delete_active_point(self):
        item = self.newPointsListWidget.currentRow()
        self.newPointsListWidget.takeItem(item)
        try:
            self.points.pop(item)
        except IndexError:
            self.partnerDialog.console_print("There is no point to remove")
            return
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
