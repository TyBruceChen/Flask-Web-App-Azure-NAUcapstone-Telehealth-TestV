# Telehealth-NAU
* [Introduction](https://github.com/TyBruceChen/Telehealth-NAU/tree/main#introduction)
* [Implementation](https://github.com/TyBruceChen/Telehealth-NAU/tree/main#implementaion)
  * [Build Server with Flask Python](https://github.com/TyBruceChen/Telehealth-NAU/tree/main#build-server-with-flask-python)
  * [Deployment through Github Actions Workflow](https://github.com/TyBruceChen/Telehealth-NAU/tree/main#deployment-through-github-actions-workflow)
  * [Server Management and Verification](https://github.com/TyBruceChen/Telehealth-NAU/tree/main#server-management-and-verification)
* [Detailed Programming Strategies](https://github.com/TyBruceChen/Telehealth-NAU/tree/main#detailed-programming-strategies)
## Introduction:
This is an **EXPERIMENT** web app project to let user use our COVID-19 detection service remotely. For more information, please visit our capstone page: https://sites.google.com/nau.edu/ai-telehealth/home.

There will be no our classification model to be presented here. And this is a tutorial of holding a web app on Azure Web App service server that can process user's request.


## Implementaion:
#### Build Server with Flask Python
Build the Flask web app object:
```
from flask import Flask,url_for,render_template,request

app = Flask(__name__)
```

Create the function that can be triggered be specific URL request (here is /temp folder under the domain):
```
@app.route('/temp')
def your_triggered function:
    actions
```
For more information of Flask functions that handle different request, please vistit: [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application).

Run the Flask App:
```
if __name__ == '__main__':    #when this file is run as main file
    app.run()
```
To test the function of your Flask web app, you can access 127.0.0.1:5000/specific_directory and use the command: `Flask -app your_file_name.py run --debug` (I tested on VS Studio Code terminal).

Link the webstorage to store user's uploaded file (information):
```
from azure.storage.blob import BlobServiceClient, BlobClient
```
Here I use Azure storage service (Blob). The storage file system structures like this: Source Group -> (storage service) -> containers -> blobs. Blobs are the stored files under the container. For more information, please vistit [Quickstart: Azure Blob Storage client library for Python](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=connection-string%2Croles-azure-portal%2Csign-in-azure-cli#authenticate-to-azure-and-authorize-access-to-blob-data).
```
Azure_Storage_Blob_Connection_String = 'the connection authority key, can be found at access key -> connection string'
Container_Name = 'the container you want to store (need to be created first)'
Blob_Name = 'where the file will be stored in the container (path + file name)'
```
To upload the users' file, you need to specify three things: Connection String, Container Name and Blob Name.
<br>The Azure Web App service and Storage service can be found here: <br>
![explanation/Azure Services.png](https://github.com/TyBruceChen/Telehealth-NAU/blob/main/explanation/Azure%20Services.png)
<br>To create a Web App instance which is hold by Python: <br>
![explanation/Azure Web App.png](https://github.com/TyBruceChen/Telehealth-NAU/blob/main/explanation/Azure%20Web%20App.png)
<br>The Connection String can be found at the *Resource Group*: <br>
![explanation/Azure-Storage.png](https://github.com/TyBruceChen/Telehealth-NAU/blob/main/explanation/Azure%20Storage.png)
```
blob_server_client = BlobServiceClient.from_connection_string(Azure_Storage_Blob_Connection_String) #connect to your Azure storage resource
blob_client = blob_server_client.get_blob_client(container = Container_Name, blob = blob_name)  #connect to the container and the underlying blob
```
Build connection to Azure Storage service and then a specific container
```
blob_client.upload_blob(bin_file,blob_type='BlockBlob',overwrite = True)
# Uploaded file should be read as the binary form (with open(file_name,'rb') as file #here rb is read and binary) 
```
Upload a file as blob: path+name to the container.

#### Deployment through Github Actions Workflow
When you sucessfully test all the functions in local, it's time to upload your web app and deploy it on Azure. The method I use is through Github actions workflow, you can find other methods here:  [Quickstart: Deploy a Python (Django or Flask) web app to Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Czip-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli).
First make sure your main file contains `if __name__=='__main__'` for identification. Then go into your Azure Web App instance: Deployment Center -> Settings, link your Github repository to it: <br>
![Azure Deployment](https://github.com/TyBruceChen/Telehealth-NAU/blob/main/explanation/Azure%20Web%20App%20Deployment.png)
After that, click the save buttom and wait for few minutes, you can view your deployment status in Github Actions column with creating a yaml file (under .github/worflows) generated by Azure: <br>
![Github Actions](https://github.com/TyBruceChen/Telehealth-NAU/blob/main/explanation/Github%20Actions.png)

#### Server Management and Verification
**Attention!** If you are using the free Azure Web service like me, the CPU hour per day is 60 minutes, which means that your web app can not work (no response) when it uses up of work time. You can create a new instance to solve this (Not sure). So stop your server when it's not tested. 
To see how your server manages files, find the Development Tools -> Advanced Tools -> Go -> Bash (hold by [Kudu](https://github.com/projectkudu/kudu/wiki)): <br>
![Azure Console](https://github.com/TyBruceChen/Telehealth-NAU/blob/main/explanation/Azure%20Web%20Server%20Console.png) <br>
The deployed files are under ```/home/site/```. To *temporarily* store at the server (free plan only has 1GB space!), my suggection is to specify the absolute path, like this: ```/home/site/wwwroot/temp_fold```.

## Detailed Programming strategies
Programming on VS Code (mac OS):
Create the virtual environment (venv) in terminal: ```python3 -m env venv_path```. <br>
Activate the virtual environment in terminal: ```source venv_path/bin/activate```. <br>
Set your interpreter: ```cmd+shift+P``` -> ```python interpreter```. <br>

Guide to new page and Handle <form> uploaded files:
```
from flask import Flask,url_for,render_template,request
@app.route('/directory',methods = ['POST','GET'])
def func():
    if request.method == 'POST' and 'upload_element_id' in request.files:
        file = request.files[uploaded_element_id]
        actions ....
    return render_template('/the page you want jump', name= None)
```
For the corresponding form element in html page:
```
<form action="/" method="post" enctype="multipart/form-data">
    <label for="upload_element_id">Text Explanation</label>
    <br>    
    <input type="file" name="name of this input element" id="upload_element_id">
    <br>
    <input type="submit" value="Upload">
</form> 
```
The post method method should be POST, the encryption method should be multipart/form-data and the input element id should corresponds to request.file[] in python file so that it can be detected.
The page that is loaded (here is once '/directory' accessed by user), should be store at the specific folder: ```/templates```. The static local files (like css, images, etc) that is linked by html page should be stored under ```static```.
