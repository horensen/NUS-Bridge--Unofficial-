import app_datastore
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


def load_form():
    upload_url = blobstore.create_upload_url('/upload')
    temp='<html><body><form action="'+upload_url+'" method="POST" enctype="multipart/form-data">'
    temp+='Upload File: <input type="file" name="file"><br> <input type="submit"name="submit" value="Submit"> </form></body></html>'
    return temp