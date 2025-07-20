from django import forms
from .models import Checkorder, Allorder, Destination  

from django.forms import ModelForm

class CheckoutForm(forms.ModelForm):
   
    class Meta:
        model = Checkorder
        exclude = ('paid',)
       
        widgets = {
            'address': forms.Textarea(attrs={'row': 5, 'col': 8}),
        }

class NewFoodForm(forms.ModelForm):
	class Meta:
            model = Destination
            exclude = ('offer',)
            fields = ['name', 'price', 'desc', 'img'] 

            widgets = {
                'name': forms.TextInput(attrs={
                                                'placeholder': 'title',
                                                'class': 'form-control',
                                                'style': 'margin-bottom: 10px',
                                                }),
                'desc': forms.Textarea(attrs={'row': 5, 'col': 8}),
            }          



## 해당 부분에 form에서 입력 받을 속성을 결정합니다. models.py와 동일하게 설정하면 됩니다. ##
## exclude = ('offer',) : to be deleted 