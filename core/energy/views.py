from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from .models import *

def home(request):
   
    context={
      
    }
    return render(request,'main.html', context)
