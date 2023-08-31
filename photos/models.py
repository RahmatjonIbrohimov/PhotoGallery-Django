from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class PhotosModel(models.Model):
    post_img = models.ImageField(upload_to='photos/')
    post_auth = models.ForeignKey(User, on_delete=models.CASCADE)
    post_header = models.CharField(max_length=50)
    post_content = models.CharField(max_length=255)
    post_date = models.DateTimeField(default=timezone.datetime.now)

    class Meta:
        db_table = 'gallery'

    def __str__(self):
        return self.post_header
