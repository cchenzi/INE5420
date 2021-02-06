import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from new_wireframe_window import NewWireframeWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(847, 589)
        self.wireframes = []
        self.partnerDialog = NewWireframeWindow(self)
        self.setup()

    def setup(self):
        self.debuggerTextBrowser = QtWidgets.QTextBrowser(self)
        self.debuggerTextBrowser.setGeometry(QtCore.QRect(200, 411, 631, 121))
        self.debuggerTextBrowser.setObjectName("debuggerTextBrowser")
        self.displayFileLabel = QtWidgets.QLabel(self)
        self.displayFileLabel.setGeometry(QtCore.QRect(10, 20, 81, 31))
        self.displayFileLabel.setObjectName("displayFileLabel")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 111, 121))
        self.listWidget.setObjectName("listWidget")
        self.newPushButton = QtWidgets.QPushButton(self)
        self.newPushButton.setGeometry(QtCore.QRect(130, 50, 51, 34))
        self.newPushButton.setObjectName("newPushButton")
        self.deletePushButton = QtWidgets.QPushButton(self)
        self.deletePushButton.setGeometry(QtCore.QRect(130, 80, 51, 34))
        self.deletePushButton.setObjectName("deletePushButton")
        self.clearPushButton = QtWidgets.QPushButton(self)
        self.clearPushButton.setGeometry(QtCore.QRect(130, 110, 51, 34))
        self.clearPushButton.setObjectName("clearPushButton")
        self.loadPushButton = QtWidgets.QPushButton(self)
        self.loadPushButton.setGeometry(QtCore.QRect(130, 140, 51, 34))
        self.loadPushButton.setObjectName("loadPushButton")
        self.transformationsLabel = QtWidgets.QLabel(self)
        self.transformationsLabel.setGeometry(QtCore.QRect(10, 190, 111, 18))
        self.transformationsLabel.setObjectName("transformationsLabel")
        self.rotationLabel = QtWidgets.QLabel(self)
        self.rotationLabel.setGeometry(QtCore.QRect(10, 310, 58, 18))
        self.rotationLabel.setObjectName("rotationLabel")
        self.zoomLabel = QtWidgets.QLabel(self)
        self.zoomLabel.setGeometry(QtCore.QRect(10, 430, 58, 18))
        self.zoomLabel.setObjectName("zoomLabel")
        self.upPushButton = QtWidgets.QPushButton(self)
        self.upPushButton.setGeometry(QtCore.QRect(60, 220, 51, 34))
        self.upPushButton.setObjectName("upPushButton")
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
        self.zoomOutPushButton = QtWidgets.QPushButton(self)
        self.zoomOutPushButton.setGeometry(QtCore.QRect(70, 450, 51, 34))
        self.zoomOutPushButton.setObjectName("zoomOutPushButton")
        self.rotateXPushButton = QtWidgets.QPushButton(self)
        self.rotateXPushButton.setGeometry(QtCore.QRect(10, 370, 51, 34))
        self.rotateXPushButton.setObjectName("rotateXPushButton")
        self.rotateYPushButton = QtWidgets.QPushButton(self)
        self.rotateYPushButton.setGeometry(QtCore.QRect(70, 370, 51, 34))
        self.rotateYPushButton.setObjectName("rotateYPushButton")
        self.rotateZPushButton = QtWidgets.QPushButton(self)
        self.rotateZPushButton.setGeometry(QtCore.QRect(130, 370, 51, 34))
        self.rotateZPushButton.setObjectName("rotateZPushButton")
        self.degreesLabel = QtWidgets.QLabel(self)
        self.degreesLabel.setGeometry(QtCore.QRect(20, 340, 58, 18))
        self.degreesLabel.setObjectName("degreesLabel")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(80, 330, 91, 31))
        self.textEdit.setObjectName("textEdit")
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
        canvas = QtGui.QPixmap(400, 300)
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
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.displayFileLabel.setText(_translate("MainWindow", "Display File"))
        self.newPushButton.setText(_translate("MainWindow", "New"))
        self.deletePushButton.setText(_translate("MainWindow", "Delete"))
        self.clearPushButton.setText(_translate("MainWindow", "Clear"))
        self.loadPushButton.setText(_translate("MainWindow", "Load"))
        self.transformationsLabel.setText(_translate("MainWindow", "Transformations"))
        self.rotationLabel.setText(_translate("MainWindow", "Rotation"))
        self.zoomLabel.setText(_translate("MainWindow", "Zoom"))
        self.upPushButton.setText(_translate("MainWindow", "Up"))
        self.downPushButton.setText(_translate("MainWindow", "Down"))
        self.rightPushButton.setText(_translate("MainWindow", "Right"))
        self.leftPushButton.setText(_translate("MainWindow", "Left"))
        self.zoomInPushButton.setText(_translate("MainWindow", "+"))
        self.zoomOutPushButton.setText(_translate("MainWindow", "-"))
        self.rotateXPushButton.setText(_translate("MainWindow", "X"))
        self.rotateYPushButton.setText(_translate("MainWindow", "Y"))
        self.rotateZPushButton.setText(_translate("MainWindow", "Z"))
        self.degreesLabel.setText(_translate("MainWindow", "Degrees:"))

    def set_buttons_actions(self):
        self.newPushButton.clicked.connect(self.new_wireframe_window)
        self.deletePushButton.clicked.connect(
            lambda: self.draw_something(10, 10, 10, 300)
        )

    def new_wireframe_window(self):
        self.partnerDialog.new_window()

    def draw_something(self, x1, y1, x2, y2):
        print("test")
        print(f"Wireframes:{self.wireframes}")
        print(self.textEdit.toPlainText())
        # x1 = int(self.textEdit.toPlainText())
        self.displayFrame.update()
        self.painter.setPen(QtCore.Qt.blue)
        print(f"Points=({x1, y1}); {x2, y2})")
        self.painter.drawLine(x1, y1, x2, y2)

    def draw_line(self, x1, y1, x2, y2):
        print(f"Drawning new line! Points={(x1, y1)}, {(x2, y2)}")
        self.displayFrame.update()
        self.painter.setPen(QtCore.Qt.blue)
        self.painter.drawLine(x1, y1, x2, y2)

    def draw_wireframe(self, wireframe):
        for index in range(wireframe.number_points):
            x1, y1 = wireframe.coordinates[index]
            x2, y2 = wireframe.coordinates[(index + 1) % wireframe.number_points]
            self.draw_line(x1, y1, x2, y2)
