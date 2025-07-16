1. create a project
    ```
    django-admin startproject <project_name>
    ```

2. create app
    ```
    python manage.py startapp <app_name>
    ```
    Then go to project main folder -> setting.py -> INSTALLED_APPS: add a string eg "myapp"

3. urls display
   For each url, write the content in templates, register the url in urls.py, create a view handle in views.py
   2. urls.py in main folder: the whole handler, can pass specific urls to urls.py in each app folder

   3. view.py can render the html


4. run: ```python manage.py runserver```

5. models.py: deal with database
   1. after changing the database, run `python manage.py makemigrations; python manage.py migrate`. Then in sqlite everything will be done
   
    ```

    ```

6. Access as admin and add things into databases:
   ```
   python manage.py createsuperuser
   ```
   In the website, type `.../admin` to access