from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(galleryModel)
admin.site.register(electricityPrice)
admin.site.register(electricData)
admin.site.register(client)