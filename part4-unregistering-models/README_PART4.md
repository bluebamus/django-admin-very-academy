# part4-unregistering-models
part4-unregistering-models
link : [Registering/Unregistering Models from the Django Django Site - Django Admin Series - Part 4](https://www.youtube.com/watch?v=QP4qRNl_5kA&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=5)

# Top Topics:
- Setup a suctom admin area
- Overriding the default admin site
- Setup multiple admin areas

## Django Admin Series
- registering models to the admin site

## Topics:
- Registering a model
- Registering a model - Object -> Customisation
- Registering All Models
  - unregister

# Topics abstract
1. Registering a model
    ```
    # admin.py
    from django.contrib import admin
    from .models import Post, Cetegory

    admin.site.register(Post)
    admin.site.register(Cetegory)
    ```

2. Registering a model - Object -> Customisation
   - Build class 
   - Register
    ```
        # admin.py
        from django.contrib import admin
        from .models import Post, Cetegory

        class PostAdmin(admin.ModelAdmin):
            fields = ['title', 'author']

        # use decorator
        @admin.register(Post)
        class CetegoryAdmin(admin.ModelAdmin):
            fields = ['title', 'author']

        admin.site.register(Post,PostAdmin)
    ```


3. Registering All Models
   - Collect model data 
   - Loop through models
    ```
    from django.contrib import admin
    import django.apps

    # get all models information
    models = django.apps.apps.get_models()

    for model in models :
        try :
            admin.site.register(model)
        except admin.sites.AlreadyRegistered :
            pass

    admin.site.unregister(django.contrib.sessions.models.Session)
    ```