# part8-django-admin-filters-intro-and-custom-filter-part-1
part8-django-admin-filters-intro-and-custom-filter-part-1
youtube link : [Django Admin Filters Intro and Custom Filter - Part 1 - Django Admin Series - Part 8
](https://www.youtube.com/watch?v=E-Ts39IUGNc&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=10)

# Top Topics:

## Django Admin Series
- Introduction to Django admin filters

## Topics:
- Create simple filters
- Custom filter

# Topics abstract
1. django official web page : [The Django admin site](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)
2. Update models.py
3. Create Filter class at admin.py
   1. define simple filter option using 'list_filter' parameter
        ```
        class Filter(admin.ModelAdmin):
            list_display = ('id','email','created_at','role','is_active')
            list_filter = ('is_active','role','created_at')
        ```
4. Users can use 'filters' on their profile page on the admin site
5. Create 'Emailfilter' class using abstract class of simplelistfilter
   1. title parameter is filter title
   2. parameter_name is column name (must be same with database field name)
   3. lookups - a method that implements what is visible in the filter window
   4. queryset - defines what happens when the user selects one of the filter options.
   5. code :
        ```
        class EmailFilter(SimpleListFilter):
            title = 'Email Filter'
            parameter_name = 'user_email'

            def lookups(self,request,model_admin):
                return (
                    ('has_email', 'has_email'),
                    ('no_email', 'no_email')
                )

            def queryset(self,request,queryset):
                if not self.value():
                    return queryset
                if self.value().lower() == 'has_email':
                    return queryset.exclude(user__email='')
                if self.value().lower() == 'no_email':
                    return queryset.filter(user__email='')


        class Filter(admin.ModelAdmin):
            list_display = ('id','email','created_at','role','is_active')
            list_filter = ('is_active','role','created_at', EmailFilter)
        ```