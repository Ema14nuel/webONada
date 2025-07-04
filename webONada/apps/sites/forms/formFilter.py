from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

#models
from apps.products.models import ProductPresentation, Product, Category

class formFilterProduct(forms.Form):

    

    featured_title = forms.CharField(
        required=False, 
        label="Nombre del producto", 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Ingrese título'
                })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_filter_product'
        self.helper.form_method = 'get'

        # Campos del formulario
        self.fields['category'] = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
            required=False,
            widget=forms.CheckboxSelectMultiple, 
            label="Categoría",
        )

        self.helper.layout = Layout(
            Fieldset(
                'Buscar productos',
                Row(
                    Column('featured_title', css_class='form-group col-md-12 mb-3'),
                    css_class='form-row'
                ),
                Row(
                    Column('category', css_class='form-group col-md-12 mb-3'),
                    css_class='form-row'
                ),
            )
        )