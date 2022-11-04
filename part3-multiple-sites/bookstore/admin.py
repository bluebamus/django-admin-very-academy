from django.contrib import admin
from . import models

# Register your models here.
class BookStoreAdminArea(admin.AdminSite): 
    site_header = 'BookStore Admin Area'
    site_title = "BookStore Post Admin Portal"
    index_title = "Welcome to BookStore Admin"
    
bookstore_site = BookStoreAdminArea(name='BookStoreAdmin')

admin.site.register(models.Reply)
bookstore_site.register(models.Reply)