# THIS IS THE VIEWS.PY FOR THE APP!!!
# cars_and_brands/views.py      
from django.shortcuts import render

from .models import Brand, Car

# /brands # show the list of all the car brands
def list_brands(request):
    brand_list = Brand.objects.order_by('id')
    data = {
        'brand_list' : brand_list
    }
    print(len(data['brand_list']))
    return render(request, 'cars_and_brands/list_brands.html', data)

# /brands/new/ renders new_brand.html for userinput brand name & lets them insert a new brand name
def new_brand(request):
    # print(request.method)
    if request.method == 'POST':
        new_brand_name = request.POST['new_brand_name']
        print(new_brand_name)       # confirm userinput has been passed
        # insert data into cars_and_brands_brand table
        Brand.objects.create(brand_name=new_brand_name)

    return render(request, 'cars_and_brands/new_brand.html')

# Helper method to get brand data from Brand
def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)

# render see_brand.html to see brand given id in the URL /brand/x/
def see_brand(request, id):
    brand = get_brand(id)
    return render(request, 'cars_and_brands/see_brand.html', {'brand':brand})

# /brand/id/edit Change a brand's name
def edit_brand(request, id):
    # print(request.method)
    brand = get_brand(id)

    if request.method == 'POST':
        new_brand_name = request.POST['new_brand_name']
        
        # get the brand and update it's name
        Brand.objects.filter(id=id).update(brand_name = new_brand_name)

    return render(request, 'cars_and_brands/edit_brand.html', {'brand':brand})


##########################################################


# Shows list of all cars of a brand, given the brand's id
def list_cars(request, brand_id):
    brand = get_brand(brand_id)
    car_list = brand.cars.filter(brand=brand)

    data = {
        'brand' : brand,
        'car_list' : list(car_list)
    }
    # print(list(car_list))
    return render(request, 'cars_and_brands/list_cars.html', data)


# Takes in car info in new_car.html, creates a new car
def new_car(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == 'POST':
        # insert data into cars_and_brands_brand table
        Car.objects.create(brand_id=brand_id, color=request.POST['color'], number_of_seats=request.POST['num_seats'])

    return render(request, 'cars_and_brands/new_car.html', {'brand':brand})


# Helper method to get car data from Car
def get_car(car_id):
    return Car.objects.get(id=car_id)

# See car info given brand id and car id
def see_car(request, brand_id, car_id):
    print(f"brand id arg: {brand_id}")
    print(f"car id arg: {car_id}")

    brand = get_brand(brand_id)
    target_car = get_car(car_id)
    data = {
        'brand': brand,
        'car': target_car
    }
    print(f"brand id: {brand.id}")
    print(f"car id: {target_car.id}")

    return render(request, 'cars_and_brands/see_car.html', data)


# edit car color and number of seats, given brand and car id
# DOESN'T ALLOW USER TO CHANGE BRAND OF THEIR CAR...
def edit_car(request, brand_id, car_id):    
    brand = get_brand(brand_id)
    if request.method == 'POST':
        print(request.POST)
        # update data into cars_and_brands_brand table
        Car.objects.filter(id=car_id).update(color=request.POST['new_color'], number_of_seats=int(request.POST['new_seat_num']))

    car = get_car(car_id)
    data = {
        'brand': brand,
        'car': car
    }
    return render(request, 'cars_and_brands/edit_car.html', data)