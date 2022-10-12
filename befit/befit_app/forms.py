from dataclasses import field
from django import forms


class FoodTracker(forms.Form):
    
    name = forms.CharField(max_length=200, label="Food")
    quantity = forms.CharField(max_length=200, label="Amount")
    calorie = forms.CharField(max_length=200, label="kcal")
    
    