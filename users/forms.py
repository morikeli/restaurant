from .models import Food, Tables, FoodOrders
from django import forms


class AddNewFoodForm(forms.ModelForm):
    SELECT_FOOD = (
        (None, '-- Select food --'),

    )
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'type': 'text', 'class': 'mb-2'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}))
    type = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_FOOD)

    class Meta:
        model = Food
        fields = '__all__'


class AddNewTableForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}))
    seats = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'class': 'mb-2'}))
    
    class Meta:
        model = Tables
        fields = '__all__'


class PlaceFoodOrderForm(forms.ModelForm):
    SELECT_ORDER= (
        (None, '-- Select your order --'),
        ('Booked table', 'I have booked a table'),
        ('Take away', 'Take away'),
    )
    type = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select', 'class': 'mb-2'}), choices=SELECT_ORDER)

    class Meta:
        model = FoodOrders
        fields = '__all__'

