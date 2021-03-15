import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from app.wireframe import Wireframe, BezierCurve
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
        self.setPointsWireframeLabel = QtWidgets.QLabel(self.wireframeTab)
        self.setPointsWireframeLabel.setGeometry(QtCore.QRect(10, 10, 81, 18))
        self.setPointsWireframeLabel.setObjectName("setPointsWireframeLabel")
        self.newXWireframeLabel = QtWidgets.QLabel(self.wireframeTab)
        self.newXWireframeLabel.setGeometry(QtCore.QRect(30, 45, 21, 18))
        self.newXWireframeLabel.setObjectName("newXWireframeLabel")
        self.newYWireframeLabel = QtWidgets.QLabel(self.wireframeTab)
        self.newYWireframeLabel.setGeometry(QtCore.QRect(30, 85, 16, 16))
        self.newYWireframeLabel.setObjectName("newYWireframeLabel")
        self.newXWireframeTextEdit = QtWidgets.QTextEdit(self.wireframeTab)
        self.newXWireframeTextEdit.setGeometry(QtCore.QRect(50, 35, 51, 31))
        self.newXWireframeTextEdit.setObjectName("newXWireframeTextEdit")
        self.newYWireframeTextEdit = QtWidgets.QTextEdit(self.wireframeTab)
        self.newYWireframeTextEdit.setGeometry(QtCore.QRect(50, 75, 51, 31))
        self.newYWireframeTextEdit.setObjectName("newYWireframeTextEdit")
        self.fillCheckBox = QtWidgets.QCheckBox(self.wireframeTab)
        self.fillCheckBox.setGeometry(QtCore.QRect(30, 115, 120, 18))
        self.fillCheckBox.setObjectName("fillCheckBox")
        self.fillCheckBox.setEnabled(False)
        self.tabWidget.addTab(self.wireframeTab, "")

        self.bezierTab = QtWidgets.QWidget()
        self.setPointsBezierLabel = QtWidgets.QLabel(self.bezierTab)
        self.setPointsBezierLabel.setGeometry(QtCore.QRect(10, 10, 81, 18))
        self.setPointsBezierLabel.setObjectName("setPointsBezierLabel")
        self.newXBezierLabel = QtWidgets.QLabel(self.bezierTab)
        self.newXBezierLabel.setGeometry(QtCore.QRect(30, 45, 21, 18))
        self.newXBezierLabel.setObjectName("newXBezierLabel")
        self.newYBezierLabel = QtWidgets.QLabel(self.bezierTab)
        self.newYBezierLabel.setGeometry(QtCore.QRect(30, 85, 16, 16))
        self.newYBezierLabel.setObjectName("newYBezierLabel")
        self.newXBezierTextEdit = QtWidgets.QTextEdit(self.bezierTab)
        self.newXBezierTextEdit.setGeometry(QtCore.QRect(50, 35, 51, 31))
        self.newXBezierTextEdit.setObjectName("newXBezierTextEdit")
        self.newYBezierTextEdit = QtWidgets.QTextEdit(self.bezierTab)
        self.newYBezierTextEdit.setGeometry(QtCore.QRect(50, 75, 51, 31))
        self.newYBezierTextEdit.setObjectName("newYBezierTextEdit")
        self.accuracyBezierLabel = QtWidgets.QLabel(self.bezierTab)
        self.accuracyBezierLabel.setGeometry(QtCore.QRect(30, 145, 81, 16))
        self.accuracyBezierLabel.setObjectName("accuracyLabel")
        self.accuracyBezierTextEdit = QtWidgets.QTextEdit(self.bezierTab)
        self.accuracyBezierTextEdit.setGeometry(QtCore.QRect(100, 138, 71, 31))
        self.accuracyBezierTextEdit.setObjectName("accuracyTextEdit")
        self.accuracyBezierTextEdit.setText("10.0")
        self.tabWidget.addTab(self.bezierTab, "")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.set_buttons_actions()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.newWireframeLabel.setText(_translate("Form", "List of Points"))
        self.setWindowTitle(_translate("Form", "New Wireframe"))
        self.drawPolygonPushButton.setText(_translate("Form", "Draw"))
        self.addNewPointPushButton.setText(_translate("Form", "Add Point"))
        self.deletePointPushButton.setText(_translate("Form", "Delete Point"))
        self.colorPickerPushButton.setText(_translate("Form", "Pick Color"))
        self.setPointsWireframeLabel.setText(_translate("Form", "Set points:"))
        self.setPointsBezierLabel.setText(_translate("Form", "Set points:"))
        self.newXWireframeLabel.setText(_translate("Form", "X:"))
        self.newYWireframeLabel.setText(_translate("Form", "Y:"))
        self.newXBezierLabel.setText(_translate("Form", "X:"))
        self.newYBezierLabel.setText(_translate("Form", "Y:"))
        self.fillCheckBox.setText(_translate("Form", "Fill Polygon"))
        self.accuracyBezierLabel.setText(_translate("Form", "Accuracy:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.wireframeTab),
            _translate("Form", "Wireframe"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.bezierTab),
            _translate("Form", "Bezier Curve"),
        )

    def new_window(self):
        self.points = []
        self.set_text_draw_button()
        self.show()

    def add_new_point(self):
        active_tab = self.tabWidget.currentIndex()

        if active_tab == 0:
            xTextEdit = self.newXWireframeTextEdit
            yTextEdit = self.newYWireframeTextEdit
        if active_tab == 1:
            xTextEdit = self.newXBezierTextEdit
            yTextEdit = self.newYBezierTextEdit
        try:
            x = float(xTextEdit.toPlainText())
            y = float(yTextEdit.toPlainText())
        except ValueError:
            self.partnerDialog.console_print("Invalid or empty value on X or Y")
            return
        # self.partnerDialog.console_print(f"Points={(x, y)}")
        self.points.append((x, y))
        self.partnerDialog.console_print(f"Points after append={self.points}")
        xTextEdit.clear()
        yTextEdit.clear()
        point_id = len(self.points) - 1
        point_str = f"Point {point_id}: {x}, {y}"
        self.newPointsListWidget.insertItem(point_id, point_str)
        self.set_text_draw_button()
        if len(self.points) > 2:
            self.fillCheckBox.setEnabled(True)

    def add_new_wireframe(self):
        active_tab = self.tabWidget.currentIndex()
        if len(self.points) > 0:
            wireframe_id = self.partnerDialog.wireframe_count
            if active_tab == 0:
                wireframe = Wireframe(
                    self.points,
                    wireframe_id,
                    self.color,
                    self.partnerDialog.window_coordinates,
                    self.partnerDialog.window_transformations_matrix,
                )
                if self.fillCheckBox.isChecked():
                    wireframe.filled = True

            if active_tab == 1:
                if len(self.points) % 3 != 1 or len(self.points) < 3:
                    self.partnerDialog.console_print(
                        "Invalid number of points to draw bezier curve"
                    )
                    return
                try:
                    accuracy = float(self.accuracyBezierTextEdit.toPlainText())
                except ValueError:
                    self.partnerDialog.console_print(
                        "Invalid or empty value on accuracy, using default value (10)"
                    )
                    accuracy = 10
                wireframe = BezierCurve(
                    self.points,
                    wireframe_id,
                    self.color,
                    self.partnerDialog.window_coordinates,
                    self.partnerDialog.window_transformations_matrix,
                    accuracy,
                )

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
        self.tabWidget.currentChanged.connect(self.set_text_draw_button)

    def set_text_draw_button(self):
        active_tab = self.tabWidget.currentIndex()
        if active_tab == 0:
            self.drawPolygonPushButton.setText(f"Draw {Shape(len(self.points)).name}")
        if active_tab == 1:
            if len(self.points) == 0:
                self.drawPolygonPushButton.setText(f"Draw Nothing")
            else:
                self.drawPolygonPushButton.setText(f"Draw Curve")
