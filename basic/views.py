from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, Loginform, Registerform
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.


def home(request):
    context = {
        'title': "This is home"
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'title': "This is about"
    }
    return render(request, 'home.html', context)


def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': "This is Contacts",
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/contact.html', context)


def login_page(request):
    form = Loginform(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(form.cleaned_data)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # print(request.user.is_authenticated)
            return redirect('home')
        else:
            print('Error user')
        context['form'] = Loginform()
    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = Registerform(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
    return render(request, 'auth/regi.html', context)
