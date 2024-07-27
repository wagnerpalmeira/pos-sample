from django import forms
from .models import Promotion

class CreatePromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'price', 'url', 'category']
