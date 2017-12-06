from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.shortcuts import redirect
from  .forms import InputForm, SizeForm, SelectForm
# Create your views here.

class MainView(TemplateView):
    template_name = 'core/index.html'
    def get(self, request, *args, **kwargs):
        input_form = InputForm(self.request.GET or None)
        size_form = SizeForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['size_form'] = size_form
        context['input_form'] = input_form
        #return render(context, 'core/index.html')
        return self.render_to_response(context)

class InputFormView(FormView):
    form_class = InputForm
    template_name = 'core/index.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        input_form = self.form_class(request.POST)
        if input_form.is_valid():
            input_form.save()
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
            size_form.save()
            return redirect('/')
        else:
            return redirect('/')


