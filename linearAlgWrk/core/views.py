import logging
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from  .forms import InputForm, SizeForm, SelectForm, EntryNewForm, RemoveForm
from django.core import validators
# Create your views here.


#def MainView(request, ):
#    if request.method == 'GET':
#        input_form = InputForm(request.GET)
#        size_form = SizeForm(request.GET)
#        return render(request, 'core/index.html', {'size_form':size_form, 'input_form':input_form,})        



class MainView(TemplateView):
    template_name = 'core/index.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() == False:
            return redirect('/login')
        input_form = InputForm(self.request.GET or None)
        size_form = SizeForm(self.request.GET or None)
        remove_form = RemoveForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['size_form'] = size_form
        context['input_form']= input_form
        context['remove_form']= remove_form

        if  'dataFlag' in request.session:
            context['clean_row_size'] = request.session['row_size']
            context['clean_col_size'] = request.session['col_size']

            temp_list = list()

            if(int(request.session['row_size']) < 5):
                temp_list.append('row1element5')
                temp_list.append('row2element5')
                temp_list.append('row3element5')
                temp_list.append('row4element5')
                temp_list.append('row5element5')

            if(int(request.session['row_size']) < 4):
                temp_list.append('row1element4')
                temp_list.append('row2element4')
                temp_list.append('row3element4')
                temp_list.append('row4element4')
                temp_list.append('row5element4')

            if(int(request.session['row_size']) < 3):
                temp_list.append('row1element3')
                temp_list.append('row2element3')
                temp_list.append('row3element3')
                temp_list.append('row4element3')
                temp_list.append('row5element3')

            if(int(request.session['row_size']) < 2):
                temp_list.append('row1element2')
                temp_list.append('row2element2')
                temp_list.append('row3element2')
                temp_list.append('row4element2')
                temp_list.append('row5element2')

            if(int(request.session['col_size']) < 5):
                temp_list.append('row5element1')
                temp_list.append('row5element2')
                temp_list.append('row5element3')
                temp_list.append('row5element4')
                temp_list.append('row5element5')

            if(int(request.session['col_size']) < 4):
                temp_list.append('row4element1')
                temp_list.append('row4element2')
                temp_list.append('row4element3')
                temp_list.append('row4element4')
                temp_list.append('row4element5')

            if(int(request.session['col_size']) < 3):
                temp_list.append('row3element1')
                temp_list.append('row3element2')
                temp_list.append('row3element3')
                temp_list.append('row3element4')
                temp_list.append('row3element5')

            if(int(request.session['col_size']) < 2):
                temp_list.append('row2element1')
                temp_list.append('row2element2')
                temp_list.append('row2element3')
                temp_list.append('row2element4')
                temp_list.append('row2element5')

            new_list = list(set(temp_list))
            new_list.append('user')
            new_list.append('row_length')
            new_list.append('col_length')
            logging.warning(new_list)
            request.session['new_list'] = new_list
            new_entry_form = EntryNewForm(self.request.GET or None, exclude_list=new_list)
            context['new_entry_form'] = new_entry_form
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


class EntryNewFormView(FormView):
    form_class = EntryNewForm
    template_name = 'core/index.html'
    success_url = '/'


    def post(self, request, *args, **kwargs):
        logging.warning(request.session['new_list'])
        new_entry_form = EntryNewForm(self.request.POST, exclude_list=request.session['new_list'])
        if new_entry_form.is_bound:
            logging.warning('blah')
        if new_entry_form.is_valid():
            var = new_entry_form.save()
            var.user = request.user
            test = request.user.username
            logging.warning(test)
            var.row_length = int(request.session['row_size'])
            var.col_length = int(request.session['col_size'])
            var.save();
            return redirect('/')
        else:
            #new_entry_form.save()
            return redirect('/')


class RemoveFormView(FormView):
    form_class = RemoveForm
    template_name = 'core/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        remove_form = self.form_class(request.POST)
        if remove_form.is_valid():
            entry_form.save()
            ##Remove Var from DB
            return redirect('/')
        else:
            return redirect('/')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
