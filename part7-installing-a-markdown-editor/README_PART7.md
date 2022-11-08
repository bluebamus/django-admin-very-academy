# part7-installing-a-markdown-editor
part7-installing-a-markdown-editor

# Top Topics:
- package for WYSIWYG Editors : [djangopackages.org](https://djangopackages.org/grids/g/wysiwyg/)
- Install django-summernote
  - github : [django-summernote](https://github.com/summernote/django-summernote)

## Topics:
1. Install summernote

## How to install
```
pip install django-summernote
```

# Topics abstract
1. Add app info to INSTALLED_APPS in settings.py
    - ex) INSTALLED_APPS = [ ..., 'django_summernote', ...]
2. Add URL path to urlpatterns in urls.py
    - ex) urlpatterns = [..., path('summernote/', include('django_summernote.urls'))]
3. static url setting in urls.py
4. set summernote in admin.py
   1. set admin.py
    ```
    from django.contrib import admin
    from . import models
    from django_summernote.admin import SummernoteModelAdmin

    class BlogAdminArea(admin.AdminSite):
        site_header = 'Blog Admin Area'
        login_template = 'blog/admin/login.html'

    blog_site = BlogAdminArea(name='BlogAdmin')

    class SummerAdmin(SummernoteModelAdmin):
        summernote_fields = '__all__'
        #summernote_fields = 'title'

    admin.site.register(model.Post, SummerAdmin)
    blog_site.register(model.Post, SummerAdmin)
    ```