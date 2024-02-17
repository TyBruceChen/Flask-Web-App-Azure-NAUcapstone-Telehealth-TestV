from flask import Flask,url_for,render_template,request
from PIL import Image
from blob_storage import *
import os
import time
import random


temp_img_path = 'temp_imgs'
app = Flask(__name__)


@app.route('/temp/<var>')
def temp(var):
    return var
#url_for('hello_world',verbose = 1)
@app.route('/',methods = ['GET','POST'])
def file_handle():
    #wait_time = 0  #let the thread to run 10s
    if request.method == 'POST':
        print(request.files)
        if 'pic' in request.files:
            file = request.files['pic']
            try:
                upload_name = file.filename
                print(upload_name) #see the name of uploaded file
                upload_name = upload_name.split('.')[0]

                img_name = str(upload_name) + str(int(random.random()*1000)) + '.png'
                file_name = os.path.join( temp_img_path, img_name)    #temperaryly save the img on local
                file.save(file_name)
                
                with open(file_name,'rb') as bin_file:
                    file_storage_blob(bin_file = bin_file, filename = img_name)
                print('Upload Finish.')
            except:
                pass
                print('Error!')
            #start_time = time.time()
    return render_template('/index.html', name = None)


if __name__ == '__main__':
    if os.path.exists(temp_img_path) != True:
        os.mkdir(temp_img_path)
    app.run()


