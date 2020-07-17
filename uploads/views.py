from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import UploadedFiles, UploadedFilesThumb
from django.urls import reverse_lazy
from .forms import UploadForm
from django.db.models import Q

from django.conf import settings
import urllib, mimetypes
from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
import os
from wsgiref.util import FileWrapper


# View na homepage
class HomePageView(CreateView):
    model = UploadedFilesThumb
    form_class = UploadForm
    template_name = "home.html"
    success_url = reverse_lazy("home")

# View da galeria
class FotosPageView(ListView):
    model = UploadedFilesThumb
    template_name = "fotos.html"

    def get_queryset(self):

        query = self.request.GET.get('q')

        if query:
            return UploadedFilesThumb.objects.filter(
                Q(descricao__icontains=query) | Q(formato__icontains=query)
            )
        else:
            return UploadedFilesThumb.objects.all()
    
    

