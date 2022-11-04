# django-admin-multiple-sites-ex
django-admin-multiple-sites-ex

# Test abstract
1. Multi admin site test
   1. Each apps has blog_site in admin.py
   2. config/settings.py allows users to access a standalone admin site
2. Default admin change test
   1. One of the app admins can be the default admin site instead of the default admin site
   2. Important!!! The current django version produces an error in the following video class:
      1. [Setup Custom/Multiple Django Admin Sites - Django Admin Series - Part 3](https://www.youtube.com/watch?v=QCnefsgalF8&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=3)
   3. To change the default admin site, you need to create a new 'apps-admin.py' file. This is to set the default admin site using AdminConfig.
   4. Remove basic admin app in settings.py
   5. Add new admin app in settings.py as "blog.apps-admin.BlogAdminConfig"
3. Default admin setting error case test
   1. Duplicate admin error when user add new admin app in to settings.py or add default admin app with custom admin app.

# How to test
## Make default environment
1. make database
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
## Multi admin site test
1. set admin.py in blog and bookstore apps
2. add new url path in config/urls.py
## Default admin change test
1. 

## Default admin setting error case test