# Django Rest Framework Task

<br>


## Package Used
- django 3.2 <br>
- djangorestframework 3.10<br>
- requests 2.28.2<br>
- django-cors-headers 3.14.0<br>
- python-decouple 3.8<br>

<br>
<br>

# Installation

## Step 1 - Clone the Project
```
 $ git clone git@github.com:wilws/django_rest_framework.git
```
<br>
<br>


## Step 2 - Create Virtual Environment
```
 $ cd django_rest_framework
 $ python3 -m venv venv
```

a "venv" folder will be created
<br>
<br>
<br>


## Step 3 - Activate Virtual Environment
```
 $ source venv/bin/activate
```
<br>
<br>



## Step 4 - Install Package
```
 $ pip install -r requirements.txt
```
<br>
<br>

## Step 5 - Run Server
```
 $ python manage.py runserver

 or 

 $ python3 manage.py runserver
```
<br>
<br>

## Step 6 - Conflict Handling

It may have error shown like :
```
<you-current-folder> /venv/lib/python3.10/site-packages/rest_framework/serializers.py", line 24, in <module>
    from django.db.models.fields import FieldDoesNotExist
ImportError: cannot import name 'FieldDoesNotExist' from 'django.db.models.fields'

```
"venv" is the folder created in step 2.

Just open "/venv/lib/python3.10/site-packages/rest_framework/serializers.py" and amend like below:


```diff
#line 24 of serializers.py

-from django.db.models.fields import FieldDoesNotExist
+from django.core.exceptions import FieldDoesNotExist

```

It should work fine as follows :
```
$ python3 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 19, 2023 - 23:38:58
Django version 3.2, using settings 'home.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```


<br>
<br>
<br>

# App Introduction

## API Routes
task : "http://localhost/api/task/" <br>
tile : "http://localhost/api/tile/" <br>
admin : "http://localhost/admin/"
<br>
<br>
<br>

## Login
Log in is required to View / Create / Edit items. There are 2 accounts created: <br>

Account 1
- username : **staff_view** <br> 
- password : **123qwe!@#** <br> 
- Feature : Can only view  “Task” and “Tile” items <br>

Account 2
- username : **staff_edit** <br> 
- password : **123qwe!@#** <br> 
- Feature : Can Edit all “Task” and “Tile” items

If login dialog doest not pop-up, please go to [admin page]("http://127.0.0.1:8000/admin/") for login

<br>
<br>

# Some Features

<br>

## 1) Permission is required for Get Request   
- To prevent unpermitted view, customised permission is configured to restrict the use of GET request

```diff
# home/permission.py

    perms_map = {
+       'GET': ['%(app_label)s.view_%(model_name)s'],   
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

```

<br>
<br>

## 2) Single task’s URL is also returned  


```diff
#task/serializers.py

def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('task-detail',kwargs={"pk": obj.pk}, request=request)


-----------------------------------------
Output :

 {
     "title": "Task_1",
        "order": 1,
        "description": "This is Task 1",
        "type": "discussion",
        "tile": 1,
        "tile_data": {
            "tile_name": "tile_1",
            "launch_date": "2023-03-06",
            "status": "pending"
        },
+        "url": "http://127.0.0.1:8000/api/task/1/“       
    },


```


<br>
<br>

## 3) Many-to-one relationship. Tile item contains related tasks 


```diff

{
        "tile_name": "tile_1",
        "launch_date": "2023-03-06",
        "status": "pending",
+       "tasks": [
+          "http://127.0.0.1:8000/api/task/1/",
+          "http://127.0.0.1:8000/api/task/2/"
+        ]
    },


```

