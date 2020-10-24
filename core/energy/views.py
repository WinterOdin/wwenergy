from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from .models import *

def home(request):
    latest_pics = galleryModel.objects.all()[:6]



    
    context={
      'latest_pics':latest_pics,
    }
    return render(request,'index.html', context)
