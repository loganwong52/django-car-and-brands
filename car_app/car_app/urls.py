# THIS IS THE URLS.PY FOR THE PROJECT
from django.urls import path, include

urlpatterns = [
    path('brands/', include('cars_and_brands.urls')),
]
