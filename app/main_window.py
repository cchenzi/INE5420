from PyQt5 import QtCore, QtGui, QtWidgets
from new_wireframe_window import NewWireframeWindow
from utils import (
    CoordinatesRepresentation,
    transform_coordinates,
)
from config import (
    DEFAULT_X_MAX,
    DEFAULT_X_MIN,
    DEFAULT_Y_MAX,
    DEFAULT_Y_MIN,
    SHIFT_FACTOR,
)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(847, 589)
        self.display_file = []
        self.partnerDialog = NewWireframeWindow(self)
        self.default_x_max = DEFAULT_X_MAX
        self.default_x_min = DEFAULT_X_MIN
        self.default_y_max = DEFAULT_Y_MAX
        self.default_y_min = DEFAULT_Y_MIN
        self.scale_acumulator = 0
        self.window_coordinates = CoordinatesRepresentation(
            self.default_x_min,
            self.default_y_min,
            self.default_x_max,
            self.default_y_max,
            factor=SHIFT_FACTOR,
        )
        self.viewport_coordinates = CoordinatesRepresentation(
            self.default_x_min,
            self.default_y_min,
            self.default_x_max,
            self.default_y_max,
        )
        self.wireframe_count = 0
        self.setup()

    def setup(self):
        self.debuggerTextBrowser = QtWidgets.QTextBrowser(self)
        self.debuggerTextBrowser.setGeometry(QtCore.QRect(200, 410, 630, 120))
        self.debuggerTextBrowser.setObjectName("debuggerTextBrowser")
        self.displayFileLabel = QtWidgets.QLabel(self)
        self.displayFileLabel.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.displayFileLabel.setObjectName("displayFileLabel")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 111, 121))
        self.listWidget.setObjectName("listWidget")
        self.newPushButton = QtWidgets.QPushButton(self)
        self.newPushButton.setGeometry(QtCore.QRect(130, 50, 60, 34))
        self.newPushButton.setObjectName("newPushButton")
        self.deletePushButton = QtWidgets.QPushButton(self)
        self.deletePushButton.setGeometry(QtCore.QRect(130, 80, 60, 34))
        self.deletePushButton.setObjectName("deletePushButton")
        self.clearPushButton = QtWidgets.QPushButton(self)
        self.clearPushButton.setGeometry(QtCore.QRect(130, 110, 60, 34))
        self.clearPushButton.setObjectName("clearPushButton")
        self.refreshPushButton = QtWidgets.QPushButton(self)
        self.refreshPushButton.setGeometry(QtCore.QRect(130, 140, 60, 34))
        self.refreshPushButton.setObjectName("refreshPushButton")
        self.navigationLabel = QtWidgets.QLabel(self)
        self.navigationLabel.setGeometry(QtCore.QRect(10, 190, 111, 18))
        self.navigationLabel.setObjectName("navigationLabel")
        self.rotationLabel = QtWidgets.QLabel(self)
        self.rotationLabel.setGeometry(QtCore.QRect(10, 310, 58, 18))
        self.rotationLabel.setObjectName("rotationLabel")
        self.zoomLabel = QtWidgets.QLabel(self)
        self.zoomLabel.setGeometry(QtCore.QRect(10, 430, 58, 18))
        self.zoomLabel.setObjectName("zoomLabel")
        self.upPushButton = QtWidgets.QPushButton(self)
        self.upPushButton.setGeometry(QtCore.QRect(60, 220, 51, 34))
        self.upPushButton.setObjectName("upPushButton")

        self.inPushButton = QtWidgets.QPushButton(self)
        self.inPushButton.setGeometry(QtCore.QRect(115, 200, 35, 20))
        self.inPushButton.setObjectName("inPushButton")
        self.outPushButton = QtWidgets.QPushButton(self)
        self.outPushButton.setGeometry(QtCore.QRect(150, 200, 35, 20))
        self.outPushButton.setObjectName("outPushButton")

        self.downPushButton = QtWidgets.QPushButton(self)
        self.downPushButton.setGeometry(QtCore.QRect(60, 250, 51, 34))
        self.downPushButton.setObjectName("downPushButton")
        self.rightPushButton = QtWidgets.QPushButton(self)
        self.rightPushButton.setGeometry(QtCore.QRect(110, 240, 51, 34))
        self.rightPushButton.setObjectName("rightPushButton")
        self.leftPushButton = QtWidgets.QPushButton(self)
        self.leftPushButton.setGeometry(QtCore.QRect(10, 240, 51, 34))
        self.leftPushButton.setObjectName("leftPushButton")
        self.zoomInPushButton = QtWidgets.QPushButton(self)
        self.zoomInPushButton.setGeometry(QtCore.QRect(10, 450, 51, 34))
        self.zoomInPushButton.setObjectName("zoomInPushButton")
        self.zoomInPushButton.setEnabled(False)
        self.zoomOutPushButton = QtWidgets.QPushButton(self)
        self.zoomOutPushButton.setGeometry(QtCore.QRect(70, 450, 51, 34))
        self.zoomOutPushButton.setObjectName("zoomOutPushButton")
        self.zoomOutPushButton.setEnabled(False)
        self.rotateXPushButton = QtWidgets.QPushButton(self)
        self.rotateXPushButton.setGeometry(QtCore.QRect(10, 370, 51, 34))
        self.rotateXPushButton.setObjectName("rotateXPushButton")
        self.rotateXPushButton.setEnabled(False)
        self.rotateYPushButton = QtWidgets.QPushButton(self)
        self.rotateYPushButton.setGeometry(QtCore.QRect(70, 370, 51, 34))
        self.rotateYPushButton.setObjectName("rotateYPushButton")
        self.rotateYPushButton.setEnabled(False)
        self.rotateZPushButton = QtWidgets.QPushButton(self)
        self.rotateZPushButton.setGeometry(QtCore.QRect(130, 370, 51, 34))
        self.rotateZPushButton.setObjectName("rotateZPushButton")
        self.rotateZPushButton.setEnabled(False)
        self.degreesLabel = QtWidgets.QLabel(self)
        self.degreesLabel.setGeometry(QtCore.QRect(20, 340, 58, 18))
        self.degreesLabel.setObjectName("degreesLabel")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(80, 330, 91, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(False)
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(10, 170, 191, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(10, 290, 191, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(10, 410, 191, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.displayFrame = QtWidgets.QLabel(self)
        self.displayFrame.setGeometry(QtCore.QRect(200, 20, 630, 380))
        self.displayFrame.setAutoFillBackground(False)
        self.displayFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        canvas = QtGui.QPixmap(630, 380)
        canvas.fill(QtGui.QColor("white"))
        self.displayFrame.setPixmap(canvas)
        self.painter = QtGui.QPainter(self.displayFrame.pixmap())
        self.displayFrame.setObjectName("displayFrame")

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 30))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.dialogs = list()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.set_buttons_actions()
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Computer Graphics"))
        self.displayFileLabel.setText(_translate("MainWindow", "Display File"))
        self.newPushButton.setText(_translate("MainWindow", "New"))
        self.deletePushButton.setText(_translate("MainWindow", "Delete"))
        self.clearPushButton.setText(_translate("MainWindow", "Clear"))
        self.refreshPushButton.setText(_translate("MainWindow", "Refresh"))
        self.navigationLabel.setText(_translate("MainWindow", "Navigation"))
        self.rotationLabel.setText(_translate("MainWindow", "Rotation"))
        self.zoomLabel.setText(_translate("MainWindow", "Zoom"))
        self.upPushButton.setText(_translate("MainWindow", "Up"))
        self.downPushButton.setText(_translate("MainWindow", "Down"))
        self.rightPushButton.setText(_translate("MainWindow", "Right"))
        self.leftPushButton.setText(_translate("MainWindow", "Left"))
        self.inPushButton.setText(_translate("MainWindow", "In"))
        self.outPushButton.setText(_translate("MainWindow", "Out"))
        self.zoomInPushButton.setText(_translate("MainWindow", "+"))
        self.zoomOutPushButton.setText(_translate("MainWindow", "-"))
        self.rotateXPushButton.setText(_translate("MainWindow", "X"))
        self.rotateYPushButton.setText(_translate("MainWindow", "Y"))
        self.rotateZPushButton.setText(_translate("MainWindow", "Z"))
        self.degreesLabel.setText(_translate("MainWindow", "Degrees:"))

    def console_print(self, string):
        self.debuggerTextBrowser.append(string)
        print(string)

    def console_clear(self):
        self.debuggerTextBrowser.clear()

    def set_buttons_actions(self):
        self.newPushButton.clicked.connect(self.new_wireframe_window)
        self.deletePushButton.clicked.connect(self.delete_wireframe)
        self.clearPushButton.clicked.connect(self.clear_display_file)
        self.clearPushButton.clicked.connect(self.clear_canvas)
        self.refreshPushButton.clicked.connect(self.refresh_canvas)
        self.leftPushButton.clicked.connect(self.shift_window_left)
        self.rightPushButton.clicked.connect(self.shift_window_right)
        self.upPushButton.clicked.connect(self.shift_window_up)
        self.downPushButton.clicked.connect(self.shift_window_down)
        self.inPushButton.clicked.connect(self.scale_window_in)
        self.outPushButton.clicked.connect(self.scale_window_out)

    def new_wireframe_window(self):
        self.partnerDialog.new_window()

    def delete_wireframe(self):
        if len(self.display_file) > 0:
            item = self.listWidget.currentRow()
            self.listWidget.takeItem(item)
            wireframe = self.display_file.pop(item)
            self.console_print(f"{wireframe.name} deleted!")
            self.redraw_wireframes()

    def clear_display_file(self):
        self.listWidget.setCurrentRow(0)
        wireframes = len(self.display_file)
        for i in range(wireframes):
            item = self.listWidget.currentRow()
            self.listWidget.takeItem(item)
            self.display_file.pop(item)
        self.set_navigation_default_paramaters()
        self.scale_window_by_step(0)
        self.redraw_wireframes()
        self.console_print("Canvas cleared")

    def clear_canvas(self):
        self.displayFrame.pixmap().fill(QtGui.QColor("white"))
        self.displayFrame.update()

    def draw_line(self, x1, y1, x2, y2, color):
        self.console_print(f"Drawning new line! Points={(x1, y1)}, {(x2, y2)}")
        self.displayFrame.update()
        self.painter.setPen(QtGui.QPen(color, 5))
        self.painter.drawLine(x1, y1, x2, y2)

    def draw_wireframe(self, wireframe):
        for index in range(wireframe.number_points):
            x1, y1 = wireframe.coordinates[index]
            xvp1, yvp1 = transform_coordinates(
                x1,
                y1,
                self.window_coordinates,
                self.viewport_coordinates,
            )
            x2, y2 = wireframe.coordinates[(index + 1) % wireframe.number_points]
            xvp2, yvp2 = transform_coordinates(
                x2,
                y2,
                self.window_coordinates,
                self.viewport_coordinates,
            )
            self.draw_line(xvp1, yvp1, xvp2, yvp2, wireframe.color)

    def set_navigation_default_paramaters(self):
        self.console_print("Navigation parameters reseted!")
        self.window_coordinates.x_max = self.default_x_max
        self.window_coordinates.x_min = self.default_x_min
        self.window_coordinates.y_max = self.default_y_max
        self.window_coordinates.y_min = self.default_y_min
        self.scale_acumulator = 0

    def shift_window_left(self):
        self.window_coordinates.x_min -= self.window_coordinates.x_shift_factor
        self.window_coordinates.x_max -= self.window_coordinates.x_shift_factor
        self.redraw_wireframes()

    def shift_window_right(self):
        self.window_coordinates.x_min += self.window_coordinates.x_shift_factor
        self.window_coordinates.x_max += self.window_coordinates.x_shift_factor
        self.redraw_wireframes()

    def shift_window_up(self):
        self.window_coordinates.y_min += self.window_coordinates.y_shift_factor
        self.window_coordinates.y_max += self.window_coordinates.y_shift_factor
        self.redraw_wireframes()

    def shift_window_down(self):
        self.window_coordinates.y_min -= self.window_coordinates.y_shift_factor
        self.window_coordinates.y_max -= self.window_coordinates.y_shift_factor
        self.redraw_wireframes()

    def scale_window_by_step(self, step):
        self.scale_acumulator += step
        scale_factor = 1 + self.scale_acumulator
        self.window_coordinates.x_max = self.default_x_max * scale_factor
        self.window_coordinates.y_max = self.default_y_max * scale_factor

    def scale_window_in(self):
        self.scale_window_by_step(-0.01)
        self.redraw_wireframes()

    def scale_window_out(self):
        self.scale_window_by_step(0.01)
        self.redraw_wireframes()

    def refresh_canvas(self):
        self.set_navigation_default_paramaters()
        self.redraw_wireframes()

    def redraw_wireframes(self):
        self.clear_canvas()
        for wirefame in self.display_file:
            self.draw_wireframe(wirefame)
