# Steps
## Tutorial 1
- create virtual environment using pip
- install django using pip
- create django project `django-admin startproject projectname`
- move to the project
- `manage.py` is used to interact with django app.
- `init.py` is used to read the project folder structure.
- `asgi.py` is asynchronous gateway interface
- `wsgi.py` is web server gateway interface
- `urls.py` contains all the url mapping.
- `settings.py` contains all the settings for django app
- `asgi.py` is not necessary for now

## Tutorial 2
- we can create an app in django using `python3 manage.py startapp appname`
- This creates a django app folder with boilerplate scripts inside.
- `admin.py` is to reach the admin panel to register some changes in it or register some model in it.
- `apps.py` tells django that this directory is named core.
- `models.py` deals with all the database related work.
- `tests.py` deals with testing of functionality in app.
- `views.py` deals with logic in app
- we need app created using `startapp` to hold set of functionalities in a module.
- This helps to segregate different set of functionalities in modules which are resuable too.
- `python3 manage.py runserver` is used to run server and assign a port 8000 by default to the server and create a link to visit the django app. This can be done with custom port also as `python3 manage.py runserver 0.0.0.0:3000`.
- Django needs to know all the apps in django app, thus we need to add the appname in the `INSTALLED_APP` list of `settings.py` of core django app
- we can create a separate list `EXTERNAL_APPS` list for all created apps and append it to `INSTALLED_APPS`, this will help keep created apps in separate list.

## Tutorial 3
- For now we will deal with function based view
- here we have to add a function `home` and add make it return `HttpResponse('testing httpresponse')` with it.
- In `urls.py` of `core` folder we have to add the home method on default endpoint like `path('', home, name="home")`

## Tutorial 4
- To make django give html response we need to add a template folder where we will put html files.
- we need to replace the `HttpResponse` in the `home` function with `render` function, it will help put html page as response.
- If we want to put html files in a folder inside the template folder we need to update the file path in render method as `foldername/htmlfile.html`

## Tutorial 5
- We can send data from server to the client through template also using template engine of django.
- We can create a dictionary and iterate over it in template using context in Django.
- for example,
    ```python
    def home(request):
        people = [
            {...},
            {...},
            ...
        ]
        return render(requestm "home/index.html", content = {'people': people})
    ```
- now to render this context data in template html we can
    ```
        {% for person in people %}
        {{forloop.counter}},
        {{person.name}},
        {{person.age}}
        {% endfor %}
    ```
- [Django template tags](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/) are available to provide various tags like truncatechars
- we can use `text|truncatechars:numchars` to truncate text such that UI doesnot get ruined with too much text.
- all the python keywords can be used in template using Django template tags
- Here we can follow DRY (donot repeat) principle in template html files as they have common html boilerplate code which can be substituted with a base.html containing that boiler plate code.

## Tutorial 6
- database schema is shown in models script
- model structure is created using class extending `models.Model` and it consists of various fields like `CharField, IntegerField, EmailField, TextField, ImageField, FileField` etc.
```Python
class Student(models.Model):
    name = model.CharField(max_length=50)
    ...
```
- here we can use sqlite3 viewer as a local webapp to view tables created from django models.
- `python manage.py makemigrations` will create migration script for the database with tables
- the migration file contains two fields `dependencies` and `operations`.
- `dependencies` consists of tuples that shows what previous migration files are needed for current migration script.
- `operations` consists of all the modifications applied on the database
- `python3 manage.py makemigrations` will create a migration script `home/migrations/0001_initial.py` with the dependencies and operations on the DB till that time.
- these migration script are very important as if any of this migration file is deleted then any other dependent migration file are there, then DB will collapse.
- `python3 manage.py migrate` will create tables in DB which can be viewed in SQLite viewer web app.

## Tutorial 7
- Django shell can be used to fetch, insert data to tables in the database.
- Django shell can be invoked by command `python3 manage.py shell`.
- we can instantiate a student class object in models as `student = Student(name="Harsh", age=26, email="harsh@gmail.com", address="Lucknow",)`
- we can insert this student model instance by command `student.save()`.
- `Student.object.create()` here `Student` is model manager.
`Student.objects.all()[0]` will give a row of student table, thus we can access `Student.objects.all()[0].name` to print its name column.

## Tutorial 8
- CREATE models with Django
```python
Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from home.models import *
>>> car = Car()
>>> car.save()
>>> car
<Car: Car object (1)>
>>> car.save()
>>> car
<Car: Car object (1)>
>>> clear
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'clear' is not defined
>>> car = Car(name="Honda jazz", speed = 60)
>>> car.save()
>>> car = Car(name="Alto", speed = 40)
>>> car.save()
>>> Car.objects.create(name="Mercedes AMG", speed=150)
<Car: Car object (4)>
>>> car_dict = {"name" : "BMW M3 GTR", "speed" : 190}
>>> Car.objects.create(**car_dict)
<Car: Car object (5)>
```

- Read operations
```python
class Car(models.Model):
    name = models.CharField(max_length=20)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return f"Car name: {self.name}, Car speed: {self.speed}\n"

Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from home.models import *
>>> cars = Car.objects.all()
>>> cars
<QuerySet [<Car: Car name: , Car speed: 50
>, <Car: Car name: Honda jazz, Car speed: 60
>, <Car: Car name: Alto, Car speed: 40
>, <Car: Car name: Mercedes AMG, Car speed: 150
>, <Car: Car name: BMW M3 GTR, Car speed: 190
>]>
>>> car = Car.objects.get(id = 1)
>>> car
<Car: Car name: , Car speed: 50
>
>>> car = Car.objects.filter(id = 2)
>>> car
<QuerySet [<Car: Car name: Honda jazz, Car speed: 60
>]>
>>> car = Car.objects.filter(id = 10)
>>> car
<QuerySet []>
```
- Update operations
```python
>>> car = Car.objects.get(id=1)
>>> car
<Car: Car name: , Car speed: 50
>
>>> Car.objects.filter(id=1).update(name="Gallardo", speed=170)
1
>>> Car.objects.all()
<QuerySet [<Car: Car name: Gallardo, Car speed: 170
>, <Car: Car name: Honda jazz, Car speed: 60
>, <Car: Car name: Alto, Car speed: 40
>, <Car: Car name: Mercedes AMG, Car speed: 150
>, <Car: Car name: BMW M3 GTR, Car speed: 190
>]>
```

- delete operation
```python
>>> Car.objects.filter(id=3).delete()
(1, {'home.Car': 1})
>>> Car.objects.all()
<QuerySet [<Car: Car name: Gallardo, Car speed: 180
>, <Car: Car name: Honda jazz, Car speed: 60
>, <Car: Car name: Mercedes AMG, Car speed: 150
>, <Car: Car name: BMW M3 GTR, Car speed: 190
>]>
```

- donot use command `Car.objects.all().delete()` as it will delete all the entries in the `Car` table

## Tutorial 9
