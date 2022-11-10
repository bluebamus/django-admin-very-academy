# part11-csv-file-upload
part11-csv-file-upload
youtube site link : [Django Admin CSV file upload](https://www.youtube.com/watch?v=BLxCnD5-Uvc&list=PLOLrQ9Pn6cazhaxNDhcOIPYXt2zZhAXKO&index=12)
github link : [YT_Django_Admin_csv_Button_Upload](https://github.com/veryacademy/YT_Django_Admin_csv_Button_Upload)
# Top Topics:
- Custom admin button action Populate a table from a.asv file
## Django Admin Series
- csv file upload
## Topics:
- Override admin template
- Create custom admin page 
- Populate a table from an uploaded .csv file
# Topics abstract
- If user want to user parent template, can use {{ block.super }}
  - doc link : [The Django template language](https://docs.djangoproject.com/en/4.1/ref/templates/language/)
1. Create html in templates/admin
   1. csv_upload.html is in templates/admin
      1. this file will override the parent template
   2. change_list.html is in templates/admin/bank/customer
      1. this file will make new form to upload csv file
2. Override the function of  'get_urls', make new path
   1. doc link : [The Django admin site](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)
3. Define a new view function with the name 'upload_csv'