import re
from django import forms
from django.utils import timezone
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Hidden, Div, Submit

#models
from apps.products.models import Category

class ProductFilter(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, required=False)
    category = forms.ModelMultipleChoiceField(
        label="Categoría",
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    price_min = forms.DecimalField(
        label="Precio mínimo",
        required=False,
        min_value=0,
        decimal_places=2,
        max_digits=10
    )
    price_max = forms.DecimalField(
        label="Precio máximo",
        required=False,
        min_value=0,
        decimal_places=2,
        max_digits=10
    )