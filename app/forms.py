from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta: 
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']
        
    def clean(self):
        cleaned_data = super().clean()
        price_data = cleaned_data.get('price')
        desc_data = cleaned_data.get('description')
        
        # validate that the price is not too expensive
        if price_data >= 1000:
            self.add_error('price', 'Price is too expensive.')
        
        # validate that the description is not too short
        if len(desc_data) < 20:
            self.add_error('description', 'Product must have a good description.')
 