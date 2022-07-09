from django import forms

from .models import Produto
from django_svg_image_form_field import SvgAndImageFormField


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }