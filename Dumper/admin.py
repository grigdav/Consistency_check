from django.contrib import admin

# Register your models here.

from .models import ENodeBFunction, AdmissionControll

admin.site.register(ENodeBFunction)

admin.site.register(AdmissionControll)