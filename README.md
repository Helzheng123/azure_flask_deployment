# azure_flask_deployment
This is an introduction to Azure and Flask deployment.

Deployed URL for my application: https://helen-504-flask.azurewebsites.net/

## Guide on how to set up and deploy the application:
### Set up:
1. Create a new repository with the name called ```azure_flask_deployment``` on Github (check off "**Add a READme.md file**"). Once the repository has been created, go to ```<> Code``` and copy the link. Open your Google Shell and in the terminal, use the command ```git clone <URL>``` (replace **URL** with the link you copied from your repository). Go to **File**-->**Open** and find your cloned repository.
2. Create a new ```app.py``` file. For this application, you will need to have the following in your file:
```
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

df = pd.read_csv('data/healthy_lifestyle_city_2021.csv')
@app.route('/data')
def data(data=df):
    data = data.head(15)
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
```
If needed, you can change the ```df = pd.read_csv('data/healthy_lifestyle_city_2021.csv')``` line with your own dataset name.
3. Since we are dealing with HTML, we will need a ```templates``` folder. In this folder, we will need to make a```about.html```, ```base.html```, and ```data.html```files. In each of these files, the templates were taken from [here](https://github.com/hantswilliams/HHA_504_2023/blob/main/WK2). You can customize it to tailor your application.
4. Create a ```requirements.txt``` file. Type in ```faker```,```pandas```, and ```flask``` in separate lines.
5. In the Google Shell terminal, type in: ```git add .```. Afterward, type in ```git commit -m '<add a message>'```and replace the **add a message** portion with your comment. Then type in ```git push``` to send the repo to Github.

### Deploy Application via Azure:
1. In the Google Shell terminal, you will need to install [AZURE CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) with this: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```. Copy and paste the line in and enter.
2. Then type in ```az```. Type in ```az login --use-device-code``` and wait for a link and a code to appear in the terminal. Copy the code and press the link to log in to your Azure account. This will help connect your Google Shell with Azure.
3. Login to your [Azure account](https://azure.microsoft.com/en-us/). Navigate to **Resource Group** and create a new Resource Group with a unique name. Press **Review and Create***. 
4. Head back to Google Shell and in the terminal, type in ```az account list --output table``` to make sure you have the correct subscription for your Azure account. Make sure your subscription is correct. In my case, the subscription is **Azure for Students**. If the subscription has not defaulted to the desired one, type in ```az account set --subscription <paste the desired SubscriptionId here>```.
5. Now type in ```az group list```.
6. Type in ```az webapp up --name <replace with what you would like to name the webapp> --runtime PYTHON:3.9 --sku B1```. Once entered, the Azure app service will create the web app for you. This step may take a while to load.
7. Once the service completes the deployment, you can go to App Service in the Azure site to deploy the web app. Choose the appropriate web app. Then you will be redirected to the overview of the web app. The link for your application will be found at the **Default domain**. Click on the link and you will now be redirected to your web application.
8. Congrats! You have deployed your web application!

If you do make any changes, make sure to do the three git commands shown in step 5 of **Setup:** in the Google Shell terminal. 
