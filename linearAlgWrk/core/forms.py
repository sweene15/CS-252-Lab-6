from django import forms

from .models import Input
from .models import Var


class SizeForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ['row_size', 'col_size']

class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ['input_type']
        labels = {
            'input_type': ('Data'),
        }

class SelectForm(forms.ModelForm):
    input_1 = forms.ModelChoiceField(queryset=Var.objects.all())
    input_2 = forms.ModelChoiceField(queryset=Var.objects.all())
    class Meta:
        model = Input
        fields = ('input_1', 'input_2',)


