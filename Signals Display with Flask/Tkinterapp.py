
# coding: utf-8

# In[ ]:


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog 
from tkinter import ttk

from scipy import signal

import scipy


root=Tk()


entry1=ttk.Entry(root,width=20)
entry1.pack()

entry2=ttk.Entry(root,width=20)
entry2.pack()

entry3=ttk.Entry(root,width=20)
entry3.pack()

b1=ttk.Button(root,text='browse')
b1.pack()

b2=ttk.Button(root,text='filter now')
b2.pack()


def buclick():
    global fileName        
    global sig1
    global sig
    root.fileName=filedialog.askopenfilename(filetypes=(( "comma separated value","*.CSV"),("All files ","*.*")))
    sig1=np.loadtxt(root.fileName, dtype=float,delimiter=',')
    sig=np.asarray(sig1)
   
    #print (sig1)
    #np.reshape(sig,(1,3000))
    #if entry1.get()=="" :
    f=Figure(figsize=(5,5),dpi=75)
    a1=f.add_subplot(212)
    #a1=f.plt.subplot2grid((2,1),(0,0),rowspan=2)
    a1.plot(sig)
    canvas=FigureCanvasTkAgg(f,root)
    canvas.show()
    canvas.get_tk_widget().pack()
    toolbar=NavigationToolbar2TkAgg(canvas,root)
    toolbar.update()
    #canvas._tkcanvas.pack()

    
b1.config(command=buclick)
   
def buclick2():
    global fileName        
    global sig1
    global sig
   
    sig1=np.loadtxt(root.fileName, dtype=float,delimiter=',')
    sig=np.asarray(sig1)    
    #else:
        
    x=eval(entry1.get())
    y=eval(entry2.get())
    z=eval(entry3.get())
    
    highpass=np.array([x,y,z])
    
    filtered=scipy.signal.convolve(sig,highpass,mode='same')
    f=Figure(figsize=(5,5),dpi=75)
    a2=f.add_subplot(211)
    #a2=f.plt.subplot2grid((2,1),(2,0),rowspan=2)
    a2.plot(filtered)
     
    canvas=FigureCanvasTkAgg(f,root)
    canvas.show()
    canvas.get_tk_widget().pack()
    toolbar=NavigationToolbar2TkAgg(canvas,root)
    toolbar.update()
    #canvas._tkcanvas.pack()

    
b2.config(command=buclick2)

#plt.show()



root.mainloop()

