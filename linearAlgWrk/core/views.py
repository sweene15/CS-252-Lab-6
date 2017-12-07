import logging
from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.shortcuts import redirect
from  .forms import InputForm, SizeForm, SelectForm, EntryForm
# Create your views here.


#def MainView(request, ):
#    if request.method == 'GET':
#        input_form = InputForm(request.GET)
#        size_form = SizeForm(request.GET)
#        return render(request, 'core/index.html', {'size_form':size_form, 'input_form':input_form,})        



class MainView(TemplateView):
    template_name = 'core/index.html'
    def get(self, request, *args, **kwargs):
        input_form = InputForm(self.request.GET or None)
        size_form = SizeForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['size_form'] = size_form
        context['input_form']= input_form
        if  'dataFlag' in request.session:
            context['clean_row_size'] = request.session['row_size']
            context['clean_col_size'] = request.session['col_size']
            entry_form = EntryForm(self.request.GET or None)
            context['entry_form'] = entry_form
            #del request.session['data_flag']
            #del request.session['row_size']
            #del request.session['col_size']

        if 'input_type' in request.session:
            context['clean_input_type'] = request.session['input_type']
            select_form = SelectForm(self.request.GET or None)
            context['select_form'] = select_form
            del request.session['input_type']

        return render(request, 'core/index.html', context)

class InputFormView(FormView):
    form_class = InputForm
    template_name = 'core/index.html'
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        input_form = self.form_class(request.POST)
        if input_form.is_valid():
            input_form.save()
            input_type = input_form.cleaned_data['input_type']
            request.session['input_type'] = input_type
            return redirect('/')
        else:
            return redirect('/')

class SizeFormView(FormView):
    form_class = SizeForm
    template_name = 'core/index.html'
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        size_form = self.form_class(request.POST)
        if size_form.is_valid():
            row_size = size_form.cleaned_data['row_size']
            col_size = size_form.cleaned_data['col_size']
            dataFlag = True
            size_form.save()
            request.session['col_size'] = col_size
            request.session['row_size'] = row_size
            request.session['dataFlag'] = dataFlag
            return redirect('/')
        else:
            return redirect('/')

class SelectFormView(FormView):
    form_class = SelectForm
    template_name = 'core/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        select_form = self.form_class(request.POST)
        if select_form.is_valid():
            select_form.save()
            return redirect('/')
        else:
            return redirect('/')

class EntryFormView(FormView):
    form_class = EntryForm
    template_name = 'core/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        entry_form = self.form_class(request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return redirect('/')
        else:
            return redirect('/')

