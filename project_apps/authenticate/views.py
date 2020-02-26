from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'auth/sign-in.html')
    else:
        return render(request, 'auth/sign-in.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('sign-in')

    else:
        form = RegistrationForm()

    return render(request, 'auth/sign-up.html', {'form':form})
