from django.contrib import admin
from . import models

# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    site_title = "Blog Post Admin Portal"
    index_title = "Welcome to Blog Admin"

blog_site = BlogAdminArea(name='BlogAdmin')

admin.site.register(models.Post)
blog_site.register(models.Post)