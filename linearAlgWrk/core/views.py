from django.shortcuts import render
from  .forms import InputForm
# Create your views here.

def index(request):
    input_str = InputForm()
    return render(request, 'core/index.html', {'input_str':input_str})

