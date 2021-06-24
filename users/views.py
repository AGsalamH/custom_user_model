from django.shortcuts import render
from django.contrib.auth import login
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from users.forms import UserRegistrationForm, LoginForm
from django.views.generic.base import TemplateView

# Create your views here.
     
class RegisterView(TemplateView):
    template_name = 'test_form.html'
    extra_context = {
        'form': UserRegistrationForm()
    }
    
    def post(self, request:HttpRequest, *args, **kwargs):
        '''
        Create new user and save it to database
        '''
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/admin/')
        return render(request, self.template_name, {
            'form': form
        })


class LoginView(TemplateView):
    template_name = 'test_form.html'
    extra_context = {
        'form': LoginForm()
    }
    
    def post(self, request:HttpRequest, *args, **kwargs):
        '''
        Handling Login
        '''
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            form.confirm_login_allowed()
            login(request, form.user)
            return HttpResponseRedirect('/admin/')
        return render(request, self.template_name, {
            'form': form
        })
