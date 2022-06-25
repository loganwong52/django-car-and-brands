# THIS IS URLS.PY FOR THE APP!!!
from django.urls import path
from . import views

app_name = 'cars_and_brands'

urlpatterns = [
    path('', views.list_brands, name='list_brands'),
    path('new/', views.new_brand, name='new_brand'),
    path('<int:id>/', views.see_brand, name='see_brand'),
    path('edit/<int:id>/',views.edit_brand, name='edit_brand'),
    
    path('cars/<int:brand_id>/', views.list_cars, name='list_cars'),
    path('new/cars/<int:brand_id>/', views.new_car, name='new_car'),
    path('<int:car_id>/cars/<int:brand_id>/', views.see_car, name='see_car'),
    path('edit/<int:car_id>/cars/<int:brand_id>/', views.edit_car, name='edit_car')
]

# /brands # a list of all the car brands
# /brands/new # form for a new car brand
# /brands/<:id> # see a specific car brand
# /brands/<:id>/edit # edit page for a specific car brand

# /brands/<:brand_id>/cars # a list of cars for a specific car brand
# /brands/<:brand_id>/cars/new # form for a new car under a specific car brand
# /brands/<:brand_id>/cars/<:car_id> # see a specific car for a specific car brand
# /brands/<:brand_id>/cars/<:car_id>/edit # edit page for a specific car under a specific car brand