from django.urls import path
from . import views
#    ^. means from the same folder
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webkiosk' #useful if you have multiple apps with same names like multiple indexes
urlpatterns = [
    path('',views.index, name='index'),
    #when we visit a specific url then  it's gonna go to views then execute index
    ## the third one, we are naming the url -- allows us to reference it using the name index 
    
    #localhost:8000/webkiosk/Food
    path("food/", views.listfood, name="food-list"),
    #executes listfood function

    #localhost:800/webkiosk/food/new #get request to see the form 
    #clicking submit is a post request
    path("food/new/", views.createfood, name='food-create'),

    #localhost:8000/webkiosk/food/<id>
    path('food/<int:pk>',views.detailfood , name='food-detail'),

    #localhost:8000/webkiosk/food/<id>/edit/
    #localhost:8000/webkiosk/food/4/edit/
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),

    #localhost:8000/webkiosk/food/<id>/delete/
    #localhost:8000/webkiosk/food/4/delete
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),

    #localhost:8000/webkiosk/customers
    #call a view function named listcustomers
    #name the url pattern as customers-list
    path('customers/', views.listcustomers, name='customers-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)