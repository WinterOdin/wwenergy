from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from django.core.mail import send_mail
from .models import *
from .forms import *

def home(request):
    dataFooter  = info.objects.last()
    latest_pics = galleryModel.objects.all()[:6]
    form        = clientForm()
    selectPrice = electricityPrice.objects.all()
    context={
      'latest_pics':latest_pics,
      'form'       :form,
      'selectPrice':selectPrice,
      'dataFooter':dataFooter
    }
    return render(request,'index.html', context)


def generated_data(request):
    dataFooter  = info.objects.last()
    if request.method == "POST":
      price = request.POST.get('powerPrice')
      data  = electricData.objects.get(id=price)
      dataPrice = electricityPrice.objects.get(id=price)
      phone = request.POST.get('phone')
      email = request.POST.get('email')
      name  = request.POST.get('name')
      if not phone and not email:
          pass
      else:
        values = request.POST.copy()
        values['price'] = dataPrice

        #sending mail
        # send_mail(
          #'Nowy klient WWenergy', #subject
          #'Imie i nazwisko klienta:' + values["name"] + values['surname'] + " numer telefontu " + values['phone'] + "email klienta" + values['email'],#content
          #values['email'],#from who 
          #['wwenergywebsite@gmail.com']#)
        form  = clientForm(values)
        if form.is_valid():
          form.save()
        
    context={
      'data':data,
      'dataFooter':dataFooter,
      'name':name
    }
    return render(request,'generated.html', context)

