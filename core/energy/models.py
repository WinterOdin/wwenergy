from django.db import models

# Create your models here.

class galleryModel(models.Model):
    
    place    = models.CharField(max_length=50, null=False,blank=False)
    picPlace = models.ImageField(null=True)
    kwPlace  = models.DecimalField(null=True,blank=False,decimal_places=1,max_digits=6)

    def __str__(self):
        return self.place + " " +str(self.kwPlace) + " kW"


class electricityPrice(models.Model):
    price = models.CharField(max_length=100,unique=False)

    def __str__(self):
        return self.price


class electricData(models.Model):
    price_id     = models.ForeignKey(electricityPrice, on_delete=models.CASCADE, null=True)
    kwp           = models.DecimalField(null=True,blank=False,decimal_places=2,max_digits=6)
    paneleM2     = models.CharField(max_length=70,null=True, blank=True)
    sztukiPaneli = models.CharField(max_length=70,null=True, blank=True)
   
    def __str__(self):
        return self.paneleM2 + " metrów kwadratowych"

class client(models.Model):
    name       = models.CharField(max_length=15,null=True, blank=True, )
    surname    = models.CharField(max_length=20,null=True, blank=True, )
    phone      = models.CharField(max_length=9,null=True, blank=True)
    email      = models.CharField(max_length=33,null=True, blank=True)

    
    def __str__(self):
        return str(self.name )+ " " + str(self.surname) 