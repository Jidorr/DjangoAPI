# Django API
First steps at learning to create a django API, reads a specific csv file format and processes and stores it.

## HOW TO
Django has been used to create an API that we can use for file processing. First, we need to install the 
requirements.txt modules needed to run the application. Once that is done, we can start the server running
the following command inside our project folder:

$ python manage.py runserver

We can then open our web browser and go to the following URL: http://127.0.0.1:8000/files
In this page, we will be able to see, download and delete all the uploaded files (once we have uploaded some).
If we click on the "Upload new file" button, we will be redirected to http://127.0.0.1:8000/files/upload_file  
which is the page used to upload our csv file. We can give it a name and then select the file to upload.
Now we are redirected to the initial page, where our new uploaded file shows up. If we click on Download,
we will get the newly processed csv file. If we upload different files with the same name, they will be 
renamed so that there is no conflict.

Expected csv format:
<div align="center">
    <img src="csv_format.png?raw=true">
</div>