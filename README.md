# 2022-django-blog-flattern
This is my exercise based on the template I downloaded from https://www.free-css.com/


#### 1. Create django project, blog app and portfolio app

        STEPS:

        1. Install and check python
        2. Install pip and check pip
        3. Create virtual env
        4. Activate env
        	λ venv39303\scripts\activate
        5. Install django
        	(portfolio) λ pip install django==3.0.3
        6. Create project
        	(portfolio) λ django-admin startproject config . 
        7. Create appsand apps
         	(portfolio) λ mkdir apps
         	(portfolio) λ mkdir apps\portfolio
         	(portfolio) λ mkdir apps\blog
         	(portfolio) λ django-admin startapp blog apps\blog
         	(portfolio) λ django-admin startapp portfolio apps\portfolio
        7. Modify apps.py files 
        8. Register apps to settings.py
        9. Run the server to test it out:
        10. File structures
        
        E:.
        │   .gitignore
        │   LICENSE
        │   manage.py
        │   README.md
        │
        ├───apps
        │   ├───blog
        │   │   │   admin.py
        │   │   │   apps.py
        │   │   │   models.py
        │   │   │   tests.py
        │   │   │   views.py
        │   │   │   __init__.py
        │   │   │
        │   │   └───migrations
        │   │           __init__.py
        │   │
        │   └───portfolio
        │       │   admin.py
        │       │   apps.py
        │       │   models.py
        │       │   tests.py
        │       │   views.py
        │       │   __init__.py
        │       │
        │       └───migrations
        │               __init__.py
        │
        └───config
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py