from django.contrib.admin.apps import AdminConfig 

class BookstoreAdminConfig(AdminConfig):
    default_site = 'bookstore.admin.BookStoreAdminArea'
