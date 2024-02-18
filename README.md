# Telehealth-NAU
* [Introduction]()
* [Implementation]()
  * [Build Server with Flask Python]()
  * [Deployment through Github Actions Workflow]()
  * [Server Management and Verification]()
## Introduction:
This is an **EXPERIMENT** web app project to let user use our COVID-19 detection service remotely. For more information, please visit our capstone page: https://sites.google.com/nau.edu/ai-telehealth/home.

There will be no our classification model to be presented here.


## Implementaion:
#### Build Server with Flask Python
Build the Flask web app object:
```
app = Flask(__name__)
```

Create the function that can be triggered be specific URL request (here is /temp folder under the domain):
```
@app.route('/temp')
def your_triggered function:
    actions
```

Run the Flask App:
```
if __name__ == '__main__':    #when this file is run as main file
    app.run()
```
To test the function of your Flask web app, you can access 127.0.0.1:5000/specific directory and use the command: Flask -app your_file_name.py run --debug (I tested on VS Studio Code terminal)

#### Deployment through Github Actions Workflow

#### Server Management and Verification
