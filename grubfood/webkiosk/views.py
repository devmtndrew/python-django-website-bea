from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from .models import Customer, Food
from .forms import FoodForm
# Create your views here.

def index(request):
    return render(request, 'webkiosk/welcome.html')


# food list page
def listfood(request):
    fl = Food.objects.all() #gets all and stores it in fl
    context = {
        'foodlist': fl #fl is a list of all of food in our database and assigning it to the key
        #key : value
        #matches food list under ol in html
    }
    return render(request, "webkiosk/food_list.html", context) #we want to pass the context


# add food page

def createfood(request):
    if request.method == "GET":
        ff = FoodForm()
    elif request.method == "POST":
        #they already typed stuff
        #request.POST passes all the info to the foodform
        ff = FoodForm(request.POST)
        if ff.is_valid():
            ff.save() #form is saved and adds record to database
            return redirect('webkiosk:food-list') #can also be 'webkiosk/food/'

    context = { "form" : ff}
    return render(request, "webkiosk/food_form.html", context )

#django makes a request object for us w/ information such as if its a get or post



#Details View function
def detailfood(request, pk):
    f = Food.objects.get(id=pk) #gets only the one with that id
    context = { 'food': f }
    return render(request,"webkiosk/food_detail.html",context)


# Update Food Record
def updatefood(request, pk):
    f = Food.objects.get(id=pk)
    if request.method == "GET":
        ff = FoodForm(instance=f) #filled in with info from instance f, which record should the isntance use, the form will be filled na in the form
    elif request.method == "POST":
        ff = FoodForm(request.POST, instance = f) #when they click submit #cant be request.POST only because it'll turn everything new, updates instance only
        if ff.is_valid():
            ff.save()
            messages.success(request, 'Food record successfully updated.') #classifying as a success message for when the form's valid

    context = {'form': ff}
    return render(request, 'webkiosk/food_form.html', context)

#Delete Food Records
def deletefood(request, pk):
    f = Food.objects.get(id=pk)
    if request.method == "GET": #get request when u press delete button so the template of confirmation gets rendered
        context = {"food":f}               
        return render(request, 'webkiosk/food_delete.html', context) #only renders the form if they're confirming
    elif request.method == "POST":
        f.delete()
        return redirect('webkiosk:food-list')                  

#Customers list
def listcustomers(request):
    cl = Customer.objects.all() #gets all and stores it in cl
    context = {
        'customerslist': cl #fl is a list of all of food in our database and assigning it to the key
        #key : value
        #matches food list under ol in html
    }
    return render(request, "webkiosk/customers_list.html", context) #we want to pass the context