# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyPlugin_1.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.pushButton_Manual = QtGui.QPushButton(Form)
        self.pushButton_Manual.setGeometry(QtCore.QRect(0, 30, 401, 48))
        self.pushButton_Manual.setObjectName(_fromUtf8("pushButton_Manual"))
        self.pushButton_Autonomy = QtGui.QPushButton(Form)
        self.pushButton_Autonomy.setGeometry(QtCore.QRect(0, 100, 401, 48))
        self.pushButton_Autonomy.setObjectName(_fromUtf8("pushButton_Autonomy"))
        self.pushButton_STOP = QtGui.QPushButton(Form)
        self.pushButton_STOP.setGeometry(QtCore.QRect(0, 170, 401, 48))
        self.pushButton_STOP.setObjectName(_fromUtf8("pushButton_STOP"))

        #trying out to test a button
        self.submit_button.clicked.connect(showSTOP)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_Manual.setText(_translate("Form", "Manual Movement", None))
        self.pushButton_Autonomy.setText(_translate("Form", "Autonomous Movement", None))
        self.pushButton_STOP.setText(_translate("Form", "STOP", None))

    def showStop(self):
        QtWidgets.QMessageBox.information(self, "STOPPP")
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

