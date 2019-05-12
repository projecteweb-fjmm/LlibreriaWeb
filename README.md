# LlibreriaWeb
Projecte Web 2019

## Authors ##
* [Miquel Oliveros](https://github.com/MiquelOliveros)
* [Marc Visa](https://github.com/mvp17)
* [Francesc Contreras](https://github.com/elskater98)
* [Marc Joan Masip](https://github.com/Drakitus)

## Documentation ##
- [First deliverable](https://github.com/projecteweb-fjmm/LlibreriaWeb/blob/master/deliverable1.md)
- [Second deliverable](https://github.com/projecteweb-fjmm/LlibreriaWeb/blob/master/deliverable2.md)
- [Third deliverable]()

## Installation ##

### Local installation ###
The following commands must be entered in a virtual environment.

    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate

After introducing the commands before, you need to create a super user.

    python3 manage.py createsuperuser
    
Finally, you must run the server.
    
    python3 manage.py runserver
  
### Docker installation ###
  
    docker build .
    docker-compose build    
    docker-compose up
