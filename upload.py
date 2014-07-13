import app_datastore
from google.appengine.ext import blobstore

def load_form():
    upload_url = blobstore.create_upload_url('/upload')

