# Django_Rest_Api
A Simple Rest API using Django Rest Framework.\
This retuns a nested list of all members along with their every detail.

## Dependencies
 - Python
 - Django
 - Django Rest Framework
 - Django Seed
 
## Installation Details 
#### Clone this repository:
```
git clone https://github.com/bitu10/Django_Rest_Api.git
```
#### Create virtualenv and install all requirements in full_throtle_labs directory:
```
cd full_throtle_labs/
python3 -m venv venv_name
source venv_name/bin/activate
pip install -r requirements.txt
```
#### Fire up the Django Server
```
cd full_throtle_labs/
python3 manage.py migrate
python3 manage.py runserver
```
#### For populating with DB with Dummy Data
```
cd full_throtle_labs/
python manage.py seed api_basic --number=1

where 1 is the no of records of dummy data to be inserted into each table in the DB
```
## API Details
Live Deployed Project on Heroku-\
URL Definition - https://b210-first-django-app.herokuapp.com/basic/ \
HTTP-Method = GET
#### Sample Response Body-
![Screenshot from 2020-07-07 16-32-28](https://user-images.githubusercontent.com/56647211/86771350-b0e63080-c06f-11ea-8fbc-2b3c44a38cb1.png)


## Built With
[Django](https://www.djangoproject.com/) - A Python-based free and open-source web framework \
[Django REST framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs \
[Django Seed](https://github.com/Brobin/django-seed#usage) - A library to populate DB with Dummy Data
