from django.db import models

class FileUpload(models.Model):
    name = models.CharField(max_length=20) 
    file = models.FileField(upload_to='videos') 
    def __str__(self):
        return self.name