# part5-field-and-fieldset-customisation
part5-field-and-fieldset-customisation

## Django Admin Series
- ModelAdmin options - Fields

## Topics:
- Selecting fields
- Fieldsets
  - Fields, Descriptions, Classes
- Help Text
- Building a coustom form
- 
# Topics abstract
1. Selecting fields
    ```
    # admin.py
    from django.contrib import admin
    from .models import Post, Cetegory

    class PostAdmin(admin.ModelAdmin):
        fields = ['title', ('author', 'slus')] # ('author', 'slus') make group

    admin.site.register(Post,PostAdmin)
    ```
    
3. Fieldsets
  - Fields, Descriptions, Classes
     ```
    # admin.py
    from django.contrib import admin
    from .models import Post, Cetegory

    TEXT = 'Some text that we can include'

    class PostAdmin(admin.ModelAdmin):
        fieldsets = (
            ('Section 1', {
                'fields': ('title','author',)
                'description': '%s' % TEXT, # Write a description under this section heading
            }),
            ('Section 2', {
                'fields': ('slug',),
                'classes': ('collapse',), # make hide / show button on this section heading
            }),
        )

    admin.site.register(Post,PostAdmin)
    ```
3. Help Text
   1. Field Text
        ```
        # models.py 
        ex) title = models.CharField(max_length=250, help_text="This is the title")
            # This field option automatically builds field help text
        ```
4. Building a coustom form
    ```
    # admin.py
    from django.contrib import admin
    from .models import Post
    from django import forms

    class PostForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['title'].help_text = 'New Help Text'

        class Meta:
            model = Post
            exclude = ('slug',) # Hide this field 

    
    class PostFormAdmin(admin.ModelAdmin):
        form = PostForm


    admin.site.register(Post, postFormAdmin)
    ```