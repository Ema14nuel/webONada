from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

#models
from apps.products.models import ProductPresentation, Product, Category

class formFilterProduct(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(formFilterProduct, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_filter_product'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Fieldset(
                'Filter Products',
                Row(
                    Column('category', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
            )
        )
    