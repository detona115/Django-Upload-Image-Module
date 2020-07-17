from django.contrib import admin

# Register your models here.
from .models import UploadedFiles, UploadedFilesThumb


class CustomUploadForm(admin.ModelAdmin):      
    
    list_display = ('descricao', 'arquivo')

admin.site.register(UploadedFiles)
admin.site.register(UploadedFilesThumb, CustomUploadForm)
