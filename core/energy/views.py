from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.templatetags.static import static
from .models import *
from .forms import *





def home(request):
    data = info.objects.last()
    latest_pics = galleryModel.objects.all()[:6]
    form        = clientForm()
    selectPrice = electricityPrice.objects.all()
    context={
      'latest_pics':latest_pics,
      'form'       :form,
      'selectPrice':selectPrice,
      'data':data
    }
    return render(request,'index.html', context)


def generated_data(request):
    if request.method == "POST":
      price = request.POST.get('powerPrice')
      data  = electricData.objects.get(id=price)
      form  = clientForm(request.POST)
      if form.is_valid():
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        if not phone and not email:
          pass
        else:
         form.save()

    context={
      'data':data
    }
    return render(request,'generated.html', context)

