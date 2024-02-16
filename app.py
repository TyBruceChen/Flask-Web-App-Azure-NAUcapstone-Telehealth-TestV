from flask import Flask,url_for,render_template,request
from PIL import Image
import os
import time



app = Flask(__name__)
"""
@app.route('/hello/')    #returns a response once URL/hello is requested
def hello_world():
#    print(verbose)
    return render_template('index.html',name = None)
"""

@app.route('/temp/<var>')
def temp(var):
    return var
#url_for('hello_world',verbose = 1)
@app.route('/',methods = ['GET','POST'])
def file_handle():
    file_name = 'downloads/temp.png'
    #wait_time = 0  #let the thread to run 10s
    if request.method == 'POST':
        print(request.files)
        if 'pic' in request.files:
            f = request.files['pic']
            try:
                f.save(file_name)
                img = Image.open(file_name)
                img.show()
            except:
                pass
            #start_time = time.time()
    return render_template('/index.html', name = None)

'''
with app.test_request_context():
    print(url_for('temp',var='Hello'))
    url_for('static',filename = 'files/Bart-Philip-me.png')
'''
app.run()




"""
def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path,'Flask.sqlite'),
    )

    if test_config is None:
        #load the instance config
        app.config.from_pyfile('config.py',silent = True)
    else:
        #load the test config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')    #handle response to URL/hello
    def hello():
        return 'Hello, World!'
    
    return app
"""
