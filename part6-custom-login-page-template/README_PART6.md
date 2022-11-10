# part6-custom-login-page-template
part6-custom-login-page-template
link : [Custom Login Page Template - Django Admin Series - Part 6
](https://www.youtube.com/watch?v=fNMTKxO8HsI&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=6)

# Top Topics:
- Using custom template html file, update admin page template

## Django Admin Series

## Topics:

# Topics abstract
1. Update TEMPLATES Option in settings.py 
   ```
   # config/settings.py

    ...
   TEMPLATE = [
        'BACKEND' : ...,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        ...
   ]
   ...
   ```
2. Create html file at template\blog\admin
   - ex) login.html
3. Set static url, root in settings.py and Set static path in urls.py
   - STATIC_URL
   - STATICFILES_DIRS *
   - Run collectstatic command
     - ex) python manage.py collectstatic
4. Copy original admin's login.html code to custom login.html file
- file path: env/Lib/django/contrib/admin/template/admin/login.html
5. Copy original admin's login.css code to custom login.css file
- original file path: static/admin/css/login.css
- target file path: static/blog/admin
- must change css including code
  - ex) <link rel="stylesheet" type="text/css" href="{% static "blog/admin/login.css" %}">
6. Modify admin.py
    ```
    # admin.py
    from django.contrib import admin
    from . import models

    class BlogAdmin(admin.AdminSite):
        site_header = 'Blog Admin Area'
        login_template = 'blog/admin/login.html'

    blog_site = BlogAdminArea(name='BlogAdmin') # 'name' parameter will be site name like apps_name
    blog_site.register(models.Post)
    ```

*** How to do debug for css
    ```
    python manage.py findstatic --verbosity 2 login.css
    ```