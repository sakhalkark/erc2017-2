# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vyadh.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(906, 623)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(2, -1, 551, 321))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(240, 120, 59, 14))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.dial = QtGui.QDial(self.tab)
        self.dial.setGeometry(QtCore.QRect(90, 80, 121, 91))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(140, 60, 351, 151))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(550, 20, 351, 561))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 30, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 520, 101, 61))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton\n"
"{\n"
"background-color:red;\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"font-size:22px;\n"
"}"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(140, 400, 62, 24))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(140, 460, 62, 24))
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 320, 20, 261))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(380, 320, 20, 261))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(290, 400, 62, 24))
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(290, 460, 62, 24))
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(440, 400, 62, 24))
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(440, 460, 62, 24))
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 340, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 340, 81, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 350, 59, 14))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 360, 71, 121))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArm_Control_Calibrations = QtGui.QMenu(self.menubar)
        self.menuArm_Control_Calibrations.setObjectName(_fromUtf8("menuArm_Control_Calibrations"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArm_Control_Calibrations.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vyadh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gripper Control", None))
        self.label_6.setText(_translate("MainWindow", "backup controls in case the joystick controls fail", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Rover Control", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Telemetry Data</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "STOP", None))
        self.label_2.setText(_translate("MainWindow", "Base Arm", None))
        self.label_3.setText(_translate("MainWindow", "2nd Arm", None))
        self.label_4.setText(_translate("MainWindow", "3rd Arm", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Values in </p><p>degrees</p></body></html>", None))
        self.menuArm_Control_Calibrations.setTitle(_translate("MainWindow", "Arm Control Calibrations", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

