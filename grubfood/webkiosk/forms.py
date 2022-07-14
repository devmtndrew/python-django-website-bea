from django.forms import ModelForm
from .models import Food

class FoodForm(ModelForm):
    #ModelForm is a helper class
    class Meta:
        model = Food #this food form model is for the food model
        fields = ['name', 'description', 'price'] #specifying what fields should show up in the form
