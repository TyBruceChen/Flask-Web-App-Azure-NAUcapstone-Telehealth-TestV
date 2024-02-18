from flask import Flask,url_for,render_template,request
#from PIL import Image
from blob_storage import *
import os
import time
import random


#temp_img_path = 'temp_imgs'
temp_img_path = 'home/site/temp_imgs'   #when it's uploaded to Azure server.
app = Flask(__name__)
if os.path.exists(temp_img_path) != True:
        os.mkdir(temp_img_path)


@app.route('/temp/<var>')
def temp(var):
    return var

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
                file_name = os.path.join( temp_img_path,img_name)    #temperaryly save the img on local
                file.save(file_name)
                # the initial idea is to save the file then read as binary type
                with open(file_name,'rb') as bin_file:
                    file_storage_blob(bin_file = bin_file, filename = img_name)
                print('Upload Finish.')
                try:
                    os.remove(file_name)
                    print('Server File deleted.')
                except:
                    print('Fail to delete server file!')
            except:
                pass
                print('Error!')           
    return render_template('/index.html', name = None)


if __name__ == '__main__':
    app.run()


