import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from wireframe import Wireframe
from utils import Shape

# UPDATE


class TransformWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(560, 360)
        self.setObjectName("TransformWindow")
        self.partnerDialog = parent
        self.setup()

    def setup(self):
        self.transformLabel = QtWidgets.QLabel(self)
        self.transformLabel.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.transformLabel.setObjectName("transformLabel")
        self.listView = QtWidgets.QListView(self)
        self.listView.setGeometry(QtCore.QRect(10, 30, 171, 261))
        self.listView.setObjectName("listView")
        self.deleteTransformationPushButton = QtWidgets.QPushButton(self)
        self.deleteTransformationPushButton.setGeometry(QtCore.QRect(10, 300, 171, 25))
        self.deleteTransformationPushButton.setObjectName(
            "deleteTransformationPushButton"
        )

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(200, 30, 351, 261))
        self.tabWidget.setObjectName("tabWidget")

        self.rotationTab = QtWidgets.QWidget()
        self.rotationTab.setObjectName("rotationTab")
        self.rotationComboBox = QtWidgets.QComboBox(self.rotationTab)
        self.rotationComboBox.setGeometry(QtCore.QRect(20, 20, 281, 25))
        self.rotationComboBox.setObjectName("rotationComboBox")
        self.rotationComboBox.addItem("")
        self.rotationComboBox.addItem("")
        self.rotationComboBox.addItem("")
        self.rotationText = QtWidgets.QTextEdit(self.rotationTab)
        self.rotationText.setGeometry(QtCore.QRect(100, 60, 51, 21))
        self.rotationText.setObjectName("rotationText")
        self.rotationLabel = QtWidgets.QLabel(self.rotationTab)
        self.rotationLabel.setGeometry(QtCore.QRect(30, 60, 71, 17))
        self.rotationLabel.setObjectName("rotationLabel")
        self.tabWidget.addTab(self.rotationTab, "")

        self.translationTab = QtWidgets.QWidget()
        self.translationTab.setObjectName("translationTab")
        self.translationXTextEdit = QtWidgets.QTextEdit(self.translationTab)
        self.translationXTextEdit.setGeometry(QtCore.QRect(40, 20, 51, 21))
        self.translationXTextEdit.setObjectName("translationXTextEdit")
        self.translationXLabel = QtWidgets.QLabel(self.translationTab)
        self.translationXLabel.setGeometry(QtCore.QRect(20, 20, 16, 17))
        self.translationXLabel.setObjectName("translationXLabel")
        self.translationYTextEdit = QtWidgets.QTextEdit(self.translationTab)
        self.translationYTextEdit.setGeometry(QtCore.QRect(40, 50, 51, 21))
        self.translationYTextEdit.setObjectName("translationYTextEdit")
        self.translationYLabel = QtWidgets.QLabel(self.translationTab)
        self.translationYLabel.setGeometry(QtCore.QRect(20, 50, 16, 17))
        self.translationYLabel.setObjectName("translationYLabel")
        self.tabWidget.addTab(self.translationTab, "")

        self.scaleTab = QtWidgets.QWidget()
        self.scaleTab.setObjectName("scaleTab")
        self.scalingXTextEdit = QtWidgets.QTextEdit(self.scaleTab)
        self.scalingXTextEdit.setGeometry(QtCore.QRect(40, 20, 51, 21))
        self.scalingXTextEdit.setObjectName("scalingXTextEdit")
        self.scalingYLabel = QtWidgets.QLabel(self.scaleTab)
        self.scalingYLabel.setGeometry(QtCore.QRect(20, 50, 16, 17))
        self.scalingYLabel.setObjectName("scalingYLabel")
        self.scalingXLabel = QtWidgets.QLabel(self.scaleTab)
        self.scalingXLabel.setGeometry(QtCore.QRect(20, 20, 16, 17))
        self.scalingXLabel.setObjectName("scalingXLabel")
        self.scalingYTextEdit = QtWidgets.QTextEdit(self.scaleTab)
        self.scalingYTextEdit.setGeometry(QtCore.QRect(40, 50, 51, 21))
        self.scalingYTextEdit.setObjectName("scalingYTextEdit")
        self.tabWidget.addTab(self.scaleTab, "")

        self.reflectionTab = QtWidgets.QWidget()
        self.reflectionTab.setObjectName("reflectionTab")
        self.reflectionXCheckBox = QtWidgets.QCheckBox(self.reflectionTab)
        self.reflectionXCheckBox.setGeometry(QtCore.QRect(20, 20, 92, 23))
        self.reflectionXCheckBox.setObjectName("reflectionXCheckBox")
        self.reflectionYCheckBox = QtWidgets.QCheckBox(self.reflectionTab)
        self.reflectionYCheckBox.setGeometry(QtCore.QRect(20, 50, 92, 23))
        self.reflectionYCheckBox.setObjectName("reflectionYCheckBox")
        self.tabWidget.addTab(self.reflectionTab, "")

        self.addTransformationPushButton = QtWidgets.QPushButton(self)
        self.addTransformationPushButton.setGeometry(QtCore.QRect(380, 300, 171, 25))
        self.addTransformationPushButton.setObjectName("addTransformationPushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.tabWidget.setCurrentIndex(0)
        self.set_buttons_actions()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.transformLabel.setText(
            _translate("TransformWindow", "Transform Wireframe")
        )
        self.deleteTransformationPushButton.setText(
            _translate("TransformWindow", "Delete Transformation")
        )
        self.translationXLabel.setText(_translate("TransformWindow", "X:"))
        self.translationYLabel.setText(_translate("TransformWindow", "Y:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.translationTab),
            _translate("TransformWindow", "Translation"),
        )
        self.reflectionXCheckBox.setText(_translate("TransformWindow", "X"))
        self.reflectionYCheckBox.setText(_translate("TransformWindow", "Y"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.reflectionTab),
            _translate("TransformWindow", "Reflection"),
        )
        self.rotationComboBox.setItemText(
            0, _translate("TransformWindow", "Rotate about the center of the object")
        )
        self.rotationComboBox.setItemText(
            1, _translate("TransformWindow", "Rotate about the origin")
        )
        self.rotationComboBox.setItemText(
            2, _translate("TransformWindow", "Rotate about a point")
        )
        self.rotationLabel.setText(_translate("TransformWindow", "Degrees:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.rotationTab),
            _translate("TransformWindow", "Rotation"),
        )
        self.scalingYLabel.setText(_translate("TransformWindow", "Y:"))
        self.scalingXLabel.setText(_translate("TransformWindow", "X:"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.scaleTab),
            _translate("TransformWindow", "Scaling"),
        )
        self.addTransformationPushButton.setText(
            _translate("TransformWindow", "Add Transformation")
        )

    def set_buttons_actions(self):
        pass

    def new_window(self):
        self.show()
