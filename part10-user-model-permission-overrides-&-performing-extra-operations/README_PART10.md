# part10-user-model-permission-overrides-&-performing-extra-operations
part10-user-model-permission-overrides-&-performing-extra-operations
youtube link : [Django Admin User Model Permission Overrides & Performing Extra Operations](https://www.youtube.com/watch?v=WVSEcfAvlfc&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=11)

# Top Topics:

## Django Admin Series
- First look at model permissions via ModelAdmin methods

## Topics:
- add: ModelAdmin.has_add_permission()
- change: ModelAdmin.has_change_permission()
- delete: ModelAdmin.has_delete_permission()
- view: ModelAdmin.has_view_permission()

# Topics abstract
1. part1 - Django Project Setup
   1. Create new project
    ```
    py manage.py startproject blog
    # update INSTALLED_APPS in settings.py
    py manage.py makemigrations
    py manage.py migrate
    ```
   3. Make a custom admin area
    ```
    class BlogAdminArea(admin.AdminSite):
        site_header = 'Blog Database'

    blog_site = BlogAdminArea(name='BlogAdmin')

    blog_site.register(models.Post)
    ```
   4. Create users
      1. Superuser
      2. Admin
      ```
      py manage.py createsuperuser admin
      py manage.py createsuperuser user
      # Set the superuser status to null in the user info in the user menu
      ```

2. Appling Permissions
   1. add: ModelAdmin.has_add_permission()
   2. change: ModelAdmin.has_change_permission()
   3. delete: ModelAdmin.has_delete_permission()
   4. view: ModelAdmin.has_view_permission()
   ```
    class BlogAdminArea(admin.AdminSite):
        site_header = 'Blog Database'

    class TestAdminPermissions(admin.ModelAdmin):

        def has_add_permission(self, request):
            return False

        def has_change_permission(self, request, obj=None):
            return False

        def has_delete_permission(self,request,obj=None):
            return False

        def has_view_permission(self,request,obj=None):
            return False

    blog_site = BlogAdminArea(name='BlogAdmin')

    blog_site.register(models.Post, TestAdminPermissions)
    blog_site.register(models.Books)
   ```
3. Extending Functionality Permissions
   1. Extending permissions to provide additional functionality:
      1. Decisions based upon user