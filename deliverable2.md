# Deliverable 2

## Changes in the model of data base

It has been incorporated that the user can upload an image in the model of the book, have also rectified models of which were not 
very accurate and caused inconsistencies.

## How need to create the CreateView, UpdateView and DeleteView

First of all we had to create a new view of the type _DetailsView_, in order to be able to access the attributes of each model 
individually. A user cannot update nor delete a created object of another user. A user needs to be logged to create an object. It is important to take account of the primary key to be able to carry out the access through the object url and be able to update it or delete it.

## Test
It has been done scenarios for the creation, update and delete features. Unfortunately, it has been developed satisfactorily only the creation features scenarios. In the others, there had been some code errors which it has not been able to solve. It has been used a Windows OS, therefore, it has been needed to include in the virtual environment the [ChromeDriver](http://chromedriver.chromium.org/)

## Security
Speaking of web security level, the user has to be authenticated to create, update or delete objects;  if the user is not authenticated, the web redirects them to the log in page, so that they do not make a fraudulent use of the application.

## HTML Improvements
It has been used the bootstrap 3 to ease the web interface development and it has been reestructurated the html code. Besides it has been included some icons to improve the web usability.


## API - Google OAuth


The use of the Google OAuth API allows us to use our Google account to register directly to our website.

To make use of it, several considerations must be taken into account.

1. Install social-auth

              pip install social-auth-app-django
    
2. Migrate the data base

              python manage.py makemigrations
              python manage.py migrate
              
3. Configurations

  Go to the Google [Google Developers Console](https://console.developers.google.com/projectselector2/apis/library?supportedpurview=project) and then click on create button.

  Enter project name e.g 'Django App'. Wait for a few seconds your project should be created

  On the right side there is credentials tab, select it.

  Click on Create Credentials then OAuth Client ID. Select the application type Web app, Give any name of your choice and Enter any name in 'Product name shown to users' under OAuth Consent Screen tab.

  Enter the following URI's in Authorized redirect URIs

                http://localhost:8000/auth/complete/google-oauth2/
                http://127.0.0.1:8000/auth/complete/google-oauth2/
                
Now, Copy the Client ID and Client Secret Under settings.py

- SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =''  #Paste CLient Key
- SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' #Paste Secret Key

## Users

| User  |     Password     | 
|----------|:-------------:|
| admin |  admin | 
| username |    password   |
