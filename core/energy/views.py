from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from .models import *
from .forms import *
import re
#we are validating email in this way cuz U've read that django email validator can be bit fussy
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def check(email):  
    if(re.search(regex,email)):  
        return 1 
    else:  
        return 0



def home(request):
    latest_pics = galleryModel.objects.all()[:6]
    form        = clientForm()
    selectPrice = electricityPrice.objects.all()
    context={
      'latest_pics':latest_pics,
      'form'       :form,
      'selectPrice':selectPrice,
    }
    return render(request,'index.html', context)


def generated_data(request):
    if request.method == "POST":
      price = request.POST.get('powerPrice')
      data  = electricData.objects.get(id=price)
      form  = clientForm(request.POST)
     # if form.is_valid():
       # phone = form.cleaned_data['phone']
        #email = form.cleaned_data['email']
        #if not phone and not email:
        #  pass
        #else:
         #   form.save()

    context={
      'data':data
    }
    return render(request,'generated.html', context)
