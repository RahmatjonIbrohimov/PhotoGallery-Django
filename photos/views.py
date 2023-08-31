from django.shortcuts import render

from photos import models


# Create your views here.
def home(request):
    post = models.PhotosModel.objects.all()
    return render(request, 'photos/index.html', {'post': post})
