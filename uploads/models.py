from django.db import models
from PIL import Image
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files import File
from django.urls import reverse
import os

# Create your models here.

fs = FileSystemStorage(location='/media/images/thumbnails')

# Modelo alternativo para usar com sorl-thumbnail para generar
# automaticamente as thumbnails
class UploadedFiles(models.Model):
    descricao = models.CharField(max_length=150)
    dimensao = models.CharField(max_length=30)
    formato = models.CharField(max_length=10)
    arquivo = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.descricao   
    
    def save(self, *args, **kwargs):
        if not self.dimensao:
            size = (128, 128)
            im = Image.open(self.arquivo)
            self.dimensao = im.size 
            self.formato = im.format            
        return super().save(*args, **kwargs)

def criar_thumbnail(image, formato):

    size = (200, 200)
    im = Image.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    im.save(thumb_io, formato, quality=99)
    thumbnail = File(thumb_io, name=image.name)

    return thumbnail

# Modelo usado
class UploadedFilesThumb(models.Model):
    # Campos do modelo
    descricao = models.CharField(max_length=150)
    dimensao = models.CharField(max_length=30)
    formato = models.CharField(max_length=10)
    arquivo = models.ImageField(upload_to='images/')
    thumb = models.ImageField(upload_to='images/thumbnails/')

    def __str__(self):
        return self.descricao

    # def get_absolute_url(self):
    #     return reverse("downloaded", kwargs={"pk": self.pk, "slug":self.descricao})
       
    # Setando os campos que extraem os dados da foto
    def save(self, *args, **kwargs):
        if not self.dimensao:            
            im = Image.open(self.arquivo)
            self.dimensao = "{} x {}".format(im.size[0], im.size[1]) 
            self.formato = im.format   
            self.thumb = criar_thumbnail(self.arquivo, self.formato)
        return super().save(*args, **kwargs)