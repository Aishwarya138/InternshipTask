from django.contrib import admin

# Register your models here.
from .models import CandleData

admin.site.register(CandleData)