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
    
    # response = HttpResponse(content_type='application/force-download')
    # response['Content-Disposition'] = f'attachment; filename="image"'

    # def get(self,request,file_name):
    #     response = HttpResponse(content_type='application/force-download')
    #     response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    #     response['X-Sendfile'] = smart_str(path_to_file)
        # file_path = settings.MEDIA_ROOT +'/'+ file_name
        # file_wrapper = FileWrapper(open(file_path,'rb'))
        # file_mimetype = mimetypes.guess_type(file_path)
        # response = HttpResponse(file_wrapper, content_type=file_mimetype )
        # response['X-Sendfile'] = file_path
        # response['Content-Length'] = os.stat(file_path).st_size
        # response['Content-Disposition'] = 'attachment; filename=%s/' % str(file_name) 
        # return response
    
    # def get(self, request, *args, **kwargs):

    #     response = HttpResponse(content_type='application/force-download')
    #     response['Content-Disposition'] = f'attachment; filename="image"'
    #     # response['X-Sendfile'] = smart_str(path_to_file)

    #     return super().get(request, *args, **kwargs)



# def FotosDownloaded(request):

#     response = HttpResponse(content_type='application/force-download')
#     response['Content-Disposition'] = f'attachment; filename="image.jpg"'

#     return response
