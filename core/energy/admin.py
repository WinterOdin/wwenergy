from django.contrib import admin

# Register your models here.

from .models import *



class electricDataAdmin(admin.ModelAdmin):
    list_display  = ('panele_m2','kwp', 'sztuki_paneli','price_id')
    search_fields = ('panele_m2','kwp')
    list_filter   = ('panele_m2','kwp', 'sztuki_paneli','price_id')


class clientsDataAdmin(admin.ModelAdmin):
    list_display  = ('name','surname','email','phone')
    search_fields = ('name','surname','email','phone')








admin.site.site_header = "Admin Panel WW Energy"
admin.site.register(galleryModel)
admin.site.register(electricityPrice)
admin.site.register(electricData,electricDataAdmin)
admin.site.register(client, clientsDataAdmin)
admin.site.register(info)


