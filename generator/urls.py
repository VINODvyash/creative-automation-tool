from django.urls import path
from.views import generate_creatives

urlpatterns = [
    path('generate/', generate_creatives),

]