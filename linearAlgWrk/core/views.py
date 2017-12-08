import logging
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from  .forms import InputForm, SizeForm, EntryNewForm, RemoveForm, ViewerForm
from django.core import validators
from django.db import IntegrityError
from .models import Varia
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
        input_form = InputForm(self.request.GET or None, username=request.user.username)
        size_form = SizeForm(self.request.GET or None)
        remove_form = RemoveForm(self.request.GET or None, username=request.user.username)
        viewer_form = ViewerForm(self.request.GET or None, username=request.user.username)
        context = self.get_context_data(**kwargs)
        context['size_form'] = size_form
        context['input_form']= input_form
        context['remove_form']= remove_form
        context['viewer_form']= viewer_form
        if 'array_row1' in request.session:
            context['array_row1'] = request.session['array_row1']
            context['array_row2'] = request.session['array_row2']
            context['array_row3'] = request.session['array_row3']
            context['array_row4'] = request.session['array_row4']
            context['array_row5'] = request.session['array_row5']

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
            #logging.warning(new_list)
            request.session['new_list'] = new_list
            new_entry_form = EntryNewForm(self.request.GET or None, exclude_list=new_list)
            context['new_entry_form'] = new_entry_form
            #del request.session['data_flag']
            #del request.session['row_size']
            #del request.session['col_size']

        return render(request, 'core/index.html', context)

class InputFormView(FormView):
    form_class = InputForm
    template_name = 'core/index.html'
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        input_form = self.form_class(request.POST)
        if input_form.is_valid():
            #input_form.save()
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


class EntryNewFormView(FormView):
    form_class = EntryNewForm
    template_name = 'core/index.html'
    success_url = '/'


    def post(self, request, *args, **kwargs):
        logging.warning(request.session['new_list'])
        new_entry_form = EntryNewForm(self.request.POST, exclude_list=request.session['new_list'])
        if new_entry_form.is_valid():
            var = new_entry_form.save()
            if var:    
                var.user = request.user
                test = request.user.username
                logging.warning(var.user.username)
                var.row_length = int(request.session['row_size'])
                var.col_length = int(request.session['col_size'])
                try:
                    var.save();
                except Exception as e: 
                    logging.warning("Duplicate")
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
            var1 = remove_form.cleaned_data['input_1']
            Varia.objects.filter(id=var1.id).delete()
            return redirect('/')
        else:
            return redirect('/')

class ViewerFormView(FormView):
    form_class = ViewerForm
    template_name = 'core/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        viewer_form = self.form_class(request.POST)
        if viewer_form.is_valid():
            
            request.session['array_test'] = 'this is a test'
            var1 = viewer_form.cleaned_data['input_1']

            r1e1 = var1.row1element1
            if  r1e1 == None:
                r1e1 = ''
            r1e2 = var1.row1element2
            if  r1e2 == None:
                r1e2 = ''
            r1e3 = var1.row1element3
            if  r1e3 == None:
                r1e3 = ''
            r1e4 = var1.row1element4
            if  r1e4 == None:
                r1e4 = ''
            r1e5 = var1.row1element5
            if  r1e5 == None:
                r1e5 = ''
            r2e1 = var1.row2element1
            if  r2e1 == None:
                r2e1 = ''
            r2e2 = var1.row2element2
            if  r2e2 == None:
                r2e2 = ''
            r2e3 = var1.row2element3
            if  r2e3 == None:
                r2e3 = ''
            r2e4 = var1.row2element4
            if  r2e4 == None:
                r2e4 = ''
            r2e5 = var1.row2element5
            if  r2e5 == None:
                r2e5 = ''
            r3e1 = var1.row3element1
            if  r3e1 == None:
                r3e1 = ''
            r3e2 = var1.row3element2
            if  r3e2 == None:
                r3e2 = ''
            r3e3 = var1.row3element3
            if  r3e3 == None:
                r3e3 = ''
            r3e4 = var1.row3element4
            if  r3e4 == None:
                r3e4 = ''
            r3e5 = var1.row3element5
            if  r3e5 == None:
                r3e5 = ''
            r4e1 = var1.row4element1
            if  r4e1 == None:
                r4e1 = ''
            r4e2 = var1.row4element2
            if  r4e2 == None:
                r4e2 = ''
            r4e3 = var1.row4element3
            if  r4e3 == None:
                r4e3 = ''
            r4e4 = var1.row4element4
            if  r4e4 == None:
                r4e4 = ''
            r4e5 = var1.row4element5
            if  r4e5 == None:
                r4e5 = ''
            r5e1 = var1.row5element1
            if  r5e1 == None:
                r5e1 = ''
            r5e2 = var1.row5element2
            if  r5e2 == None:
                r5e2 = ''
            r5e3 = var1.row5element3
            if  r5e3 == None:
                r5e3 = ''
            r5e4 = var1.row5element4
            if  r5e4 == None:
                r5e4 = ''
            r5e5 = var1.row5element5
            if  r5e5 == None:
                r5e5 = ''
            
            array_row1 ='{} {} {} {} {}\n'.format(r1e1, r1e2, r1e3, r1e4, r1e5)
            array_row2 ='{} {} {} {} {}\n'.format(r2e1, r2e2, r2e3, r2e4, r2e5)
            array_row3 ='{} {} {} {} {}\n'.format(r3e1, r3e2, r3e3, r3e4, r3e5)
            array_row4 ='{} {} {} {} {}\n'.format(r4e1, r4e2, r4e3, r4e4, r4e5)
            array_row5 ='{} {} {} {} {}\n'.format(r5e1, r5e2, r5e3, r5e4, r5e5)

            request.session['array_row1'] = array_row1
            request.session['array_row2'] = array_row2
            request.session['array_row3'] = array_row3
            request.session['array_row4'] = array_row4
            request.session['array_row5'] = array_row5

            #viewer_form.save()
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


