from django import forms
from productapp.models import Category,Product
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"