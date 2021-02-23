from PyQt5 import QtCore, QtWidgets
from utils import transformations_codes


class TransformWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(560, 360)
        self.setObjectName("TransformWindow")
        self.partnerDialog = parent
        self.next_id = 0
        self.setup()

    def setup(self):
        self.transformLabel = QtWidgets.QLabel(self)
        self.transformLabel.setGeometry(QtCore.QRect(10, 10, 151, 17))
        self.transformLabel.setObjectName("transformLabel")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 171, 261))
        self.listWidget.setObjectName("listWidget")

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
        self.reflectionOriginCheckBox = QtWidgets.QCheckBox(self.reflectionTab)
        self.reflectionOriginCheckBox.setGeometry(QtCore.QRect(20, 80, 92, 23))
        self.reflectionOriginCheckBox.setObjectName("reflectionOriginCheckBox")
        self.tabWidget.addTab(self.reflectionTab, "")

        self.addTransformationPushButton = QtWidgets.QPushButton(self)
        self.addTransformationPushButton.setGeometry(QtCore.QRect(380, 300, 171, 25))
        self.addTransformationPushButton.setObjectName("addTransformationPushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.tabWidget.setCurrentIndex(0)
        self.connect_actions()


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
        self.reflectionOriginCheckBox.setText(_translate("TransformWindow", "Origin"))
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

    def new_window(self, active_wireframe):
        self.wireframe = active_wireframe
        self.update_transformations_list()
        self.show()

    def update_transformations_list(self):
        self.listWidget.clear()
        self.next_id = 0
        for code in self.wireframe.transformations_codes:
            item = f'{transformations_codes[code[0]]} {self.next_id}'
            self.listWidget.insertItem(self.next_id, item)
            self.next_id += 1
    
    def add_last_n_transformations_to_list(self, n):
        codes = self.wireframe.transformations_codes[-n:]
        for code in codes:
            transformation = transformations_codes[code[0]]
            item = f'{transformation} {self.next_id}'
            self.listWidget.insertItem(self.next_id, item)
            self.next_id += 1
    
    def connect_actions(self):
        self.addTransformationPushButton.clicked.connect(self.add_transformation)
        self.deleteTransformationPushButton.clicked.connect(self.delete_transformation)
        self.listWidget.currentItemChanged.connect(self.show_transformation)

    def delete_transformation(self):
        transformations = len(self.wireframe.transformations_codes)
        if transformations > 0:
            item = self.listWidget.currentRow()
            self.listWidget.takeItem(item)
            transformation = self.wireframe.transformations_codes.pop(item)
            name = f'{transformations_codes[transformation[0]]}'
            self.partnerDialog.console_print(f"{name} removed!")
            self.wireframe.apply_transformations_to_points()
            self.partnerDialog.redraw_wireframes()

    def add_transformation(self):
        active_tab = self.tabWidget.currentIndex()
        print(active_tab)
        self.tab_index_to_function[active_tab][0](self)
        self.wireframe.apply_transformations_to_points()
        self.partnerDialog.redraw_wireframes()

    def add_rotation(self):
        degrees = self.rotationText.toPlainText()
        if degrees != '':
            self.wireframe.transformations_codes.append(('rt', [float(degrees)]))
            self.add_last_n_transformations_to_list(1)

    def show_rotation(self, degrees):
        self.rotationText.setText(str(degrees))

    def add_translation(self):
        x_text = self.translationXTextEdit.toPlainText()
        y_text = self.translationYTextEdit.toPlainText()
        x = float(x_text) if x_text != "" else 0
        y = float(y_text) if y_text != "" else 0
        self.wireframe.transformations_codes.append(('tr', [x, y]))
        self.add_last_n_transformations_to_list(1)
    
    def show_translation(self, x, y):
        self.translationXTextEdit.setText(str(x))
        self.translationYTextEdit.setText(str(y))

    def add_scaling(self):
        x_text = self.scalingXTextEdit.toPlainText()
        y_text = self.scalingYTextEdit.toPlainText()
        x = float(x_text) if x_text != "" else 1
        y = float(y_text) if y_text != "" else 1
        self.wireframe.transformations_codes.append(('sc', [x, y]))
        self.add_last_n_transformations_to_list(1)
    
    def show_scaling(self, x, y):
        self.scalingXTextEdit.setText(str(x))
        self.scalingYTextEdit.setText(str(y))

    def add_reflection(self):
        count = 0
        if self.reflectionXCheckBox.isChecked():
            self.wireframe.transformations_codes.append(('rf', ['x']))
            count += 1
        if self.reflectionYCheckBox.isChecked():
            self.wireframe.transformations_codes.append(('rf', ['y']))
            count += 1
        if self.reflectionOriginCheckBox.isChecked():
            self.wireframe.transformations_codes.append(('rf', ['origin']))
            count += 1
        self.add_last_n_transformations_to_list(count)
    
    def show_reflection(self, rtype):
        self.reflectionXCheckBox.setChecked(False)
        self.reflectionYCheckBox.setChecked(False)
        self.reflectionOriginCheckBox.setChecked(False)
        if rtype == 'x':
            self.reflectionXCheckBox.setChecked(True)
        elif rtype == 'y':
            self.reflectionYCheckBox.setChecked(True)
        elif rtype == 'origin':
            self.reflectionOriginCheckBox.setChecked(True)

    tab_index_to_function = {
        0: (add_rotation, show_rotation),
        1: (add_translation, show_translation),
        2: (add_scaling, show_scaling),
        3: (add_reflection, show_reflection)
    }

    transformation_name_to_index = {
        'Rotation': 0,
        'Translation': 1,
        'Scaling': 2,
        'Reflection': 3
    }

    def show_transformation(self):
        item = self.listWidget.currentItem()
        try:
            item_name = item.text().split()[0]
            new_index = self.transformation_name_to_index[item_name]
            self.tabWidget.setCurrentIndex(new_index)

            row = self.listWidget.currentRow()
            transformation_code = self.wireframe.transformations_codes[row]
            params = transformation_code[1]
            self.tab_index_to_function[new_index][1](self, *params)
        except AttributeError:
            self.partnerDialog.console_print('Error parsing current transformation')
        
