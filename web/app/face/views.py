from django.shortcuts import render, redirect
from . import models
import cv2
from imutils import url_to_image

def index(request):
    if request.method == 'POST':
        
        # TO DO save to Url
        url = models.Url.objects.create(
            image_url=request.POST.get('image_url', ''))
        
        url.save()

        return redirect('/face')

    urls = models.Url.objects.all()

    context = {'image_urls': urls}
    return render(request, 'face/index.html', context)
