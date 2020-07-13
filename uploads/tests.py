from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
from .views import HomePageView, FotosPageView
from .models import UploadedFilesThumb

# Test home page (home.html)
class HomePageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

        self.upload = UploadedFilesThumb.objects.create(
            descricao = 'test',
            dimensao = '(500, 500)',
            formato = 'JPG',
            arquivo = SimpleUploadedFile(name='fg.jpg', content=open('/code/media/images/fg.jpg', 'rb').read()),
            thumb = SimpleUploadedFile(name='fg.jpg', content=open('/code/media/images/fg.jpg', 'rb').read())
        )

    def test_form_homepage(self):
        self.assertEqual(f'{self.upload.descricao}', 'test')
        self.assertEqual(f'{self.upload.dimensao}', '(500, 500)')
        self.assertEqual(f'{self.upload.formato}', 'JPG')


    def test_homepage(self):
        # test page status code
        self.assertEqual(self.response.status_code, 200)

        # test template used
        self.assertTemplateUsed(self.response, 'home.html')

        # test if the template contains a certain content
        self.assertContains(self.response, 'Django Upload Image Module')

        # test if the template not contains a certain content
        self.assertNotContains(self.response, 'Hi Hellloooo.')

        # test if the correct view is used view
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

# Test fotos (fotos.html)
class FotoPageTests(TestCase):

    def setUp(self):
        url = reverse('listasfotos')
        self.response = self.client.get(url)

    def test_fotopage(self):
        # test page status code
        self.assertEqual(self.response.status_code, 200)

        # test template used
        self.assertTemplateUsed(self.response, 'fotos.html')

        # test if the template contains a certain content
        self.assertContains(self.response, 'Fotos Page')

        # test if the template not contains a certain content
        self.assertNotContains(self.response, 'Hi Hellloooo.')

        # test if the correct view is used view
        view = resolve('/fotos/')
        self.assertEqual(view.func.__name__, FotosPageView.as_view().__name__)