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



<br>
<br>

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

Please go to [admin page]("http://localhost/admin/") for login

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

## 4) Many-to-one relationship. Tile item contains related tasks 


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

