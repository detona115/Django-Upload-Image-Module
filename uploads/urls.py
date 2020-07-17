from django.urls import path

from .views import HomePageView, FotosPageView #, FotosDownloaded

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # url da página principal
    path('fotos/', FotosPageView.as_view(), name='listasfotos'), # url da página de exibição das fotos    
]
