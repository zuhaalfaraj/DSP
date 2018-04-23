import GUI4
from PyQt5 import QtWidgets
import sys
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from PyQt5.QtWidgets import QFileDialog
from scipy.io import wavfile
import sounddevice as sd
import scipy
from scipy.signal import butter, lfilter
from scipy.signal import freqz
from scipy import signal 


class Equalizer(QtWidgets.QMainWindow, GUI4.Ui_MainWindow):
     def __init__(self):
        super(Equalizer, self).__init__()
        self.setupUi(self)
        self.samplerate = 44100
        self.order=3
        self.a=[2756.25, 5512.5, 8268.75, 11025.0, 13781.25, 16537.5, 19293.75, 22050.0]
        x= np.zeros([100,100])
        self.data , self.myrecording, self.datatoF , self.myrecordingtoF, self.times =x,x,x,x,x
        self.filData , self.filRec, self.filDatatoF , self.filRectoF =x,x,x,x
        self.Phase= np.zeros(self.data.shape[0])
        self.data = np.sin(30.0 * 2.0*np.pi*x) +np.sin(120.0 * 2.0*np.pi*x)+np.sin(210.0 * 2.0*np.pi*x)
        self.data+= np.sin(330.0 * 2.0*np.pi*x)
        self.data+= np.sin(170.0 * 2.0*np.pi*x)
        self.data+= np.sin(260.0 * 2.0*np.pi*x)
        
        self.v1.valueChanged.connect(self.v_change)
        self.v2.valueChanged.connect(self.v_change)
        self.v3.valueChanged.connect(self.v_change)
        self.v4.valueChanged.connect(self.v_change)
        self.v5.valueChanged.connect(self.v_change)
        self.v6.valueChanged.connect(self.v_change)
        self.v7.valueChanged.connect(self.v_change)
        self.v8.valueChanged.connect(self.v_change)
        
        self.browse.clicked.connect(lambda: self.openFile(self.browse))
        self.play.clicked.connect(self.playSound)
        
        self.disFile.clicked.connect(lambda: self.time_domain(self.disFile))
        self.disRec.clicked.connect(lambda: self.time_domain(self.disRec))
        
        self.record.clicked.connect(self.recordSound )
        self.playr.clicked.connect(self.playRecord )
        
     def inverseFT(self,y):
        newData=ifft(y).real
        newData=np.around(newData, 2)
        newData= newData.astype(np.int16)
        return newData
     
     def Fourier(self,y, N):        
         newData=fft(y)
         newData= 2.0/N * np.abs(newData[:N//2])
         return newData
     
     def Phase_(self,y):
         data= fft(y)
         phase= np.angle(data)
         return phase
     
     def IIR(self,lowcut, highcut, fs, order):
         nyq = 0.5 * fs
         low = lowcut / nyq
         high = highcut / nyq
         b, a = signal.iirfilter(3, [low, high], rs=60, btype='band', ftype='butter')
         return b,a

     def IIR_filter(self,data, lowcut, highcut, fs, order):
         b,a = self.IIR(lowcut, highcut, fs, order=order)
         y = lfilter(b, a, data)
         return y   
     
     def openFile(self,b):
         self.axis2.cla()
         if b.text() == 'Browse': 
             filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
             self.samplerate, self.data = wavfile.read(filename[0] )
             self.data = self.data[:,0]
             self.samplerate = 44100
             self.data = self.data
             self.times = np.arange(len(self.data))/float(self.samplerate)
             self.filData =self.data
             self.Phase = np.zeros(self.data.shape[0])

             self.plot_file()

     
     def playSound(self):
         sd.play(self.filData)
         
     def recordSound(self):  
        duration = 2.5  # seconds       
        self.myrecording = sd.rec(int(duration * self.samplerate), samplerate=self.samplerate, channels=2,  blocking=True)
        self.myrecording =self.myrecording[:,0]
        self.plot_record()
        



        
     def playRecord(self):
        sd.play(self.filRec)
        
    
     def v_change(self):
         
         self.sl1 = str(self.v1.value())
         self.sl2 = str(self.v2.value())
         self.sl3 = str(self.v3.value())
         self.sl4 = str(self.v4.value())
         self.sl5 = str(self.v5.value())
         self.sl6 = str(self.v6.value())
         self.sl7 = str(self.v7.value())
         self.sl8 = str(self.v8.value())
         
         type = str(self.filType.currentText())
         
         if type == "Online":
             
             fs = 44100.0
             order=3
             a=[2756.25, 5512.5, 8268.75, 11025.0, 13781.25, 16537.5, 19293.75, 22050.0]
             wo=2756
             
             b1,a1 =self.IIR( 0, a[0], fs, order)
             w, h1 = freqz( b1,a1, worN=wo)
         
             b2,a2 = self.IIR( a[0], a[1], fs, order)
             w, h2 = freqz( b2,a2, worN=wo)
          
             b3,a3= self.IIR(a[1],a[2], fs, order)
             w, h3 = freqz( b3,a3, worN=wo)
    
             b4,a4= self.IIR( a[2], a[3], fs, order)
             w, h4 = freqz( b4,a4, worN=wo)
         
             b5,a5= self.IIR(a[3], a[4], fs, order)
             w, h5 = freqz( b5,a5, worN=wo)
         
             b6,a6= self.IIR(a[4], a[5], fs, order)
             w, h6 = freqz( b6,a6, worN=wo)

             b7,a7= self.IIR(a[5],a[6], fs, order)
             w, h7 = freqz( b5,a5, worN=wo)
         
             b8,a8= self.IIR(a[6], a[7], fs, order)
             w, h8 = freqz( b6,a6, worN=wo)   
             

             r1= abs(h1)*float(self.sl1)
             r2= abs(h2)*float(self.sl2)
             r3= abs(h3)*float(self.sl3)
             r4= abs(h4)*float(self.sl4)
             r5= abs(h5)*float(self.sl5)
             r6= abs(h6)*float(self.sl6)
             r7= abs(h7)*float(self.sl7)
             r8= abs(h8)*float(self.sl8)         
             #r=np.concatenate((r1,r2,r3,r4,r5,r6,r7,r8),axis=0)
             r = r1+r2+r3+r4+r5+r6+r7+r8
             x= np.arange(0,r.shape[0],1)
         
             self.axis1.cla()
             self.axis1.plot((fs * 0.5 / np.pi) * x,r)
             self.tf.draw()
         
             self.file_response()
             self.record_response()
             
         else:
             N= self.filData.shape[0]
             T= 1/ self.samplerate
             xf = np.linspace(0.0, 1.0/(2.0*T), N/2) 
             
             self.datatoF= 2.0/N * np.abs(fft(self.data)[:N//2])
             delta=round(self.datatoF.shape[0]/8)
             d= [0, delta, 2*delta , 3*delta, 4*delta , 5*delta , 6*delta , 7*delta, 8*delta]


             data1 = self.datatoF[:d[1]]*float(self.sl1)
             data1 = data1*np.hamming(data1.shape[0])
             
             data2 = self.datatoF[d[1]:d[2]]*float(self.sl2)
             data2 = data2*np.hamming(data2.shape[0])
             
             
             data3 = self.datatoF[d[2]:d[3]]*float(self.sl3)
             data3 = data3*np.hamming(data3.shape[0])
             
             
             data4 = self.datatoF[d[3]:d[4]]*float(self.sl4)
             data4 = data4*np.hamming(data4.shape[0])
             
             
             data5 = self.datatoF[d[4]:d[5]]*float(self.sl5)
             data5 = data5*np.hamming(data5.shape[0])
             
             
             data6 = self.datatoF[d[5]:d[6]]*float(self.sl6)
             data6 = data6*np.hamming(data6.shape[0])
             
             
             data7 = self.datatoF[d[6]:d[7]]*float(self.sl7)
             data7= data7*np.hamming(data7.shape[0])
             
             data8 = self.datatoF[d[7]:d[8]]*float(self.sl8)
             data8 = data8*np.hamming(data8.shape[0])
             
             self.filDatatoF = np.concatenate((data1,data2,data3,data4,data5,data6,data7,data8), axis=0)
             #self.filData = ifft(self.filDatatoF)

            
             self.axis1.cla()
             self.axis1.plot(self.filDatatoF)
             self.tf.draw()
             
             self.axis3.cla()
             self.axis3.plot(ifft(self.filDatatoF))
             self.axis3.set_xlim(0,300)
             self.TA.draw()
             
             self.axis2.cla()
             self.axis2.plot(self.data)
             self.axis2.set_xlim(0,300)
             self.TP.draw()
#             
#             self.file_response()
             
         
     def file_response(self):
             N= self.filData.shape[0]
             T= 1/ self.samplerate
             xf = np.linspace(0.0, 1.0/(2.0*T), N/2)          
             
             
             arr= [self.sl1,self.sl2,self.sl3,self.sl4,self.sl5,self.sl6,self.sl7,self.sl8]
             
             self.filData=self.IIR_filter(self.data,0, self.a[0], self.samplerate, self.order)*float(arr[0])
             self.filData+=self.IIR_filter(self.data,self.a[0],self.a[1], self.samplerate, self.order)*float(arr[1])
             self.filData+=self.IIR_filter(self.data,self.a[1],self.a[2], self.samplerate, self.order)*float(arr[2])
             self.filData+=self.IIR_filter(self.data,self.a[2],self.a[3], self.samplerate, self.order)*float(arr[3])
             self.filData+=self.IIR_filter(self.data,self.a[3],self.a[4], self.samplerate, self.order)*float(arr[4])
             self.filData+=self.IIR_filter(self.data,self.a[4],self.a[5], self.samplerate, self.order)*float(arr[5])
             self.filData+=self.IIR_filter(self.data,self.a[5],self.a[6], self.samplerate, self.order)*float(arr[6])
             self.filData+=self.IIR_filter(self.data,self.a[6],self.a[7], self.samplerate, self.order)*float(arr[7])
             
#             for i in range (7):
#                 I =self.IIR_filter(self.data,self.a[i], self.a[i+1], self.samplerate, self.order)*float(arr[i])
#                 self.filData+=I


             self.filDatatoF= self.Fourier(self.filData, self.filData.shape[0])
             self.axis6.cla()
         
             self.axis6.plot(xf, 2.0/N * np.abs(fft(self.filData)[:N//2]))
             self.axis6.set_ylim(0,200)
             self.FAA.draw()
         
         
             self.axis7.cla()
             self.axis7.plot(self.Phase_(self.filData))
             self.axis7.set_xlim(0,7000)
             self.FPA.draw()  
         
             
             self.axis2.cla()
                      #self.axis2.set_xlim(self.times[0], self.times[-1])
             self.axis3.set_ylim(-20000, 20000)
             self.axis2.set_xlim(0,300)

             self.axis2.plot( self.data)
             self.TP.draw()
                      
             self.axis3.cla()
             self.axis3.plot(self.filData)
             self.axis3.set_ylim(-20000, 20000)
             self.axis3.set_xlim(0,300)
             self.TA.draw()
             
                      
             
             
             

            
     def record_response(self):
         arr= [self.sl1,self.sl2,self.sl3,self.sl4,self.sl5,self.sl6,self.sl7,self.sl8]
         self.filRec=self.IIR_filter(self.myrecording ,0, self.a[0], self.samplerate, self.order)*float(arr[0])
         for i in range(7):
             I =self.IIR_filter(self.myrecording,self.a[i], self.a[i+1], self.samplerate, self.order)*float(arr[i])
             self.filRec+=I
          
         N= self.filRec.shape[0]
         T=1/self.samplerate
         xf= np.linspace(0.0, 1.0/(2.0*T), N/2)
         
         self.axis11.cla()
         self.axis11.set_ylim(0,0.01)
         self.axis11.plot(xf, 2.0/N * np.abs(fft(self.filRec)[:N//2]))
         self.PRA.draw()  
         
         self.axis10.cla()
         self.axis10.set_ylim(-0.5,0.5)
         self.axis10.plot(self.filRec)
         self.FRA.draw() 
         

             
         
     def plot_file(self): #plot The original signal from file 
         
         
         N= self.data.shape[0]
         T= 1/ self.samplerate
         self.datatoF = fft(self.data)
         xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
         
         self.axis4.cla()
         self.axis4.plot(xf, 2.0/N * np.abs(fft(self.data)[:N//2]))
         self.FA.draw() 
         
         self.Phase = np.zeros(self.data.shape[0])
         
         self.axis5.cla()
         self.axis5.plot((self.Phase))
         self.FP.draw()

        

     def plot_record(self):
         
          N= self.myrecording.shape[0]
          T= 1/ self.samplerate
          xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
         
          self.time = np.arange(len(self.myrecording))/float(self.samplerate)
          self.axis8.cla()
          self.axis8.set_ylim(-0.5,0.5)

          self.axis8.plot(self.time, self.myrecording, color='k') 
          self.FR.draw()   
          
          
          self.axis9.cla()
          self.axis9.set_ylim(0,0.01)
          self.axis9.plot(xf, 2.0/N * np.abs(fft(self.myrecording)[:N//2]))
          self.PR.draw()  
          
    
          
#     def time_domain (self, b):
#         if b.text() == 'Display Record': 
#                       self.axis2.cla()
#                       self.axis2.plot(self.time ,self.myrecording, color='k') 
#                       self.TP.draw()   
#                                
#                       self.axis3.cla()
#                       self.axis3.plot(self.time ,self.filRec )
#                       self.TA.draw()
                       
#         if b.text() == 'Display file': 
#                      self.axis2.cla()
#                      #self.axis2.set_xlim(self.times[0], self.times[-1])
#                      self.axis3.set_ylim(-20000, 20000)
#                      self.axis2.set_xlim(0,300)
#
#                      self.axis2.plot(self.data)
#                      self.TP.draw()
#                      
#                      self.axis3.cla()
#                      self.axis3.plot(self.filData)
#                      self.axis3.set_ylim(-20000, 20000)
#                      self.axis3.set_xlim(0,300)
#                      self.TA.draw()
#                      
                      
             
             
                       
             
         
         

# Phase and Clear fig 

def main():
    App = QtWidgets.QApplication(sys.argv)
    form = Equalizer()
    form.show()
    App.exec_()


if __name__ == '__main__':
    main()

         
         
        
    
        
        
    
