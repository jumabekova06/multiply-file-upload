from django.urls import  path
from newapp.views import FileUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', FileUploadView.as_view(), name='file-upload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)