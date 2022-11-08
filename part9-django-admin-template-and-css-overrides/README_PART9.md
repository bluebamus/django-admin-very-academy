# part9-django-admin-template-and-css-overrides
part9-django-admin-template-and-css-overrides
youtube link :[Django Admin Template and CSS Overrides](https://www.youtube.com/watch?v=eosXCVcgtPw&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=9)

# Top Topics:

## Django Admin Series
- How do you edit the admin template?

## Topics:
- Admin templating
- Admin template styling

# Topics abstract
1. Django html location
   - venv/Lib/site-pakages/django/contrib/admin
   - copy to templates/admin/base.html
2. Django css location
   - venv/Lib/site-pakages/django/contrib/admin/static/admin
   - copy to static/admin/css/base.css
3. Must modify settings.py
   - STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

* For static setting
- [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/4.1/howto/static-files/)
- [Settings](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-STATICFILES_DIRS)
- [How to deploy static files](https://docs.djangoproject.com/en/4.1/howto/static-files/deployment/)
- [The staticfiles app](https://docs.djangoproject.com/en/4.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles)
- [The Django admin site](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.AdminSite)
- [Admin actions](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/actions/)