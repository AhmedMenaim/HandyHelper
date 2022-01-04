from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from Users.forms import RegisterationForm, UserAuthenticationForm

# Create your views here.

def registeration_view(request):
    context = {}
    if request.POST:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username').lower()
            firstName =  form.cleaned_data.get('firstName')
            lastName =  form.cleaned_data.get('lastName')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email,username=username,firstName=firstName, lastName=lastName, password=raw_password)
            # login(request,user)
            return redirect('Login')
        else:
            context['registeration_form'] = form
    else:
        form = RegisterationForm()
        context['registeration_form'] = form
    return render(request, 'Register.html',context)


def logout_view(request):
    logout(request)
    return redirect('Dashboard')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("Dashboard")

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("Dashboard")
    
    else:
        form = UserAuthenticationForm()
        
    context['login_form'] = form
    return render(request, 'login.html', context)
