import GUI
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sc
from numpy import genfromtxt
from scipy.fftpack import rfft, irfft, fftfreq, ifft, fft
from scipy import signal
import os
import pyaudio
import struct
import time
from tkinter import TclError
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class TFApp(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        super(TFApp, self).__init__()
        self.setupUi(self)
        self.limit = 0.1
        self.clickFlag = 0
        self.mouseX = 0.0
        self.mouseY = 0.0
        
        circle1 = plt.Circle((0, 0), 1, fill=False)
        f = plt.figure()
        a = f.add_subplot(111)
        plt.grid(True) 
        a.add_artist(circle1)
        a.set_xlim(-1.1, +1.1)
        a.set_ylim(-1.1, +1.1)
        self.axis = a
        

        f2 = plt.figure()
        a2 = f2.add_subplot(111)
        a2.set_ylim(0, 2)
        plt.grid(True)    
        self.axis2 = a2

        f3 = plt.figure()
        a3 = f3.add_subplot(111)
        a3.set_ylim(-2, 2)
        plt.grid(True)
        self.axis3 = a3
    
        f4 = plt.figure()
        a4 = f4.add_subplot(111)
        a4.set_ylim(-2, 2)
        plt.grid(True)
        self.axis4 = a4
        
        f5 = plt.figure()
        a5 = f5.add_subplot(111)
        a5.set_ylim(-0.01, 0.5)
        plt.grid(True)
        self.axis5 = a5
        
        f6 = plt.figure()
        a6 = f6.add_subplot(111)
        a6.set_ylim(-100, 1000)
        plt.grid(True)
        self.axis6 = a6
        
        f7 = plt.figure()
        a7 = f7.add_subplot(111)
        a7.set_ylim(0, 255)
        a7.set_xlim(0, 2 * 1024)
        plt.grid(True)
        self.axis7 = a7
        
        f8 = plt.figure()
        a8 = f8.add_subplot(111)
        a8.set_ylim(-100, 1000)
        plt.grid(True)
        self.axis8 = a8   
        

        

        


        self.canvas_zplane = FigureCanvas(f)
        self.canvas_tf = FigureCanvas(f2)
        self.signalT1 = FigureCanvas(f3)
        self.signalT2 = FigureCanvas(f4)
        self.signalF1 = FigureCanvas(f5)
        self.signalF2 = FigureCanvas(f6)
        self.audioT = FigureCanvas(f7)
        self.audioF = FigureCanvas(f8)



        f.patch.set_facecolor('white')
        #for i in reversed(range(self.mplvlz.count())):
        #    self.mplvlz.itemAt(i).widget().deleteLater()
        self.mplvlz.addWidget(self.canvas_zplane)
        self.canvas_zplane.draw()
        
        self.mplvlt.addWidget(self.canvas_tf)
        self.canvas_tf.draw()
#        
        self.mplvls1.addWidget(self.signalT1)
        self.signalT1.draw()

        self.mplvls2.addWidget(self.signalT2)
        self.signalT2.draw()
    
        self.mplvls3.addWidget(self.signalF1)
        self.signalF1.draw()
        
        self.mplvls4.addWidget(self.signalF2)
        self.signalF2.draw()
        
        self.mplvls5.addWidget(self.audioT)
        self.audioT.draw()
        
        self.mplvls6.addWidget(self.audioF)
        self.audioF.draw()
        
        
        
        self.isPointAddable = False
        self.xPoint, self.yPoint = 0.0, 0.0
        self.canvas_zplane.mpl_connect('button_press_event', self.onMouseClick)
        self.canvas_zplane.mpl_connect('motion_notify_event', self.motion)
        self.canvas_zplane.mpl_connect('button_release_event', self.release)
        self.btn_add.clicked.connect(self.addPoint)
        self.btn_reset.clicked.connect(self.reset)
        
        self.Browse.clicked.connect(lambda: self.openFile(self.Browse))

        self.zeros, self.zerosXY, self.polesXY, self.poles = [], [], [], []
        self.files = ["Butterworth.xml", "Chebyshev.xml", "Lowpass.xml", "Highpass.xml"]

    def onMouseClick(self, event):
        self.clickFlag = 1
        self.isPointAddable = True
        ix, iy = float(event.xdata), float(event.ydata)
        self.xPoint, self.yPoint = ix, iy

        mytext = 'x = %f, y = %f' % (ix, iy)
        distance = np.sqrt(ix ** 2 + iy ** 2)
        if distance > 1.0:
            self.isPointAddable = False
            mytext = "Error: out of range"
        self.lbl_point.setText(mytext)

        if self.check_delete.isChecked():
            currentPoint = np.array([complex(ix, iy)])

            if len(self.zeros) > 0 and len(self.poles) > 0:
                dist1 = np.abs(currentPoint - self.zeros)
                leastDist1 = np.sort(dist1)[0]
                dist2 = np.abs(currentPoint - self.poles)
                leastDist2 = np.sort(dist2)[0]

                if leastDist1 <= leastDist2:
                    if np.sort(dist1)[0] <= self.limit:
                        idx1 = np.where(dist1 <= self.limit)[0][0]
                        del self.zeros[idx1]
                        del self.zerosXY[idx1]
                else:
                    if np.sort(dist2)[0] <= self.limit:
                        idx2 = np.where(dist2 <= self.limit)[0][0]
                        del self.poles[idx2]
                        del self.polesXY[idx2]


            elif len(self.zeros) > 0 >= len(self.poles):
                dist1 = np.abs(currentPoint - self.zeros)
                if np.sort(dist1)[0] <= self.limit:
                    idx1 = np.where(dist1 <= self.limit)[0][0]
                    del self.zeros[idx1]
                    del self.zerosXY[idx1]
            elif len(self.zeros) <= 0 < len(self.poles):
                dist2 = np.abs(currentPoint - self.poles)
                if np.sort(dist2)[0] <= self.limit:
                    idx2 = np.where(dist2 <= self.limit)[0][0]
                    del self.poles[idx2]
                    del self.polesXY[idx2]

            self.updateCircle()

    def release(self, event):
        self.clickFlag = 0
        count = 0
        if len(self.zeros) > len(self.poles):
            count = len(self.zeros)
        else:
            count = len(self.poles)
        self.table_points.setRowCount(count)
        range1 = np.arange(0, len(self.zeros), 1)
        for i in range1:
            self.table_points.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.zeros[i])))
        range1 = np.arange(0, len(self.poles), 1)
        for j in range1:
            self.table_points.setItem(j, 1, QtWidgets.QTableWidgetItem(str(self.poles[j])))

    def motion(self, event):
        self.mouseX = event.xdata
        self.mouseY = event.ydata

        if self.clickFlag == 1:
            self.lbl_point.setText('x = %f, y = %f' % (self.mouseX, self.mouseY))

            currentPoint = np.array([complex(self.mouseX, self.mouseY)])

            if len(self.zeros) > 0 and len(self.poles) > 0:
                dist1 = np.abs(currentPoint - self.zeros)
                leastDist1 = np.sort(dist1)[0]
                dist2 = np.abs(currentPoint - self.poles)
                leastDist2 = np.sort(dist2)[0]

                if leastDist1 <= leastDist2:
                    if np.sort(dist1)[0] <= self.limit:
                        idx1 = np.where(dist1 <= self.limit)[0][0]
                        self.zeros[idx1] = complex(round(self.mouseX, 5), round(self.mouseY, 5))
                        self.zerosXY[idx1] = (round(self.mouseX, 5), round(self.mouseY, 5))
                else:
                    if np.sort(dist2)[0] <= self.limit:
                        idx2 = np.where(dist2 <= self.limit)[0][0]
                        self.poles[idx2] = complex(round(self.mouseX, 5), round(self.mouseY, 5))
                        self.polesXY[idx2] = (round(self.mouseX, 5), round(self.mouseY, 5))

            elif len(self.zeros) > 0 >= len(self.poles):
                dist1 = np.abs(currentPoint - self.zeros)
                if np.sort(dist1)[0] <= self.limit:
                    idx1 = np.where(dist1 <= self.limit)[0][0]
                    self.zeros[idx1] = complex(round(self.mouseX, 5), round(self.mouseY, 5))
                    self.zerosXY[idx1] = (round(self.mouseX, 5), round(self.mouseY, 5))
            elif len(self.zeros) <= 0 < len(self.poles):
                dist2 = np.abs(currentPoint - self.poles)
                if np.sort(dist2)[0] <= self.limit:
                    idx2 = np.where(dist2 <= self.limit)[0][0]
                    self.poles[idx2] = complex(round(self.mouseX, 5), round(self.mouseY, 5))
                    self.polesXY[idx2] = (round(self.mouseX, 5), round(self.mouseY, 5))

            self.updateCircle()

    def addPoint(self):
        if self.isPointAddable:
            type = str(self.list_pointType.currentText())
            if type == 'Zero':
                zero = complex(round(self.xPoint, 5), round(self.yPoint, 5))
                self.zeros.append(zero)
                self.zerosXY.append([self.xPoint, self.yPoint])
                if len(self.zeros) >= self.table_points.rowCount():
                    self.table_points.setRowCount(len(self.zeros))
                self.table_points.setItem(len(self.zeros)-1, 0, QtWidgets.QTableWidgetItem(str(zero)))

            if type == 'Pole':
                pole = complex(round(self.xPoint, 5), round(self.yPoint, 5))
                self.poles.append(pole)
                self.polesXY.append([self.xPoint, self.yPoint])
                if len(self.poles) >= self.table_points.rowCount():
                    self.table_points.setRowCount(len(self.poles))
                self.table_points.setItem(len(self.poles)-1, 1, QtWidgets.QTableWidgetItem(str(pole)))
            self.updateCircle()

    def reset(self):
        self.updateAxisCircle()
        self.canvas_zplane.draw()
        self.isPointAddable = False
        self.xPoint, self.yPoint = 0.0, 0.0
        self.zeros, self.zerosXY, self.polesXY, self.poles = [], [], [], []
        self.lbl_point.setText('')
        self.table_points.setRowCount(0)
        self.canvas_zplane.mpl_connect('button_press_event', self.onMouseClick)
        self.canvas_zplane.mpl_connect('motion_notify_event', self.motion)
        self.canvas_zplane.mpl_connect('button_release_event', self.release)


    def column(self, matrix, i):
        return [row[i] for row in matrix]

    def updateAxisCircle(self):
        self.axis.cla()
        circle1 = plt.Circle((0, 0), 1, fill=False, ls='dashed')
        self.axis.add_artist(circle1)
        self.axis.set_xlim(-1.1, +1.1)
        self.axis.set_ylim(-1.1, +1.1)

    def updateCircle(self, k=1.0):
        self.updateAxisCircle()
        self.axis.plot(self.column(self.zerosXY, 0), self.column(self.zerosXY, 1), 'go', ms=7)
        self.axis.plot(self.column(self.polesXY, 0), self.column(self.polesXY, 1), 'rx', ms=7)
        self.axis.grid(True)
        self.canvas_zplane.draw()
        self.drawTransferFunction(k)


    def drawTransferFunction(self, k=1.0):
        self.axis2.cla()
        num, dom = sc.zpk2tf(self.zeros, self.poles, k)
        self.w, self.h = sc.freqz(num, dom)
        self.axis2.plot(self.w, abs(self.h))
        self.canvas_tf.draw()
        
        self.filtered = signal.convolve(self.yf, abs(self.h))
        self.axis6.cla()

        self.axis6.plot(self.filtered)
        self.signalF2.draw()
        
        backToTime= ifft(self.filtered)
        self.axis4.cla()
        self.axis4.plot(backToTime)
        self.signalT2.draw()
        
        
    def openFile(self,b):
        if b.text() == 'Browse': 
          filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
          data =genfromtxt(filename[0] , delimiter=',')
          N = 600
    # sample spacing
          T = 1.0 / 800.0
          self.yf = rfft(data[1,:])
          xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
          #self.ff= fft(data)
          self.axis3.plot(data[1,:])
          self.signalT1.draw()
 
          self.axis5.plot(xf, 2.0/N * np.abs(self.yf[:N//2]))
          self.signalF1.draw()
          

          
    def signalxfilter(self):
        s= np.sin(np.arange(0,1,0.1))
        self.filtered = signal.convolve(self.ff, s)
        self.axis6.plot(self.filtered)
        self.signalF2.draw()
        
        




def main():
    App = QtWidgets.QApplication(sys.argv)
    form = TFApp()
    form.show()
    App.exec_()


if __name__ == '__main__':
    main()
