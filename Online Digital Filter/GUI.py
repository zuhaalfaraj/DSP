# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1228, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signalT1 = QtWidgets.QWidget(self.centralwidget)
        self.signalT1.setGeometry(QtCore.QRect(10, 60, 251, 141))
        self.signalT1.setObjectName("signalT1")
        self.signalF1 = QtWidgets.QWidget(self.centralwidget)
        self.signalF1.setGeometry(QtCore.QRect(290, 60, 251, 141))
        self.signalF1.setObjectName("signalF1")
        self.signalT2 = QtWidgets.QWidget(self.centralwidget)
        self.signalT2.setGeometry(QtCore.QRect(10, 250, 251, 141))
        self.signalT2.setObjectName("signalT2")
        self.signalF2 = QtWidgets.QWidget(self.centralwidget)
        self.signalF2.setGeometry(QtCore.QRect(290, 250, 251, 141))
        self.signalF2.setObjectName("signalF2")
        self.canvas_zplane = QtWidgets.QWidget(self.centralwidget)
        self.canvas_zplane.setGeometry(QtCore.QRect(550, 40, 421, 281))
        self.canvas_zplane.setObjectName("canvas_zplane")
        self.canvas_tf = QtWidgets.QWidget(self.centralwidget)
        self.canvas_tf.setGeometry(QtCore.QRect(620, 500, 521, 251))
        self.canvas_tf.setObjectName("canvas_tf")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 20, 211, 31))
        self.label_3.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 210, 181, 31))
        self.label_2.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label_2.setObjectName("label_2")
        self.check_delete = QtWidgets.QCheckBox(self.centralwidget)
        self.check_delete.setGeometry(QtCore.QRect(770, 360, 191, 22))
        self.check_delete.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.check_delete.setObjectName("check_delete")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 10, 67, 17))
        self.label_5.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 460, 271, 41))
        self.label_6.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label_6.setObjectName("label_6")
        self.list_pointType = QtWidgets.QComboBox(self.centralwidget)
        self.list_pointType.setGeometry(QtCore.QRect(580, 350, 181, 41))
        self.list_pointType.setObjectName("list_pointType")
        self.list_pointType.addItem("")
        self.list_pointType.addItem("")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(570, 400, 151, 31))
        self.btn_add.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);")
        self.btn_add.setObjectName("btn_add")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(10, 400, 151, 31))
        self.Browse.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);")
        self.Browse.setObjectName("Browse")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 330, 181, 21))
        self.label_7.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label_7.setObjectName("label_7")
        self.table_points = QtWidgets.QTableWidget(self.centralwidget)
        self.table_points.setGeometry(QtCore.QRect(990, 30, 211, 221))
        self.table_points.setObjectName("table_points")
        self.table_points.setColumnCount(2)
        self.table_points.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_points.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_points.setHorizontalHeaderItem(1, item)
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(730, 400, 151, 31))
        self.btn_reset.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);")
        self.btn_reset.setObjectName("btn_reset")
        self.lbl_point = QtWidgets.QLabel(self.centralwidget)
        self.lbl_point.setGeometry(QtCore.QRect(1010, 380, 221, 51))
        self.lbl_point.setText("")
        self.lbl_point.setObjectName("lbl_point")
        self.audioT = QtWidgets.QWidget(self.centralwidget)
        self.audioT.setGeometry(QtCore.QRect(20, 470, 521, 161))
        self.audioT.setObjectName("audioT")
        self.audioF = QtWidgets.QWidget(self.centralwidget)
        self.audioF.setGeometry(QtCore.QRect(20, 640, 521, 161))
        self.audioF.setObjectName("audioF")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 440, 181, 21))
        self.label_4.setStyleSheet("font: 75 italic 14pt \"Nimbus Roman No9 L\";\n"
"font: 14pt \"Ubuntu Mono\";")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1228, 25))
        self.menubar.setObjectName("menubar")
        self.menuTask03_Group03 = QtWidgets.QMenu(self.menubar)
        self.menuTask03_Group03.setObjectName("menuTask03_Group03")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTask03_Group03.menuAction())
        
        
        self.mplvlz = QtWidgets.QVBoxLayout(self.canvas_zplane)
        self.mplvlz.setObjectName("mplvlz")
        
        self.mplvlt = QtWidgets.QVBoxLayout(self.canvas_tf)
        self.mplvlt.setObjectName("mplvlt")
        
        self.mplvls1 = QtWidgets.QVBoxLayout(self.signalT1)
        self.mplvls1.setObjectName("mplvlt")
        
        self.mplvls2 = QtWidgets.QVBoxLayout(self.signalT2)
        self.mplvls2.setObjectName("mplvlt")
        
        self.mplvls3 = QtWidgets.QVBoxLayout(self.signalF1)
        self.mplvls3.setObjectName("mplvlt")
        
        self.mplvls4 = QtWidgets.QVBoxLayout(self.signalF2)
        self.mplvls4.setObjectName("mplvlt")
        
        self.mplvls5 = QtWidgets.QVBoxLayout(self.audioT)
        self.mplvls5.setObjectName("mplvlt")
        
        self.mplvls6 = QtWidgets.QVBoxLayout(self.audioF)
        self.mplvls6.setObjectName("mplvlt")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Time Domain"))
        self.label_3.setText(_translate("MainWindow", "Frequency Domain "))
        self.label_2.setText(_translate("MainWindow", "After filteration"))
        self.check_delete.setText(_translate("MainWindow", "Enable Deletion"))
        self.label_5.setText(_translate("MainWindow", "Z-Plane"))
        self.label_6.setText(_translate("MainWindow", "Bode Polt Response"))
        self.list_pointType.setItemText(0, _translate("MainWindow", "Zero"))
        self.list_pointType.setItemText(1, _translate("MainWindow", "Pole"))
        self.btn_add.setText(_translate("MainWindow", "Add Point"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.label_7.setText(_translate("MainWindow", "Type of Point:"))
        item = self.table_points.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Zeros"))
        item = self.table_points.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Poles"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.label_4.setText(_translate("MainWindow", "Realtime Audio"))
        self.menuTask03_Group03.setTitle(_translate("MainWindow", "Task03 - Group03"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

