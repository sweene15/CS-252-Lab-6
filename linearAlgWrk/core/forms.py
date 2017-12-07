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
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Var
        fields = ('row1element1', 'row1element2', 'row1element3', 'row1element4', 'row1element5', 
                    'row2element1', 'row2element2', 'row2element3', 'row2element4', 'row2element5',
                    'row3element1', 'row3element2', 'row3element3', 'row3element4', 'row3element5',
                    'row4element1', 'row4element2', 'row4element3', 'row4element4', 'row4element5',
                    'row5element1', 'row5element2', 'row5element3', 'row5element4', 'row5element5',
                    )

class RemoveForm(forms.ModelForm):
    input_1 = forms.ModelChoiceField(queryset=Var.objects.all())
    class Meta:
        model = Input
        fields = ('input_1',)



class EntryNewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        exclude_list=kwargs.pop('exclude_list', '')
        super(EntryNewForm, self).__init__(*args, **kwargs)

        for field in exclude_list:
            del self.fields[field]
    class Meta:
        model = Var
        fields = '__all__'




#def EntryNewForm(self, exclude_list, *args, **kwargs):
#    class MyEntryNewForm(forms.ModelForm):
 #       class Meta:
 #           model = Var
  #          exclude = exclude_list

   #     def __init__(self):
   #         super(MyEntryNewForm, self).__init__(*args, **kwargs)
#
 #   return MyEntryNewForm()


















         


