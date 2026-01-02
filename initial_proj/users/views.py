from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.
def signin(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account is created for {username}')
            return redirect('blog-home')
    else:
        form = UserSignupForm()
    
    return render(request, "users/login.html", {"form": form})