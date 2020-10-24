from django.db import models

# Create your models here.

class galleryModel(models.Model):
    
    place    = models.CharField(max_length=50, null=False,blank=False)
    picPlace = models.ImageField(null=True)
    kwPlace  = models.DecimalField(null=True,blank=False,decimal_places=1,max_digits=6)

    def __str__(self):
        return self.place + " " +str(self.kwPlace) + " kW"
