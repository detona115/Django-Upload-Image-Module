from django.contrib import admin

# Register your models here.
from .models import UploadedFiles

admin.site.register(UploadedFiles)
