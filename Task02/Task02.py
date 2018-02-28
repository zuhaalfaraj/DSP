from flask import Flask, render_template ,make_response, request, send_file, url_for, redirect, flash
import pygal 
from numpy import genfromtxt
import numpy as np
from werkzeug import secure_filename
import os
from scipy import signal

data=  genfromtxt(r'D:\My stuff\Datasets\ECG.csv', delimiter=',')
app = Flask(__name__)

## Generate general functions 
def impulse(x):
    return 1 * (x == 0)

def periodic_signal( freq , amp , func ):
    ts = np.arange( 0 , 0.3 , 1 / (50 * freq) )
    phases = 2 * np.pi * freq * ts 
    ys = amp * func( phases )
    return ts , ys

def Sin( freq , amp ):
    return periodic_signal( freq, amp, np.sin )

def Cos( freq , amp ):
    return periodic_signal( freq, amp, np.cos )

def Sampling(t, func):
    T = t[1]-t[0]
    ts= np.arange(t[0], t[-1], T)
    sample= np.zeros(t.shape[0])
    for nT in ts :
        sample+= impulse(t-nT)*func(t)
    return t,sample

def Exp( freq , amp ):
    return periodic_signal( freq, amp, np.exp )

##End
    
## Start of the Web Page
    
@app.route('/')
def home():
    return render_template("view1.html")

@app.route('/signals')
def Signals():
      t1 , sin = Sin(20,1)
      t2 , cos = Cos(20,1)
      t3 , exp = Exp(2,1)

      graph = pygal.Line()
      graph.add('Sin', sin)
      graph.add('Cos', cos)
      graph.add('Exp', exp)
      graph_data = graph.render_data_uri()
      return render_template("SampCos.html", graph_data = graph_data)

@app.route('/sampling1')  
def Sampling1():
      t1 , sin = Sin(20,1)
      t , p_t = Sampling( np.arange( -10, 10 , 1 ), np.sin)
      graph = pygal.Line()
      graph.add('Sin', p_t)
      graph_data = graph.render_data_uri()
      return render_template("SamplingSin.html", graph_data = graph_data)
  
@app.route('/exp')   
def Sampling2():
      t1 , sin = Sin(20,1)
      t , p_t = Sampling( np.arange( -10, 10 , 1 ), np.exp)
      graph = pygal.Line()
      graph.add('Sin', p_t)
      graph_data = graph.render_data_uri()
      return render_template("exp.html", graph_data = graph_data)
  
@app.route('/graph', methods=["GET","POST"])
def graphing ():    
        graph = pygal.Line()
        graph.add('original', data[1,:])
        graph_data = graph.render_data_uri()
        return render_template("upload.html", graph_data = graph_data)
    
@app.route('/filter', methods = ['GET', 'POST'])   
def Filter():
   if request.method == 'POST':
        c1 =eval( request.form['c1'])
        c2 =eval( request.form['c2'])
        c3 =eval( request.form['c3'])
        x= np.array([c1,c2,c3])
        ploty= signal.convolve(x,data[1,:])
        graph = pygal.Line()
        graph.add('Filtered', ploty)
        graph_data = graph.render_data_uri()
        return render_template('filter.html', graph_data1=graph_data )
   else:
        return render_template('filter.html')
    
	
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
     # mypath=os.path.abspath(f.filename)
      data= genfromtxt(os.path.abspath(f.filename) , delimiter=',')
      graph = pygal.Line()
      graph.add('Original', data)
      graph_data = graph.render_data_uri()
      return render_template('upload.html', graph_data=graph_data)
   else:
        return render_template('upload.html')
    
    
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)