# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task04.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1674, 813)
        MainWindow.setMinimumSize(QtCore.QSize(145, 63))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TP = QtWidgets.QWidget(self.centralwidget)
        self.TP.setGeometry(QtCore.QRect(870, 40, 361, 151))
        self.TP.setObjectName("TP")
        self.TA = QtWidgets.QWidget(self.centralwidget)
        self.TA.setGeometry(QtCore.QRect(1240, 40, 401, 151))
        self.TA.setObjectName("TA")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 0, 151, 41))
        self.label_3.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1370, 0, 151, 41))
        self.label_4.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_4.setObjectName("label_4")
        self.v8 = QtWidgets.QSlider(self.centralwidget)
        self.v8.setGeometry(QtCore.QRect(310, 10, 29, 160))
        self.v8.setOrientation(QtCore.Qt.Vertical)
        self.v8.setObjectName("v8")
        self.v7 = QtWidgets.QSlider(self.centralwidget)
        self.v7.setGeometry(QtCore.QRect(260, 10, 29, 160))
        self.v7.setOrientation(QtCore.Qt.Vertical)
        self.v7.setObjectName("v7")
        self.v6 = QtWidgets.QSlider(self.centralwidget)
        self.v6.setGeometry(QtCore.QRect(210, 10, 29, 160))
        self.v6.setOrientation(QtCore.Qt.Vertical)
        self.v6.setObjectName("v6")
        self.v5 = QtWidgets.QSlider(self.centralwidget)
        self.v5.setGeometry(QtCore.QRect(160, 10, 29, 160))
        self.v5.setOrientation(QtCore.Qt.Vertical)
        self.v5.setObjectName("v5")
        self.v4 = QtWidgets.QSlider(self.centralwidget)
        self.v4.setGeometry(QtCore.QRect(120, 10, 29, 160))
        self.v4.setOrientation(QtCore.Qt.Vertical)
        self.v4.setObjectName("v4")
        self.v3 = QtWidgets.QSlider(self.centralwidget)
        self.v3.setGeometry(QtCore.QRect(80, 10, 29, 160))
        self.v3.setOrientation(QtCore.Qt.Vertical)
        self.v3.setObjectName("v3")
        self.v2 = QtWidgets.QSlider(self.centralwidget)
        self.v2.setGeometry(QtCore.QRect(40, 10, 29, 160))
        self.v2.setOrientation(QtCore.Qt.Vertical)
        self.v2.setObjectName("v2")
        self.v1 = QtWidgets.QSlider(self.centralwidget)
        self.v1.setGeometry(QtCore.QRect(0, 10, 29, 160))
        self.v1.setOrientation(QtCore.Qt.Vertical)
        self.v1.setObjectName("v1")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(160, 190, 151, 31))
        self.browse.setStyleSheet("font: 57 italic 16pt \"URW Chancery L\";\n"
"color: rgb(255, 0, 127);")
        self.browse.setObjectName("browse")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(0, 190, 151, 31))
        self.play.setStyleSheet("font: 57 italic 16pt \"URW Chancery L\";\n"
"color: rgb(255, 0, 127);")
        self.play.setObjectName("play")
        self.FR = QtWidgets.QWidget(self.centralwidget)
        self.FR.setGeometry(QtCore.QRect(160, 540, 341, 201))
        self.FR.setObjectName("FR")
        self.playr = QtWidgets.QPushButton(self.centralwidget)
        self.playr.setGeometry(QtCore.QRect(0, 610, 151, 31))
        self.playr.setStyleSheet("font: 57 italic 16pt \"URW Chancery L\";\n"
"color: rgb(255, 0, 127);")
        self.playr.setObjectName("playr")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(0, 550, 151, 31))
        self.record.setStyleSheet("font: 57 italic 16pt \"URW Chancery L\";\n"
"color: rgb(255, 0, 127);")
        self.record.setObjectName("record")
        self.tf = QtWidgets.QWidget(self.centralwidget)
        self.tf.setGeometry(QtCore.QRect(360, 60, 411, 161))
        self.tf.setObjectName("tf")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 151, 41))
        self.label_6.setStyleSheet("color: rgb(255, 0, 127);\n"
"text-decoration: underline;\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 470, 151, 41))
        self.label_7.setStyleSheet("color: rgb(255, 0, 127);\n"
"text-decoration: underline;\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_7.setObjectName("label_7")
        self.PR = QtWidgets.QWidget(self.centralwidget)
        self.PR.setGeometry(QtCore.QRect(510, 540, 341, 201))
        self.PR.setObjectName("PR")
        self.FRA = QtWidgets.QWidget(self.centralwidget)
        self.FRA.setGeometry(QtCore.QRect(860, 540, 341, 201))
        self.FRA.setObjectName("FRA")
        self.PRA = QtWidgets.QWidget(self.centralwidget)
        self.PRA.setGeometry(QtCore.QRect(1210, 540, 341, 201))
        self.PRA.setObjectName("PRA")
        self.FA = QtWidgets.QWidget(self.centralwidget)
        self.FA.setGeometry(QtCore.QRect(160, 280, 341, 201))
        self.FA.setObjectName("FA")
        self.FP = QtWidgets.QWidget(self.centralwidget)
        self.FP.setGeometry(QtCore.QRect(510, 280, 341, 201))
        self.FP.setObjectName("FP")
        self.FAA = QtWidgets.QWidget(self.centralwidget)
        self.FAA.setGeometry(QtCore.QRect(860, 280, 341, 201))
        self.FAA.setObjectName("FAA")
        self.FPA = QtWidgets.QWidget(self.centralwidget)
        self.FPA.setGeometry(QtCore.QRect(1210, 280, 341, 201))
        self.FPA.setObjectName("FPA")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 10, 151, 41))
        self.label_8.setStyleSheet("color: rgb(255, 0, 127);\n"
"text-decoration: underline;\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(790, 0, 151, 41))
        self.label_9.setStyleSheet("color: rgb(255, 0, 127);\n"
"text-decoration: underline;\n"
"font: 57 italic 11pt \"Ubuntu\";\n"
"font: 57 italic 12pt \"Ubuntu\";\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 240, 151, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 240, 151, 41))
        self.label_10.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(910, 230, 151, 41))
        self.label_11.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1310, 230, 151, 41))
        self.label_12.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_12.setObjectName("label_12")
        self.disRec = QtWidgets.QPushButton(self.centralwidget)
        self.disRec.setGeometry(QtCore.QRect(1060, 200, 141, 21))
        self.disRec.setStyleSheet("font: 57 italic 16pt \"URW Chancery L\";\n"
"color: rgb(255, 0, 127);")
        self.disRec.setObjectName("disRec")
        self.disFile = QtWidgets.QPushButton(self.centralwidget)
        self.disFile.setGeometry(QtCore.QRect(1220, 200, 141, 21))
        self.disFile.setStyleSheet("font: 57 italic 16pt \"URW Chancery L\";\n"
"color: rgb(255, 0, 127);")
        self.disFile.setObjectName("disFile")
        self.filType = QtWidgets.QComboBox(self.centralwidget)
        self.filType.setGeometry(QtCore.QRect(500, 20, 171, 31))
        self.filType.setObjectName("filType")
        self.filType.addItem("")
        self.filType.addItem("")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(220, 490, 171, 41))
        self.label_13.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(920, 490, 171, 41))
        self.label_14.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(570, 490, 171, 41))
        self.label_15.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1300, 490, 171, 41))
        self.label_16.setStyleSheet("color: rgb(255, 0, 127);\n"
"font: 57 italic 16pt \"URW Chancery L\";")
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1674, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        
        self.mplvl1 = QtWidgets.QVBoxLayout(self.tf)
        
        self.mplvl2 = QtWidgets.QVBoxLayout(self.TP)
        
        self.mplvl3 = QtWidgets.QVBoxLayout(self.TA)
        
        self.mplvl4 = QtWidgets.QVBoxLayout(self.FA)
        
        self.mplvl5 = QtWidgets.QVBoxLayout(self.FP)
        
        self.mplvl6 = QtWidgets.QVBoxLayout(self.FAA)
       
        self.mplvl7 = QtWidgets.QVBoxLayout(self.FPA)
        
        self.mplvl8= QtWidgets.QVBoxLayout(self.FR)
        
        self.mplvl9 = QtWidgets.QVBoxLayout(self.PR)
        
        self.mplvl10= QtWidgets.QVBoxLayout(self.FRA)
               
        self.mplvl11= QtWidgets.QVBoxLayout(self.PRA)
        
        f1 = plt.figure()
        a1 = f1.add_subplot(111)
        a1.set_ylim(-2, 2)
        self.axis1 = a1
    

        f2 = plt.figure()
        a2 = f2.add_subplot(111)
        self.axis2 = a2
        
        f3 = plt.figure()
        a3= f3.add_subplot(111)
        a3.set_ylim(0, 10)
        a3.set_xlim(0, 300)

        self.axis3 = a3
    

        f4 = plt.figure()
        a4 = f4.add_subplot(111)
        self.axis4 = a4
        
        f5= plt.figure()
        a5 = f5.add_subplot(111)
        self.axis5 = a5
    

        f6 = plt.figure()
        a6 = f6.add_subplot(111)
        self.axis6 = a6
        
        f7 = plt.figure()
        a7 = f7.add_subplot(111)
        a7.set_xlim(0,20000)
        self.axis7 = a7
        
        f8 = plt.figure()
        a8 = f8.add_subplot(111)
        self.axis8 = a8
        
        f9 = plt.figure()
        a9= f9.add_subplot(111)
        a9.set_ylim(0, 10)
        self.axis9 = a9
    

        f10 = plt.figure()
        a10 = f10.add_subplot(111)
        self.axis10 = a10
        
        f11= plt.figure()
        a11 = f11.add_subplot(111)
        self.axis11 = a11
    
        self.tf = FigureCanvas(f1)
        self.TP = FigureCanvas(f2)
        self.TA = FigureCanvas(f3)
        self.FA = FigureCanvas(f4)
        self.FP = FigureCanvas(f5)
        self.FAA = FigureCanvas(f6)
        self.FPA = FigureCanvas(f7)
        self.FR = FigureCanvas(f8)
        self.PR = FigureCanvas(f9)
        self.FRA = FigureCanvas(f10)
        self.PRA = FigureCanvas(f11)

        
        self.mplvl1.addWidget(self.tf)
        self.tf.draw()
        
        self.mplvl2.addWidget(self.TP)
        self.TP.draw()
        
        self.mplvl3.addWidget(self.TA)
        self.TA.draw()
        
        self.mplvl4.addWidget(self.FA)
        self.FA.draw()
        
        self.mplvl5.addWidget(self.FP )
        self.FP.draw()
        
        self.mplvl6.addWidget(self.FAA)
        self.FAA.draw()
        
        self.mplvl7.addWidget(self.FPA)
        self.FPA.draw()
        
        self.mplvl8.addWidget(self.FR)
        self.FR.draw()
        
        self.mplvl9.addWidget(self.PR )
        self.PR.draw()
        
        self.mplvl10.addWidget(self.FRA)
        self.FRA.draw()
        
        self.mplvl11.addWidget(self.PRA)
        self.PRA.draw()
        
        minimum=0
        maximum= 2
        self.v1.setMinimum(minimum)
        self.v1.setMaximum(maximum)
        self.v1.setValue(0)
        
        self.v2.setMinimum(minimum)
        self.v2.setMaximum(maximum)
        self.v2.setValue(0)
         
        self.v3.setMinimum(minimum)
        self.v3.setMaximum(maximum)
        self.v3.setValue(0)
        
        self.v4.setMinimum(minimum)
        self.v4.setMaximum(maximum)
        self.v4.setValue(0)

        self.v5.setMinimum(minimum)
        self.v5.setMaximum(maximum)
        self.v5.setValue(0)

        self.v6.setMinimum(minimum)
        self.v6.setMaximum(maximum)
        self.v6.setValue(0)

        
        self.v7.setMinimum(minimum)
        self.v7.setMaximum(maximum)
        self.v7.setValue(0)

        self.v8.setMinimum(minimum)
        self.v8.setMaximum(maximum)
        self.v8.setValue(0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Before"))
        self.label_4.setText(_translate("MainWindow", "After"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.playr.setText(_translate("MainWindow", "Play Record"))
        self.record.setText(_translate("MainWindow", "Record"))
        self.label_6.setText(_translate("MainWindow", "Frequancy Domain"))
        self.label_7.setText(_translate("MainWindow", "Online (Recording)"))
        self.label_8.setText(_translate("MainWindow", "Response"))
        self.label_9.setText(_translate("MainWindow", "Time Domain"))
        self.label_5.setText(_translate("MainWindow", "Amplitude(Before)"))
        self.label_10.setText(_translate("MainWindow", "Phase(Before)"))
        self.label_11.setText(_translate("MainWindow", "Amplitude(After)"))
        self.label_12.setText(_translate("MainWindow", "Phase (After)"))
        self.disRec.setText(_translate("MainWindow", "Display Record"))
        self.disFile.setText(_translate("MainWindow", "Display file"))
        self.filType.setItemText(0, _translate("MainWindow", "Online"))
        self.filType.setItemText(1, _translate("MainWindow", "Offline"))
        self.label_13.setText(_translate("MainWindow", "Time Domain(Before)"))
        self.label_14.setText(_translate("MainWindow", "Time Domain(After)"))
        self.label_15.setText(_translate("MainWindow", "Spectrum(Before)"))
        self.label_16.setText(_translate("MainWindow", "Spectrum(After)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

