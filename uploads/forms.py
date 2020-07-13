from django import forms
from .models import UploadedFiles, UploadedFilesThumb

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFilesThumb
        fields = ['descricao', 'arquivo']