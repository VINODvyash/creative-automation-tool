from django.contrib import admin
from .models import Brand, Dealership, Asset, Creative

# Register your models here.

admin.site.register(Brand)
admin.site.register(Dealership)     
admin.site.register(Asset)
admin.site.register(Creative)